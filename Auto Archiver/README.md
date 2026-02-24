# Auto Archiver

## Usage

1. Run the script.
2. The script will scan your Downloads directory and its subdirectories for files that have not been modified in the last 30 days.
3. It will display the list of files that are eligible for archiving.
4. You will be prompted to confirm if you want to archive these files.
5. If you confirm, the script will proceed to archive the files (it only copies the files, but does not move them)

## Note

- The script does not run automatically. You need to run it manually whenever you want to archive old files.

## FAQ

**Q: Can I change the directory that the script scans?**
A: Yes, you can modify the ```os.chdir``` line in the ```cd()``` function to point to a different directory.
