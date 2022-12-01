import { sumArray } from "./utils/array.ts";

Deno.readTextFile("./inputs/01.txt").then((data) => {
  const highest = data
    .split("\n\n")
    .map((group) =>
      sumArray(group.split("\n").map((calories) => parseInt(calories)))
    )
    .sort((a, b) => a - b)
    .slice(-3);
  console.log(highest[0]);
  console.log(sumArray(highest));
});
