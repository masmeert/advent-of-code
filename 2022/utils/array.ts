export function nums(array: string[]): number[] {
  return array.map((num) => parseInt(num));
}

export function sum(array: number[]): number {
  return array.reduce((partial, i) => partial + i, 0);
}

export function range(size: number, startAt = 0): number[] {
  return [...Array(size).keys()].map((i) => i + startAt);
}

export function isSubset<A>(a: A[], b: A[]): boolean {
  return b.every((x) => a.includes(x));
}
