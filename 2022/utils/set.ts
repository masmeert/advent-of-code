export function intersection<A>(a: Set<A>, ...b: Set<A>[]): Set<A> {
  const c = function (a: Set<A>, b: Set<A>) {
    b = new Set(b);
    return new Set([...a].filter((x) => b.has(x)));
  };
  return undefined === b[0] ? a : intersection(c(a, b[0]), ...b.slice(1));
}
