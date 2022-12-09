const TREES = (await Deno.readTextFile("./inputs/08.txt"))
  .split("\n")
  .map((row) => row.split("").map((t) => Number(t)));

const SIZE = TREES.length;
let VISIBLE = 4 * SIZE - 4;
let SCENIC = 0;

const getHorizontalVision = (
  tree: number,
  x: number,
  start: number,
  end: number,
) => {
  for (let i = start; i < end; i++) {
    if (TREES[x][i] >= tree) return false;
  }
  return true;
};

const getVerticalVision = (
  tree: number,
  y: number,
  start: number,
  end: number,
) => {
  for (let i = start; i < end; i++) {
    if (TREES[i][y] >= tree) return false;
  }
  return true;
};

const getScenicScore = (x: number, y: number) => {
  const score = [0, 0, 0, 0];
  for (let i = x - 1; i >= 0; i--) {
    if (TREES[i][y] >= TREES[x][y]) {
      score[0]++;
      break;
    } else {
      score[0]++;
    }
  }
  for (let i = y - 1; i >= 0; i--) {
    if (TREES[x][i] >= TREES[x][y]) {
      score[1]++;
      break;
    } else {
      score[1]++;
    }
  }
  for (let i = y + 1; i < SIZE; i++) {
    if (TREES[x][i] >= TREES[x][y]) {
      score[2]++;
      break;
    } else {
      score[2]++;
    }
  }
  for (let i = x + 1; i < SIZE; i++) {
    if (TREES[i][y] >= TREES[x][y]) {
      score[3]++;
      break;
    } else {
      score[3]++;
    }
  }
  return score.filter(Boolean).reduce((a, b) => a * b, 1);
};

for (let x = 1; x < SIZE - 1; x++) {
  for (let y = 1; y < SIZE - 1; y++) {
    if (
      getHorizontalVision(TREES[x][y], x, 0, y) ||
      getHorizontalVision(TREES[x][y], x, y + 1, SIZE) ||
      getVerticalVision(TREES[x][y], y, 0, x) ||
      getVerticalVision(TREES[x][y], y, x + 1, SIZE)
    ) {
      VISIBLE++;
    }
  }
}

for (let x = 0; x < SIZE; x++) {
  for (let y = 0; y < SIZE; y++) {
    const score = getScenicScore(x, y);
    if (score > SCENIC) {
      SCENIC = score;
    }
  }
}

console.log(VISIBLE);
console.log(SCENIC);
