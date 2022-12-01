import { sumArray } from "./utils/array.ts";

const results = await Deno.readTextFile("./inputs/01.txt");
const data: number[] = [];
for (const group of results.split("\n\n")) {
  data.push(sumArray(group.split("\n").map((calories) => parseInt(calories))));
}

function getNHighest(n: number) {
  return data.sort((a, b) => a - b).slice(-n);
}

console.log(getNHighest(1)[0]);
console.log(sumArray(getNHighest(3)));
