export function intersection<A>(a: Set<A>, ...sets: Set<A>[]): Set<A> {
  const intersect = (set1: Set<A>, set2: Set<A>): Set<A> =>
    new Set([...set1].filter((element) => set2.has(element)));

  return sets.reduce(intersect, a);
}
