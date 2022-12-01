export function nums(array: string[]): number[] {
  return array.map((num) => parseInt(num));
}

export function sum(array: number[]): number {
  return array.reduce((partial, i) => partial + i, 0);
}
