package main

import (
	"crypto/sha1"
	"encoding/hex"
	"encoding/json"
	"io/ioutil"
	"log"
	"net/http"
	"strings"

	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-lambda-go/lambda"
)

type pwdRequest struct {
	Password string `json:"password"`
}

type pwdResponse struct {
	Password    string `json:"password"`
	Occurrences string `json:"occurrences"`
	Sha1        string `json:"sha1"`
}

func router(req events.APIGatewayProxyRequest) (events.APIGatewayProxyResponse, error) {
	log.Printf("req-method: %s", req.HTTPMethod)
	if req.Path == "/check-password" {
		if req.HTTPMethod == "POST" {
			return checkPasswordHandler(req)
		}
	}
	return events.APIGatewayProxyResponse{
		StatusCode: http.StatusMethodNotAllowed,
		Body:       http.StatusText(http.StatusMethodNotAllowed),
	}, nil
}

func checkPasswordHandler(req events.APIGatewayProxyRequest) (events.APIGatewayProxyResponse, error) {
	var request pwdRequest
	err := json.Unmarshal([]byte(req.Body), &request)
	if err != nil {
		return events.APIGatewayProxyResponse{
			StatusCode: http.StatusInternalServerError,
			Body:       http.StatusText(http.StatusInternalServerError),
		}, nil
	}
	response, err := json.Marshal(checkPasswordService(request))
	if err != nil {
		return events.APIGatewayProxyResponse{
			StatusCode: http.StatusInternalServerError,
			Body:       http.StatusText(http.StatusInternalServerError),
		}, nil
	}
	return events.APIGatewayProxyResponse{
		StatusCode: http.StatusOK,
		Body:       string(response),
	}, nil
}

func checkPasswordService(request pwdRequest) pwdResponse {
	var api string = "https://api.pwnedpasswords.com/range/"
	pwd := request.Password
	hash := sha1.New()
	hash.Write([]byte(pwd))
	result := strings.ToUpper(hex.EncodeToString(hash.Sum(nil)))
	response, err := http.Get(api + result[0:5])
	if err != nil {
		log.Fatalln(err)
	}
	defer response.Body.Close()
	orig := result
	result = result[5:len(result)]
	contents, err := ioutil.ReadAll(response.Body)
	if err != nil {
		log.Fatalln(err)
	}
	passwords := strings.Split(string(contents), "\n")
	pwdMap := make(map[string]string)
	var currentSplit []string
	for i := 0; i < len(passwords); i++ {
		currentSplit = strings.Split(passwords[i], ":")
		pwdMap[currentSplit[0]] = currentSplit[1][0 : len(currentSplit[1])-1]
	}
	checkPwd := pwdMap[result]
	var httpResponse pwdResponse
	if pwdMap[result] != "" {
		httpResponse.Password = pwd
		httpResponse.Occurrences = checkPwd
		httpResponse.Sha1 = orig
	}
	return httpResponse
}
func main() {
	lambda.Start(router)
}
