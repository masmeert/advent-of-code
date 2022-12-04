import { range } from "./utils/array.ts";

function part1(pairs: number[][][]): number {
  let overlaps = 0;
  for (const pair of pairs) {
    const [a, b] = pair[0];
    const [c, d] = pair[1];
    if ((a <= c && d <= b) || (c <= a && b <= d)) {
      overlaps++;
    }
  }
  return overlaps;
}

function part2(pairs: number[][][]): number {
  let overlaps = 0;
  for (const pair of pairs) {
    for (let x = pair[0][0]; x <= pair[0][1]; x++) {
      if (range(pair[1][1] - pair[1][0] + 1, pair[1][0]).includes(x)) {
        overlaps++;
        break;
      }
    }
  }
  return overlaps;
}

const data = await Deno.readTextFile("./inputs/04.txt").then((data) => {
  return data
    .split("\n")
    .map((line) => line.split(","))
    .map((pairs) =>
      pairs.map((pair) => pair.split("-").map((num) => parseInt(num)))
    );
});

console.log(part1(data));
console.log(part2(data));
