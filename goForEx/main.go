package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"
	"os"

	"github.com/joho/godotenv"
)

func main() {

	err := loadEnvVariables()
	if err != nil {
		fmt.Println("Error loading .env file:", err)
		return
	}

	// Add a new endpoint for the API call.
	http.HandleFunc("/forex", apiCallHandler)

	// Start the HTTP server on port 8080.
	if err := http.ListenAndServe(":8080", nil); err != nil {
		fmt.Println("Error:", err)
	}
}

func apiCallHandler(w http.ResponseWriter, r *http.Request) {

	baseCurrency := r.URL.Query().Get("base")

	// if baseCurrency == "" {
	// 	http.Error(w, "Missing Base Currency Parameter", http.StatusBadRequest)
	// 	return
	// }

	responseData, err := makeAPICall(baseCurrency)
	if err != nil {
		http.Error(w, "API call failed", http.StatusInternalServerError)
		return
	}
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	w.Write(responseData)

}

func makeAPICall(baseCurrency string) ([]byte, error) {

	apiKey := os.Getenv("API_KEY")
	if apiKey == "" {
		fmt.Println("API_KEY is not set.")
	} else {
		fmt.Printf("API_KEY: %s\n", apiKey)
	}

	baseURL := "http://api.exchangeratesapi.io/v1/latest"
	queryParams := url.Values{}
	queryParams.Add("access_key", apiKey)
	queryParams.Add("base", baseCurrency)

	urlParsed, err := url.Parse(baseURL)
	if err != nil {
		fmt.Println("Error:", err)
		return nil, err
	}
	urlParsed.RawQuery = queryParams.Encode()

	response, err := http.Get(urlParsed.String())
	if err != nil {
		return nil, err
	}
	defer response.Body.Close()

	responseData, err := ioutil.ReadAll(response.Body)
	if err != nil {
		return nil, err
	}

	return responseData, nil
}

func loadEnvVariables() error {
	err := godotenv.Load()
	if err != nil {
		return err
	}
	return nil
}
