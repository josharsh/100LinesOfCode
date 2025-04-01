package com.example;
import java.io.*;
import java.util.Scanner;
public class DocumentGenerator {
    //Java program to generate basic documentation from java code comments
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the file path");
        String path = sc.
                nextLine();
        File inputFile = new File(path);
        if(createHelpFile( inputFile))
            System.out.println("README.md file created successfully!");
        else
            System.out.println("Error Creating File !");
    }

    /*createHelpFile method, which will create a new README.md file
     using the comments in the java program. */
    private static boolean createHelpFile(File inputFile) throws IOException {
        FileWriter writer = null;
        BufferedReader br = null;
        try {
            //Create an empty README.md file
            File helpFile = new File("README.md");
            writer = new FileWriter(helpFile);
            //Write the static content to newkly created README.md file
            writer.write("# README.md\n");
            writer.write("## This is a sample README.md file created using java program\n\n");
            writer.write("## DOCUMENTATION\n\n");
            try {
                br = new BufferedReader(new FileReader(inputFile));
                String line;
                boolean isMultiLine=false;
                //read the inout java file, one line at a time
                while ((line = br.readLine()) != null) {
                    //check if the line is a comment line
                    if (line.replace("\t","").trim().startsWith("/*")) {
                        isMultiLine = true;
                    }
                    if (isMultiLine) {
                        writer.write(line + "\n");
                    }
                    else if(line.replace("\t","").trim().startsWith("//")) {
                        System.out.println(line);
                        writer.write("##### "+ line +"\n");
                    }

                    if (line.replace("\t","").trim().endsWith("*/")) {
                        isMultiLine = false;
                    }
                }
                return true;
            } catch (FileNotFoundException e) {
                System.out.println("File not found");
                return false;
            } catch (IOException e) {
                System.out.println("An error occurred.");
                return false;
            }

        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
        finally {
            if(writer != null)
                writer.close();
            if(br != null)
                br.close();
        }

    }
}
