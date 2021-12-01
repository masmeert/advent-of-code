package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func ReadInput() []int {
	var data []int
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatalln(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		x, err := strconv.Atoi((scanner.Text()))
		if err != nil {
			log.Fatalln(err)
		}
		data = append(data, x)
	}
	if err := scanner.Err(); err != nil {
		log.Fatalln(err)
	}
	return data
}

func PartOne() int {
	data := ReadInput()
	count := 0
	for x := 1; x < len(data); x++ {
		if data[x] > data[x-1] {
			count++
		}
	}
	return count
}

func PartTwo() int {
	data := ReadInput()
	count := 0
	for x := 3; x < len(data); x++ {
		if data[x] > data[x-3] {
			count++
		}
	}
	return count
}

func main() {
	fmt.Println(PartOne())
	fmt.Println(PartTwo())
}
