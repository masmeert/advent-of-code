package main

import (
	"fmt"
	"strings"
)

type InputMap = []map[string]string

func GetInputMap(input [][]string) (ret InputMap) {
	for _, l := range input {
		hashmap := map[string]string{}
		for _, s := range l {
			v := strings.Split(s, ":")
			if v[0] != "cid" {
				hashmap[v[0]] = v[1]
			}
		}
		ret = append(ret, hashmap)
	}
	return ret
}

func GetKeys(m map[string]string) (keys []string) {
	for _, k := range m {
		keys = append(keys, k)
	}
	return keys
}

func PartOne(inMap InputMap) (sum int) {
	for _, m := range inMap {
		if len(GetKeys(m)) == 7 {
			sum += 1
		}
	}
	return sum
}

func main() {
	inMap := GetInputMap(GetInput())
	fmt.Println(PartOne(inMap))
}
