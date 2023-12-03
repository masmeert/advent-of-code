import { sum } from "./utils/array.ts";

function isCharValid(char: string): boolean {
  return (char >= "0" && char <= "9") || char === ".";
}

function getAdj(y: number, x: number): [number, number][] {
  return [
    [y - 1, x - 1],
    [y - 1, x],
    [y - 1, x + 1],
    [y, x - 1],
    [y, x + 1],
    [y + 1, x - 1],
    [y + 1, x],
    [y + 1, x + 1],
  ];
}

function findNumber(
  schematic: string[],
  [y, x]: [number, number],
  back = true,
  forward = true
): string | undefined {
  const char = schematic[y][x];
  let seq = "";
  if (char >= "0" && char <= "9") {
    seq += char;
  } else {
    return undefined;
  }
  if (back) {
    const prev = findNumber(schematic, [y, x - 1], true, false);
    if (prev) {
      seq = prev + seq;
    }
  }
  if (forward) {
    const next = findNumber(schematic, [y, x + 1], false, true);
    if (next) {
      seq += next;
    }
  }
  return seq;
}

export function findMissingParts(schematic: string[]): number[] {
  const valids = [];
  for (let y = 0; y < schematic.length; y++) {
    const line = schematic[y];
    let seq = "";
    let isValid = false;
    for (let x = 0; x < line.length; x++) {
      const char = line[x];
      if (char >= "0" && char <= "9") {
        if (
          !getAdj(y, x)
            .map(([ay, ax]) => schematic.at(ay)?.at(ax))
            .every((a) => a === undefined || isCharValid(a))
        ) {
          isValid = true;
        }
        seq += char;
      } else {
        if (isValid && seq.length > 0) {
          valids.push(parseInt(seq));
        }
        seq = "";
        isValid = false;
      }
    }
    if (isValid && seq.length > 0) {
      valids.push(parseInt(seq));
    }
  }
  return valids;
}

export function findGears(schematic: string[]): number[] {
  return schematic.flatMap((line, y) =>
    line.split("").flatMap((char, x) => {
      if (char === "*") {
        const neighbours = getAdj(y, x)
          .map((a) => findNumber(schematic, a))
          .filter((n) => !!n)
          .map((n) => n!);

        const uniques = Array.from(new Set(neighbours), Number);
        if (uniques.length === 2) {
          return uniques[0] * uniques[1];
        }
      }
      return [];
    })
  );
}

const schematic = Deno.readTextFileSync("./inputs/03.txt").split("\n");
const part1 = sum(findMissingParts(schematic));
const part2 = sum(findGears(schematic));

console.log(`Part 1: ${part1}\nPart 2: ${part2}\n`);
