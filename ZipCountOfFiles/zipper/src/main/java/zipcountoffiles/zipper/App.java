package zipcountoffiles.zipper;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.zip.*;

public class App {
	public static void main(String[] args) {
		for (String s : args) {
			if (s.toLowerCase().matches("--help|-help|-h|-\\?|/help|/h|/\\?") || args.length != 3) {
				System.out.println(
						"Run this command with 3 parameters.\nThe parameters must be:\nthe max number of files per zip\nthe directory to zip up\nthe filename to use for zipping.");
				return;
			}
		}
		int count = Integer.valueOf(args[0]);
		String sourceDir = args[1];
		String filename = args[2];
		File directory = null;
		directory = new File(sourceDir);
		List<String> files = new ArrayList<>();
		if (!directory.exists()) {
			System.out.println("Directory " + sourceDir + " not found.");
			return;
		}
		if (filename.endsWith(".zip") || filename.endsWith(".gz")) {
			filename = filename.substring(0, filename.lastIndexOf("."));
		}
		Path path = Paths.get(filename.substring(0, filename.lastIndexOf(File.separator)));
		System.out.println(path.toString());
		File[] filesToZip = directory.listFiles();
		List<String> zipFiles = new ArrayList<>();
		for (int i = 0; i < filesToZip.length; i++) {
			if (filesToZip[i].isFile()) {
				files.add(filesToZip[i].getAbsolutePath());
			}
		}
		if (files.size() == 0) {
			System.out.println("No files to zip.");
			return;
		}
		if (files.size() == 1) {
			System.out.println("There's only 1 file to zip.");
			zipFiles.add(filesToZip[0].getAbsolutePath());
			String zipFilename = filename + ".zip";
			zipFiles(zipFiles, zipFilename);
			return;
		}
		System.out.println("There is more than 1 file to zip.");
		int rangeleft = 1;
		int rangeright = count;
		zipFiles = new ArrayList<String>();
		String zipFilename = filename + "-" + rangeleft + "-" + rangeright + ".zip";
		for (int i = 0; i < files.size(); i++) {
			zipFiles.add(files.get(i));
			if (zipFiles.size() % count == 0) {
				System.out.println("i mod count is 0");
				zipFiles(zipFiles, zipFilename);
				zipFiles = new ArrayList<>();
				rangeleft = rangeleft + count;
				rangeright = rangeright + count;
				zipFilename = filename + "-" + rangeleft + "-" + rangeright + ".zip";
			}
			if (i == files.size() - 1 && zipFiles.size() % count != 0) {
				zipFilename = filename + "-" + rangeleft + "-" + (rangeleft + zipFiles.size() - 1) + ".zip";
				zipFiles(zipFiles, zipFilename);
			}
		}
	}

	private static void zipFiles(List<String> files, String zipFilename) {
		try {
			FileOutputStream fos = new FileOutputStream(zipFilename);
			ZipOutputStream zipOut = new ZipOutputStream(fos);
			for (String file : files) {
				File fileToZip = new File(file);
				FileInputStream fis = new FileInputStream(fileToZip);
				ZipEntry zipEntry = new ZipEntry(fileToZip.getName());
				zipOut.putNextEntry(zipEntry);

				byte[] bytes = new byte[1024];
				int length;
				while ((length = fis.read(bytes)) >= 0) {
					zipOut.write(bytes, 0, length);
				}
				fis.close();
			}
			zipOut.close();
			fos.close();
		} catch (NullPointerException | IOException e) {
			e.printStackTrace();
		}
	}
}