package main

import (
	"fmt"
	"regexp"
	"strconv"
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
	for k := range m {
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

func CheckHgt(hgt string) bool {
	if len(hgt) < 2 {
		return false
	}
	suffix := hgt[len(hgt)-2:]
	val, err := strconv.Atoi(hgt[:len(hgt)-2])
	if err != nil {
		return false
	}
	switch suffix {
	case "cm":
		if val < 150 || val > 193 {
			return false
		}
	case "in":
		if val < 59 || val > 76 {
			return false
		}
	default:
		return false
	}
	return true
}

func CheckFields(b ...bool) bool {
	for _, c := range b {
		if c {
			return true
		}
	}
	return false
}

func PartTwo(inMap InputMap) (sum int) {
	for _, m := range inMap {
		if !CheckFields(
			m["byr"] > "2002" || m["byr"] < "1920" || len(m["byr"]) != 4,
			m["iyr"] > "2020" || m["iyr"] < "2010" || len(m["iyr"]) != 4,
			m["eyr"] > "2030" || m["eyr"] < "2020" || len(m["eyr"]) != 4,
			!CheckHgt(m["hgt"]),
			!regexp.MustCompile("^#[0-9a-f]{6}$").Match([]byte(m["hcl"])),
			!regexp.MustCompile("^(amb|blu|brn|gry|grn|hzl|oth)$").Match([]byte(m["ecl"])),
			!regexp.MustCompile("^[0-9]{9}$").Match([]byte(m["pid"])),
		) {
			sum += 1
		}
	}
	return sum
}

func main() {
	inMap := GetInputMap(GetInput())
	fmt.Println(PartOne(inMap))
	fmt.Println(PartTwo(inMap))
}
