import { sum } from "./utils/array.ts";

export function isCharValid(char: string): boolean {
  return (char >= "0" && char <= "9") || char === ".";
}

export function getAdj(y: number, x: number): [number, number][] {
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
  const valids: number[] = [];
  const gears = [];

  for (let y = 0; y < schematic.length; y++) {
    for (let x = 0; x < schematic[y].length; x++) {
      if (schematic[y][x] === "*") {
        gears.push([y, x]);
      }
    }
  }

  for (const [y, x] of gears) {
    const ns = [
      ...new Set(
        getAdj(y, x)
          .map((a) => findNumber(schematic, a))
          .filter((n) => !!n)
          .map((n) => n!)
      ),
    ].map(Number);
    if (ns.length === 2) {
      valids.push(ns[0] * ns[1]);
    }
  }
  return valids;
}

const schematic = Deno.readTextFileSync("./inputs/03.txt").split("\n");
const part1 = sum(findMissingParts(schematic));
const part2 = sum(findGears(schematic));

console.log(`Part 1: ${part1}\nPart 2: ${part2}\n`);
