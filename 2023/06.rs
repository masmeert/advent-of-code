struct Race {
    time: u64,
    distance: u64,
}

impl Race {
    fn find_better_runs(&self) -> u32 {
        let mut wins = 0;
        for t in 1..self.time {
            if (self.time - t) * t > self.distance {
                wins += 1;
            }
        }
        wins
    }
}

fn part_one() -> u32 {
    vec![
        Race {
            time: 44,
            distance: 283,
        },
        Race {
            time: 70,
            distance: 1134,
        },
        Race {
            time: 70,
            distance: 1134,
        },
        Race {
            time: 80,
            distance: 1491,
        },
    ]
    .iter()
    .map(|r| r.find_better_runs())
    .product()
}

fn part_two() -> u32 {
    Race {
        time: 44707080,
        distance: 283113411341491,
    }
    .find_better_runs()
}

fn main() {
    println!("Part One: {}", part_one());
    println!("Part Two: {}", part_two());
}
