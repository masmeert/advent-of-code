package main

import "fmt"

func Solve(in []string, right, down int) int {
	var x, y, t int
	for y < len(in) {
		if in[y][x%len(in[0])] == '#' {
			t += 1
		}
		x += right
		y += down
	}
	return t
}

func Prod(l []int) int {
	result := 1
	for _, x := range l {
		result *= x
	}
	return result
}

func main() {
	in := GetInput()
	fmt.Println(Solve(in, 3, 1))
	fmt.Println(Prod([]int{
		Solve(in, 1, 1),
		Solve(in, 3, 1),
		Solve(in, 5, 1),
		Solve(in, 7, 1),
		Solve(in, 1, 2),
	}))
}
