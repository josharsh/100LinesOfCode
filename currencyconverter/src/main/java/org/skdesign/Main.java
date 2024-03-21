package org.skdesign;

import java.io.IOException;
import java.util.Currency;
import java.util.Scanner;

/**
 * This program is for converting USD to other currencies based on prevalent exchange rates. It uses Currency Data
 * API to convert currency and return the result. This is a free API which allows 100 calls per day. It uses okhttp3
 * library to call the url. Use  implementation("com.squareup.okhttp3:okhttp:3.14.6") in build.gradle.
 */
public class Main {
    public static void main(String[] args) throws IOException, InterruptedException {
        convert();  // call convert method from main method
    }

    public static void convert() throws IOException, InterruptedException {
        Currency from = Currency.getInstance("USD");    //Base currency
        Currency to = Currency.getInstance("USD"); //Currency to be converted to
        double amount = 0d;
        System.out.println("Welcome to Currency Converter");
        System.out.println("Enter three letter currency code to be converted from USD");
        Scanner scanner = new Scanner(System.in);
        try {
            to = Currency.getInstance(scanner.nextLine().toUpperCase());
        } catch (Exception e) {
            convert();
        }
        System.out.println("Enter amount");
        try {
            amount = scanner.nextDouble();
        } catch (Exception e) {
            System.out.println("Enter amount in digits");   //Error due to wrong number format
            convert();    //restart method
        }
        Converter.converter(from, to, amount); //Call Converter class
        scanner.close();
    }
}