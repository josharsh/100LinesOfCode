package org.skdesign;

import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

import java.io.IOException;
import java.util.Currency;

/**
* Calls Currency data api using okhttp3 client and prints out response data
* */
public class Converter {

    public static void converter(Currency from, Currency to, Double amount) throws IOException, InterruptedException {
        OkHttpClient client = new OkHttpClient().newBuilder().build();
        String apiKey = "Placeholder for API key";  /**Get API Key from apilayer.com */
        Request request = new Request.Builder()   /**request to be made with api key using okhttp3 client */
                .url("https://api.apilayer.com/currency_data/convert?to=" + to + "&from=" + from + "&amount=" + amount)
                .addHeader("apikey", apiKey)
                .method("GET", null).build();
        Response response = client.newCall(request).execute();
        assert response.body() != null;
        System.out.println(response.body().string());       //Print the response
        response.body().close();

    }
}

