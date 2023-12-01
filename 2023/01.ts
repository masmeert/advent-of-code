const DIGITS_TABLE: { [key: string]: string } = {
  on: "1",
  tw: "2",
  thre: "3",
  four: "4",
  fiv: "5",
  six: "6",
  seve: "7",
  eigh: "8",
  nin: "9",
};

function recoverCalibrationValue(calibration: string): number {
  const digits = calibration.match(/\d/g);
  if (!digits) throw new Error("No digits found");

  return parseInt(digits[0] + digits[digits.length - 1]);
}

function recoverCalibrationValue2(calibration: string): number {
  const digits = calibration
    .match(
      /(?:\d|on(?=e)|tw(?=o)|thre(?=e)|four|fiv(?=e)|six|seve(?=n)|eigh(?=t)|nin(?=e))/g
    )
    ?.map((digit) => DIGITS_TABLE[digit] || digit);
  if (!digits) throw new Error("No digits found");

  return parseInt(digits[0] + digits[digits.length - 1]);
}

const input = Deno.readTextFileSync("./inputs/01.txt").split("\n");
const part1 = input.reduce((acc, i) => acc + recoverCalibrationValue(i), 0);
const part2 = input.reduce((acc, i) => acc + recoverCalibrationValue2(i), 0);

console.log(`Part 1: ${part1}\nPart 2: ${part2}\n`);
