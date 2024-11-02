package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
)

func main() {
	file, err := os.Open("../input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	reader := bufio.NewReader(file)
	floor := 0
	position := 0
	first := 0

	for {
		position++
		char, _, err := reader.ReadRune()
		if err == io.EOF {
			break
		}
		if err != nil {
			log.Fatal(err)
		}

		switch char {
		case '(':
			floor++
		case ')':
			floor--
		}

		if floor == -1 && first == 0 {
			first = position
		}
	}

	fmt.Println("Santa ends at floor:", floor)
	fmt.Println("Santa enters basement at:", first)
}
