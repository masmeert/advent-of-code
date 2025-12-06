import { Array as A, Option as O, pipe } from "effect";

export const transpose = <T>(matrix: T[][]): T[][] =>
	pipe(
		A.range(0, (matrix[0]?.length ?? 0) - 1),
		A.map((i) => A.filterMap(matrix, (row) => O.fromNullable(row[i]))),
	);
