use std::{fs, str::FromStr};

#[derive(Debug)]
struct Game {
    id: u32,
    sets: Vec<[u32; 3]>,
}

impl FromStr for Game {
    type Err = &'static str;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let (id, sets) = s.split_once(":").unwrap();
        Ok(Self {
            id: id.split_once(' ').unwrap().1.parse().unwrap(),
            sets: sets
                .split("; ")
                .map(|set| {
                    let mut set_rgb = [0; 3];
                    for (count, color) in set
                        .split(",")
                        .map(|set| set.trim().split_once(" ").unwrap())
                    {
                        set_rgb[color.as_bytes()[0] as usize % 3] = count.parse().unwrap();
                    }
                    set_rgb
                })
                .collect(),
        })
    }
}

fn part_one(path: &str) -> u32 {
    fs::read_to_string(path)
        .expect("Something went wrong reading the file")
        .split("\n")
        .map(|line| Game::from_str(line).unwrap())
        .filter(|game| {
            game.sets
                .iter()
                .all(|rgb| rgb[0] <= 12 && rgb[1] <= 13 && rgb[2] <= 14)
        })
        .map(|game| game.id)
        .sum()
}

fn part_two(path: &str) -> u32 {
    fs::read_to_string(path)
        .expect("Something went wrong reading the file")
        .split("\n")
        .map(|line| Game::from_str(line).unwrap())
        .map(|game| {
            (0..3)
                .map(|index| game.sets.iter().map(|rgb| rgb[index]).max().unwrap())
                .product::<u32>()

        })
        .sum()
}

fn main() {
    println!("Part one: {}", part_one("input.txt"));
    println!("Part two: {}", part_two("input.txt"));
}
