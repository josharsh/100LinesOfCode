import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URI;
import java.util.Scanner;

public class URLAnalyzer {
    public static void main(String[] args) throws IOException {

        System.out.println("Welcome");
        System.out.print("Enter URL: ");
        String url = new Scanner(System.in).nextLine();

        HttpURLConnection urlConnection = (HttpURLConnection) URI.create(url)
                .toURL().openConnection();

        System.out.println("\t\t *****Findings*****");
        System.out.println("URL: " + urlConnection.getURL());
        System.out.println("Response message: " + urlConnection.getResponseMessage());
        System.out.println("Response code: " + urlConnection.getResponseCode());
        System.out.println("Request method: " + urlConnection.getRequestMethod());
        System.out.println("Content type: " + urlConnection.getContentType());
        System.out.println("Content length: " + urlConnection.getContentLength());
        System.out.println("Read timeout: " + urlConnection.getReadTimeout());
        System.out.println("Using proxy? " + urlConnection.usingProxy());
        System.out.println("Allow user interaction? " + urlConnection.getAllowUserInteraction());
        System.out.println("Date: " + urlConnection.getDate());
        System.out.println("Do input? " + urlConnection.getDoInput());
        System.out.println("Do output? " + urlConnection.getDoOutput());
        System.out.println("Expiration: " + urlConnection.getExpiration());
        System.out.println("Modified since: " + urlConnection.getIfModifiedSince());
        System.out.println("Last modified: " + urlConnection.getLastModified());
        System.out.println("Connection timeout: " + urlConnection.getConnectTimeout());
        System.out.println("Uses caches? " + urlConnection.getUseCaches());
    }
}