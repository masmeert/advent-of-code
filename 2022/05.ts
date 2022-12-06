function getStacks(): string[][] {
  return [
    ["Q", "F", "M", "R", "L", "W", "C", "V"],
    ["D", "Q", "L"],
    ["P", "S", "R", "G", "W", "C", "N", "B"],
    ["L", "C", "D", "H", "B", "Q", "G"],
    ["V", "G", "L", "F", "Z", "S"],
    ["D", "G", "N", "P"],
    ["D", "Z", "P", "V", "F", "C", "W"],
    ["C", "P", "D", "M", "S"],
    ["Z", "N", "W", "T", "V", "M", "P", "C"],
  ];
}

function getStackTop(stacks: string[][]) {
  let top = "";
  for (const stack of stacks) {
    top += stack[stack.length - 1];
  }
  return top;
}

function parseInstruction(line: string): number[] {
  return Array.from(line.matchAll(/[0-9]+/g), (m) => parseInt(m[0]));
}

function move(instructions: string[], stacks: string[][]): void {
  for (const line of instructions) {
    const [n, from, to] = parseInstruction(line);
    for (let i = 0; i < n; i++) {
      const crate = stacks[from - 1].pop();
      stacks[to - 1].push(crate!);
    }
  }
}

function move2(instructions: string[], stacks: string[][]): void {
  for (const line of instructions) {
    const [n, from, to] = parseInstruction(line);
    const remove = stacks[from - 1].splice(stacks[from - 1].length - n, n);
    stacks[to - 1] = stacks[to - 1].concat(remove);
  }
}

function part1(instructions: string[], stacks: string[][]): string {
  move(instructions, stacks);
  return getStackTop(stacks);
}

function part2(instructions: string[], stacks: string[][]): string {
  move2(instructions, stacks);
  return getStackTop(stacks);
}

const instructions = await Deno.readTextFile("./inputs/05.txt").then((data) => {
  return data.split("\n");
});

console.log(part1(instructions, getStacks()));
console.log(part2(instructions, getStacks()));
