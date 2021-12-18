package main

import "fmt"

func PartOne(input []int) int {
	set := make(map[int]bool)
	for _, n := range input {
		if set[2020-n] {
			return n * (2020 - n)
		}
		set[n] = true
	}
	return -1
}

func PartTwo(input []int) int {
	for i := 0; i < len(input); i++ {
		for j := i; j < len(input); j++ {
			for k := j; k < len(input); k++ {
				if input[i]+input[j]+input[k] == 2020 {
					return input[i] * input[j] * input[k]
				}
			}
		}
	}
	return -1
}

func main() {
	in := ReadInput()
	fmt.Println(PartOne(in))
	fmt.Println(PartTwo(in))
}
