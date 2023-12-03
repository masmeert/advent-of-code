use std::fs;

fn solve(is_part2: bool) -> u32 {
    fs::read_to_string("input.txt")
        .expect("Something went wrong reading the file")
        .split("\n")
        .map(|line| {
            if is_part2 {
                line.to_string()
                    .replace("one", "one1one")
                    .replace("two", "two2two")
                    .replace("three", "three3three")
                    .replace("four", "four4four")
                    .replace("five", "five5five")
                    .replace("six", "six6six")
                    .replace("seven", "seven7seven")
                    .replace("eight", "eight8eight")
                    .replace("nine", "nine9nine")
            } else {
                line.to_string()
            }
        })
        .map(|line| {
            line.chars()
                .filter_map(|char| char.to_digit(10))
                .collect::<Vec<u32>>()
        })
        .map(|digits| 10 * digits.first().unwrap() + digits.last().unwrap())
        .sum()
}

fn main() {
    println!("Part 1: {}", solve(false));
    println!("Part 2: {}", solve(true));
}
