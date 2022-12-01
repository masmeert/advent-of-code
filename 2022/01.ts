import { sum, nums } from "./utils/array.ts";

const highest = await Deno.readTextFile("./inputs/01.txt").then((data) => {
  return data
    .split("\n\n")
    .map((group) => sum(nums(group.split("\n"))))
    .sort((a, b) => a - b);
});

console.log(highest[highest.length - 1]);
console.log(sum(highest.slice(-3)));
