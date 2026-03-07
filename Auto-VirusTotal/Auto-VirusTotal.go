package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
)

type VTResponse struct {
	Data struct {
		Attributes struct {
			LastAnalysisStats struct {
				Malicious  int `json:"malicious"`
				Harmless   int `json:"harmless"`
				Suspicious int `json:"suspicious"`
				Undetected int `json:"undetected"`
			} `json:"last_analysis_stats"`
		} `json:"attributes"`
	} `json:"data"`
}

func checkHash(hash string, apikey string) {
	url := "https://www.virustotal.com/api/v3/files/" + hash
	req, _ := http.NewRequest("GET", url, nil)
	req.Header.Set("x-apikey", apikey)

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	defer resp.Body.Close()

	var result VTResponse
	err = json.NewDecoder(resp.Body).Decode(&result)

	stats := result.Data.Attributes.LastAnalysisStats
	fmt.Printf("Malicious: %d\nHarmless: %d\nSuspicious: %d\nUndetected: %d\n",
		stats.Malicious, stats.Harmless, stats.Suspicious, stats.Undetected)

}

func main() {
	if len(os.Args) < 3 {
		fmt.Println("Usage: go run AutoVirusTotal.go <hashes_file> <apikey>")
		return
	}

	file, _ := os.Open(os.Args[1])
	defer file.Close()

	apiKey := os.Args[2]
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		hash := scanner.Text()
		checkHash(hash, apiKey)
	}
}
