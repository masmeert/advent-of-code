import { sum } from "./utils/array.ts";
import { ALPHABET } from "./utils/string.ts";

function part1(rucksacks: string[]) {
  const letters = [];
  for (const rucksack of rucksacks) {
    const a = rucksack.slice(0, rucksack.length / 2);
    const b = rucksack.slice(rucksack.length / 2);
    const common = new Set([...new Set(a)].filter((x) => b.includes(x)));
    const [letter] = common;
    letters.push(letter);
  }
  return letters;
}

function part2(rucksacks: string[]) {
  const letters = [];
  for (let x = 0; x < rucksacks.length; x += 3) {
    const [a, b, c] = rucksacks.slice(x, x + 3);
    const common = new Set(
      [...new Set(a)].filter((x) => b.includes(x) && c.includes(x))
    );
    const [letter] = common;
    letters.push(letter);
  }
  return letters;
}

function getLetterIndex(letter: string) {
  return ALPHABET.indexOf(letter) + 1;
}

const data = await Deno.readTextFile("./inputs/03.txt").then((data) => {
  return data.split("\n");
});

console.log(sum(part1(data).map((letter) => getLetterIndex(letter))));
console.log(sum(part2(data).map((letter) => getLetterIndex(letter))));
