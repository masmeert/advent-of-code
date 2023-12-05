use rayon::iter::{IntoParallelRefIterator, ParallelIterator};
use std::fs;

#[derive(Debug)]
struct Converter {
    destination: usize,
    source: usize,
    range_length: usize,
}

impl Converter {
    fn apply(&self, input: usize) -> Option<usize> {
        if input >= self.source && input < self.source + self.range_length {
            Some(self.destination + (input - self.source))
        } else {
            None
        }
    }
}

impl From<String> for Converter {
    fn from(input: String) -> Self {
        let parts = input
            .trim()
            .split_whitespace()
            .map(|s| s.parse::<usize>().unwrap())
            .collect::<Vec<usize>>();

        Self {
            destination: parts[0],
            source: parts[1],
            range_length: parts[2],
        }
    }
}

struct CategoryMapper {
    conversions: Vec<Converter>,
}

impl CategoryMapper {
    fn convert(&self, input: usize) -> usize {
        self.conversions
            .iter()
            .find_map(|t| t.apply(input))
            .unwrap_or_else(|| input)
    }
}

impl From<String> for CategoryMapper {
    fn from(input: String) -> Self {
        let lines = input.trim().lines().skip(1);
        Self {
            conversions: lines.map(|line| line.trim().to_string().into()).collect(),
        }
    }
}

fn parse_seeds(line: &str) -> Vec<usize> {
    line.trim()
        .split(": ")
        .nth(1)
        .unwrap()
        .split_whitespace()
        .map(|x| x.parse::<usize>().unwrap())
        .collect()
}

fn read_input() -> (Vec<usize>, Vec<CategoryMapper>) {
    let file = fs::read_to_string("input.txt").expect("Error reading input.txt");
    let input = file.trim().split("\n\n").collect::<Vec<&str>>();
    let seeds = parse_seeds(input[0]);
    let maps = input[1..]
        .iter()
        .map(|s| CategoryMapper::from(s.to_string()))
        .collect();

    (seeds, maps)
}

fn convert_seed(seed: usize, maps: &[CategoryMapper]) -> usize {
    let mut converted = seed;
    for map in maps {
        converted = map.convert(converted);
    }
    converted
}

fn part_one() -> Option<usize> {
    let (seeds, maps) = read_input();
    seeds
        .iter()
        .map(|&seed| convert_seed(seed, &maps))
        .min()
}

fn part_two() -> Option<usize> {
    let (seeds, maps) = read_input();
    seeds
        .chunks(2)
        .map(|chunk| (chunk[0]..chunk[0] + chunk[1]))
        .flatten()
        .collect::<Vec<usize>>()
        .par_iter()
        .map(|&seed| convert_seed(seed, &maps))
        .min()
}

fn main() {
    println!(
        "Part one: {}",
        part_one().expect("Failed to calculate part1")
    );
    println!(
        "Part two: {}",
        part_two().expect("Failed to calculate part2")
    );
}
