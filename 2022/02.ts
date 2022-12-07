function play(guide: string[], scores: Map<string, number[]>): number[] {
  let score = 0;
  let scoreP2 = 0;
  for (const line of guide) {
    score += scores.get(line)![0];
    scoreP2 += scores.get(line)![1];
  }
  return [score, scoreP2];
}

const data = await Deno.readTextFile("./inputs/02.txt").then((data) => {
  return data.split("\n");
});
const scores = new Map<string, number[]>([
  ["A X", [4, 3]],
  ["A Y", [8, 4]],
  ["A Z", [3, 8]],
  ["B X", [1, 1]],
  ["B Y", [5, 5]],
  ["B Z", [9, 9]],
  ["C X", [7, 2]],
  ["C Y", [2, 6]],
  ["C Z", [6, 7]],
]);

const results = play(data, scores);
console.log(results[0]);
console.log(results[1]);
