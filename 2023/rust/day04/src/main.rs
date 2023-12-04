use std::{
    collections::{HashMap, HashSet},
    fs,
};

fn parse_nums_set(nums: &str) -> HashSet<u32> {
    nums.split_whitespace()
        .map(|n| n.parse::<u32>().unwrap())
        .collect::<HashSet<u32>>()
}

fn parse_card_id(card: &str) -> u32 {
    card.split_whitespace()
        .nth(1)
        .unwrap()
        .parse::<u32>()
        .unwrap()
}

fn process_lines<F>(file_content: &str, mut process_line: F)
where
    F: FnMut(&str, &HashSet<u32>, &HashSet<u32>),
{
    for line in file_content.split("\n") {
        if let Some((card, content)) = line.split_once(":") {
            if let Some((winning, hand)) = content.split_once("|") {
                let winning = parse_nums_set(winning);
                let hand = parse_nums_set(hand);
                process_line(card, &winning, &hand);
            }
        }
    }
}

fn part_one() -> u32 {
    let mut total: u32 = 0;
    let file_content =
        fs::read_to_string("input.txt").expect("Something went wrong reading the file");
    process_lines(&file_content, |_, winning, hand| {
        let intersection_len = winning.intersection(hand).count() as u32;

        // Part 1: total is factorial of intersection length
        if intersection_len > 0 {
            total += u32::pow(2, intersection_len - 1);
        }
    });
    total
}

fn part_two() -> u32 {
    let mut won: HashMap<u32, u32> = HashMap::new();
    let file_content =
        fs::read_to_string("input.txt").expect("Something went wrong reading the file");
    process_lines(&file_content, |card, winning, hand| {
        let card_id = parse_card_id(card);
        let intersection_len = winning.intersection(hand).count() as u32;

        // Part 2: for each won add n copies
        for n in (card_id + 1)..(card_id + 1 + intersection_len) {
            let mut copies = *won.get(&n).unwrap_or(&0);
            copies += 1;
            copies += *won.get(&card_id).unwrap_or(&0);
            won.insert(n, copies);
        }
    });
    won.values().sum::<u32>() + file_content.lines().count() as u32
}

fn main() {
    println!("Part one: {}", part_one());
    println!("Part two: {}", part_two());
}
