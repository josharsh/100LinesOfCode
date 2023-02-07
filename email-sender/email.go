package main

import (
	"bufio"
	"fmt"
	"log"
	"net/smtp"
	"os"
)

var emails = make([][]string,0)

func ReadFile(file string) [][]string {
	f, err := os.Open(file)

    if err != nil {
        log.Fatal(err)
    }

    defer f.Close()

    scanner := bufio.NewScanner(f)

    for scanner.Scan() {
		log.Println("Reading emails...")
		temp := make([]string, 0)
        temp = append(temp, scanner.Text())
        emails = append(emails, [][]string{temp}...)
    }

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }
	return emails
}

func main()  {

	to := ReadFile("./emails.txt")
	bufferReader := bufio.NewReader(os.Stdin)
	from := os.Getenv("FROM")
	passwd := os.Getenv("PASSWD")

  	// smtp server configuration.
	smtpHost := "smtp.gmail.com"

  	// Message.
  	fmt.Printf("Enter your message:\n")
  	msg, err  := bufferReader.ReadString('\n')
	if err != nil {
		log.Println(err.Error())
	}
  
	auth := smtp.PlainAuth("", from, passwd, smtpHost)

   	// Sending email.
	for i, array := range to{
		err := smtp.SendMail("smtp.gmail.com:587", auth, from, array, []byte(msg))
		if err != nil {
			log.Println(err.Error())
		}

		log.Printf("Sending to %v...\n",array[i])
		fmt.Println("Email Sent Successfully!")
    }   
}