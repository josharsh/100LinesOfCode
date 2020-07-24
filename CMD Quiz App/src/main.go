package main

import (
	"encoding/csv"
	"flag"
	"fmt"
	"os"
	"strings"
	"time"
)

type problem struct {
	question   string
	answer     string
	userAnswer string
	isCorrect  bool
}

func main() {
	csvFileName := flag.String("csv", "problems.csv", "A csv file of format 'question,answer'")
	timeLimit := flag.Int("limit", 30, "The time limit of quiz in seconds")
	flag.Parse()

	file, err := os.Open(*csvFileName)
	if err != nil {
		exit(fmt.Sprintf("Could not open file %s\n", *csvFileName))
	}
	r := csv.NewReader(file)
	lines, err := r.ReadAll()
	if err != nil {
		exit("Failed to parse the CSV file")
	}
	problems := parseLines(lines)

	timer := time.NewTimer(time.Duration((*timeLimit)) * time.Second)
	start := time.Now()

	correctCount := 0
problemloop:
	for i := 0; i < len(problems); i++ {
		fmt.Printf("Problem #%d: %s = ", i+1, problems[i].question)
		ansChan := make(chan string)
		go func() {
			var answer string
			fmt.Scanf("%s\n", &answer)
			problems[i].userAnswer = answer
			ansChan <- answer
		}()

		select {
		case <-timer.C:
			fmt.Println()
			break problemloop
		case answer := <-ansChan:
			if answer == problems[i].answer {
				problems[i].isCorrect = true
				correctCount++
			}
		}
	}
	timer.Stop()
	for i, prob := range problems {
		check := "\u274C"
		if prob.isCorrect {
			check = "\u2705"
		}
		fmt.Printf("Problem #%d: %s = %s %s %s\n", i+1, prob.question, prob.userAnswer, string(check), prob.answer)
	}

	fmt.Printf("You scored %d out of %d in time %f seconds.\n", correctCount, len(problems), time.Since(start).Seconds())
}

func parseLines(lines [][]string) []problem {
	ret := make([]problem, len(lines))
	for i, line := range lines {
		ret[i] = problem{
			question: line[0],
			answer:   strings.TrimSpace(line[1]),
		}
	}
	return ret
}

func exit(msg string) {
	fmt.Println(msg)
	os.Exit(1)
}
