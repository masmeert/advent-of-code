export function sum(array: number[]): number {
  return array.reduce((partial, i) => partial + i, 0);
}

export function mul(array: number[]): number {
  return array.reduce((partial, i) => partial * i, 1);
}

export function range(size: number, startAt = 0): number[] {
  return [...Array(size).keys()].map((i) => i + startAt);
}

export function isSubset<T>(a: T[], b: T[]): boolean {
  return b.every(a.includes);
}

export function transpose<T>(array: T[][]): T[][] {
  return [...Array(array[0].length)].map((_, i) => array.map((row) => row[i]));
}

export function combinations<T>(array: T[], n: number): T[][] {
  const result: T[][] = [];

  function generateCombinations(
    startIndex: number,
    currentCombination: T[]
  ): void {
    if (currentCombination.length === n) {
      result.push([...currentCombination]);
      return;
    }
    for (let i = startIndex; i < array.length; i++) {
      currentCombination.push(array[i]);
      generateCombinations(i + 1, currentCombination);
      currentCombination.pop();
    }
  }
  generateCombinations(0, []);
  return result;
}
