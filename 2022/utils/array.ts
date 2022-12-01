export function sumArray(array: number[]) {
  return array.reduce((partial, i) => partial + i, 0);
}
