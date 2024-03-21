package main

/**
 * Made by @glaukiol1
 * https://github.com/glaukiol1
 * glaukiol1@gmail.com
 */

/*
 * Password generator tool in the command line, very simple.
 * Using Google Go
 */
import (
	"fmt"
	"math/rand"
	"strings"
	"time"
)

func main() {
	var symbols string = "!@#$%^&*()_+{}|:\"<>?"
	var numbers string = "1234567890"
	var lower_letters string = "abcdefghijklmnopqrstuvwxyz"
	var upper_letters string = strings.ToUpper(lower_letters)

	char1 := string([]rune(symbols)[rand_(0, len(symbols))])
	char2 := string([]rune(symbols)[rand_(0, len(symbols))])
	char3 := string([]rune(symbols)[rand_(0, len(symbols))])
	char4 := string([]rune(symbols)[rand_(0, len(symbols))])

	num1 := string([]rune(numbers)[rand_(0, len(numbers))])
	num2 := string([]rune(numbers)[rand_(0, len(numbers))])
	num3 := string([]rune(numbers)[rand_(0, len(numbers))])
	num4 := string([]rune(numbers)[rand_(0, len(numbers))])
	num5 := string([]rune(numbers)[rand_(0, len(numbers))])

	ll1 := string([]rune(lower_letters)[rand_(0, len(lower_letters))])
	ll2 := string([]rune(lower_letters)[rand_(0, len(lower_letters))])
	ll3 := string([]rune(lower_letters)[rand_(0, len(lower_letters))])
	ll4 := string([]rune(lower_letters)[rand_(0, len(lower_letters))])
	ll5 := string([]rune(lower_letters)[rand_(0, len(lower_letters))])
	ll6 := string([]rune(lower_letters)[rand_(0, len(lower_letters))])

	ul1 := string([]rune(upper_letters)[rand_(0, len(upper_letters))])
	ul2 := string([]rune(upper_letters)[rand_(0, len(upper_letters))])
	ul3 := string([]rune(upper_letters)[rand_(0, len(upper_letters))])
	ul4 := string([]rune(upper_letters)[rand_(0, len(upper_letters))])

	fmt.Println(
		"Your password is: " + ll1 + char1 + ll2 + ll3 + ul1 + fmt.Sprint(num1) + fmt.Sprint(num2) + char2 + char3 + ul2 + ul3 + ll4 + ll5 + fmt.Sprint(num3) + fmt.Sprint(num4) + fmt.Sprint(num5) + char4 + ul4 + ll6)
}

func rand_(min, max int) int {
	rand.Seed(time.Now().UnixNano())
	return rand.Intn(max-1-min+1) + min
}
