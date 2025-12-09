import { Array as A, Option as O, pipe } from "effect";

export const transpose = <T>(matrix: T[][]): T[][] =>
	pipe(
		A.range(0, (matrix[0]?.length ?? 0) - 1),
		A.map((i) => A.filterMap(matrix, (row) => O.fromNullable(row[i]))),
	);

export function combinations(n: 1): <T>(items: T[]) => [T][];
export function combinations(n: 2): <T>(items: T[]) => [T, T][];
export function combinations(n: number): <T>(items: T[]) => T[][];
export function combinations(n: number) {
	return <T>(items: T[]): T[][] => {
		if (n === 0) return [[]];
		if (items.length < n) return [];
		if (items.length === n) return [items];

		return pipe(
			items,
			A.matchLeft({
				onEmpty: () => [] as T[][],
				onNonEmpty: (first, rest) => {
					const includingFirst = pipe(
						combinations(n - 1)(rest),
						A.map((combo) => [first, ...combo]),
					);
					const excludingFirst = combinations(n)(rest);
					return [...includingFirst, ...excludingFirst];
				},
			}),
		);
	};
}
