package main

import (
	"fmt"
	"strconv"
	"strings"
)

func Solve(part2 bool, in [][]string) int {
	sum := 0
	for _, x := range in {
		bounds := strings.Split(x[0], "-")
		p1, _ := strconv.Atoi(bounds[0])
		p2, _ := strconv.Atoi(bounds[1])
		if !part2 {
			c := strings.Count(x[2], x[1])
			if p1 <= c && c <= p2 {
				sum += 1
			}
		} else if (string(x[2][p1-1]) == x[1]) != (string(x[2][p2-1]) == x[1]) {
			sum += 1
		}

	}
	return sum
}

func main() {
	in := GetInput()
	fmt.Println(Solve(false, in))
	fmt.Println(Solve(true, in))
}
