import java.io.*;
import java.util.*;
import java.util.regex.*;

/**
 * Simple java program to identify PII information in a given text file
 */
public class PIIIdentifier {
  public static void main(String[] args) {
    identifyPII("input.txt");
  }

  /**
   * identifyPII
   * @param fileName: Input file name
   */
  public static void identifyPII(String fileName) {
    try {
      List<String> lines = readTextFile(fileName);
      identifyPIIInformation(lines);
    } catch (Exception e) {
      System.out.println("Error: " + e.getMessage());
    }
  }

  /**
   *
   * @param fileName: Input file
   * @return List of PII data elements
   * @throws Exception
   */
  public static List<String> readTextFile(String fileName) throws Exception {
    List<String> lines = new ArrayList<>();
    BufferedReader reader = new BufferedReader(new FileReader(fileName));
    try {
      String line;
      while ((line = reader.readLine()) != null) {
        lines.add(line);
      }
    }
    finally {
      reader.close();
    }
    return lines;
  }

  /**
   *
   * @param lines: Lines in a file
   */
  public static void identifyPIIInformation(List<String> lines) {
    for (int i = 0; i < lines.size(); i++) {
      String line = lines.get(i);
      identifyPIIInformation(line, i + 1);
    }
  }

  /**
   *
   * @param line: line in a file
   * @param lineNumber: line number
   */
  public static void identifyPIIInformation(String line, int lineNumber) {
    final String[] regex = {
            "\\d{3}-\\d{2}-\\d{4}",                 // Social
            "\\d{3}\\d{2}\\d{4}",                 // Social
            "[\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}",  // mail
            "[2-9]\\d{2}-\\d{3}-\\d{4}"             // phone
    };

    for(String s : regex) {
      Pattern pattern = Pattern.compile(s);
      Matcher matcher = pattern.matcher(line);
      while (matcher.find()) {
        String pii = matcher.group();
        System.out.println("PII Information: " + pii + " (Line: " + lineNumber + ")");
      }
    }
  }
}