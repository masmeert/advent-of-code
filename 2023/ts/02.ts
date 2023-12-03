import { mul, sum } from "./utils/array.ts";

type Game = {
  id: number;
  colors: number[][];
};

const COLORS = ["red", "green", "blue"];
const MAXIMA = [12, 13, 14];

function parseGame(game: string): Game {
  const match = game.match(/Game (?<id>\d+): (?<cubes>.*)/)!.groups!;
  const colors = match.cubes.split("; ").map((set) => {
    return set.split(", ").reduce(
      (acc, line) => {
        const [num, color] = line.split(" ");
        acc[COLORS.indexOf(color)] = parseInt(num);
        return acc;
      },
      [0, 0, 0]
    );
  });

  return {
    id: parseInt(match.id),
    colors,
  };
}

function isGamePossible(game: Game): boolean {
  return game.colors.every((set) => {
    return set.every((num, i) => num <= MAXIMA[i]);
  });
}

function findFewestCubesNeeded(game: Game): number[] {
  return game.colors.reduce(
    (acc, v) => acc.map((n, i) => Math.max(n, v[i])),
    [0, 0, 0]
  );
}

const input = Deno.readTextFileSync("./inputs/02.txt")
  .split("\n")
  .map(parseGame);
const part1 = sum(input.filter(isGamePossible).map((game) => game.id));
const part2 = sum(input.map(findFewestCubesNeeded).map(mul));

console.log(`Part 1: ${part1}\nPart 2: ${part2}\n`);
