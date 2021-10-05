using Microsoft.SqlServer.Management.Smo;
using Microsoft.SqlServer.Management.Common;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Collections.Specialized;

namespace db_dumper {

    class DBTask {
        public string Login { get; set; }
        public string Password { get; set; }
        public string Server { get; set; }
        public string DB { get; set; }
        public string OutputFolder { get; set; }
    }

    class Program {
        static void DumpObjects<T>(SmoCollectionBase objects, string prompt, ScriptingOptions options) where T : NamedSmoObject, IScriptable {
            var isSystemObject = typeof(T).GetProperties().FirstOrDefault(x => x.Name == "IsSystemObject");
            foreach (T sec in objects) {
                if (isSystemObject != null && (bool)isSystemObject.GetValue(sec)) continue;
                StringCollection sc = sec.Script(options);
                Console.WriteLine(prompt + sec.Name);
            }
        }
        static void DumpTask(string fpath) {
            DBTask task = new DBTask();
            try {
                string data = File.ReadAllText(fpath);
                task = JsonConvert.DeserializeObject<DBTask>(data);
            } catch (FileNotFoundException e) {
                Console.WriteLine("Cannot open task file : " + fpath);
                return;
            }
            if (!Directory.Exists(task.OutputFolder)) Directory.CreateDirectory(task.OutputFolder);

            ServerConnection connection = new ServerConnection(task.Server) { LoginSecure = false, Login = task.Login, Password = task.Password, ConnectTimeout = 3 };
           
            Server sqlserv = new Server(connection);
            try {
                Console.WriteLine("Connected server version:" + sqlserv.Information.Version);
            } catch (Exception e) {
                Console.WriteLine("Cannot connect to server: " + task.Server);
                Console.WriteLine(e.Message);
                return;
            }
            Database database = null;
            try {
                database = sqlserv.Databases[task.DB];
            } catch (Exception e) {
                Console.WriteLine("Cannot find database");
                Console.WriteLine(e.Message);
                return;
            }
            string footprint = DateTime.Now.ToString("ddMMyyyy-HHmm");
            string outfile = task.OutputFolder + "/" + footprint + "_" + task.DB + "_schema" + ".sql";

            ScriptingOptions scripterOpts = new ScriptingOptions();
            scripterOpts.FileName = outfile;
            scripterOpts.AppendToFile = true;
            scripterOpts.ScriptForCreateDrop = false;
            scripterOpts.DriForeignKeys = true;
            scripterOpts.Indexes = true;
            scripterOpts.DriAllConstraints = true;
            scripterOpts.DriPrimaryKey = true;

            DumpObjects<Login>(sqlserv.Logins, "Login ", scripterOpts);
            DumpObjects<User>(database.Users, "User ", scripterOpts);

            StringCollection sc1 = database.Script(scripterOpts);
            Console.WriteLine("Database " + database.Name);

            DumpObjects<PartitionFunction>(database.PartitionFunctions, "Partition function ", scripterOpts);
            DumpObjects<PartitionScheme>(database.PartitionSchemes, "Partition scheme ", scripterOpts);
            DumpObjects<Table>(database.Tables, "Table ", scripterOpts);
            DumpObjects<View>(database.Views, "View ", scripterOpts);
            DumpObjects<UserDefinedType>(database.UserDefinedTypes, "User defined type ", scripterOpts);
            DumpObjects<UserDefinedTableType>(database.UserDefinedTableTypes, "User defined table type ", scripterOpts);
            DumpObjects<StoredProcedure>(database.StoredProcedures, "Procedure ", scripterOpts);
            DumpObjects<UserDefinedFunction>(database.UserDefinedFunctions, "Function ", scripterOpts);
            
            connection.Disconnect();
            Console.WriteLine("Done");
        }
        static void Main(string[] args) {
            if (args.Count() == 0) {
                    Console.WriteLine("MSSQL dumper 0.1");
                return;
            }
            foreach (string fpath in args) {
                DumpTask(fpath);
            }
            Console.ReadLine();
        }
    }
}
