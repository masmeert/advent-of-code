import { sum } from "./utils/array.ts";

function createTree(lines) {
  const sizes = { "/": 0 };
  const paths = ["/"];
  for (let i = 1; i < lines.length; i++) {
    const [_, cmd, dir] = lines[i].split(" ");
    if (cmd === "ls") {
      for (i++; i < lines.length; i++) {
        const parts = lines[i].split(" ");
        if (parts[0] === "$") {
          i--;
          break;
        }
        if (parts[0] !== "dir") {
          for (const path of paths) {
            sizes[path] = (sizes[path] ?? 0) + +parts[0];
          }
        }
      }
    } else {
      if (dir === "..") {
        paths.pop();
      } else {
        paths.push(`${paths.at(-1)}${dir}/`);
      }
    }
  }
  return sizes;
}

function partOne(tree) {
  const sizes = Object.values(tree);
  return sum(sizes.filter((size) => size <= 100000));
}

function partTwo(tree) {
  const sizes = Object.values(tree);
  return Math.min(...sizes.filter((size) => size >= tree["/"] - 40000000));
}

const history = await Deno.readTextFile("./inputs/07.txt").then((data) => {
  return data.split("\n");
});
const sizeTree = createTree(history);
console.log(partOne(sizeTree));
console.log(partTwo(sizeTree));
