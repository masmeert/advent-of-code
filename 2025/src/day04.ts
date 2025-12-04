import { Array as A, Data, Effect, HashSet, Option, pipe } from "effect";
import { getAocInput } from "./utils/api";

const Coord = (row: number, col: number) => Data.tuple(row, col);
type Coord = ReturnType<typeof Coord>;
type Rolls = HashSet.HashSet<Coord>;

const NEIGHBORS = [
	[-1, -1],
	[-1, 0],
	[-1, 1],
	[0, -1],
	[0, 1],
	[1, -1],
	[1, 0],
	[1, 1],
] as const;

function parseRow(line: string, row: number): Coord[] {
	return A.filterMap(line.split(""), (char, col) =>
		char === "@" ? Option.some(Coord(row, col)) : Option.none(),
	);
}

function parseRolls(input: string): Rolls {
	return pipe(
		input.trim().split("\n"),
		A.flatMap(parseRow),
		HashSet.fromIterable,
	);
}

function parseInput() {
	return Effect.map(getAocInput({ day: 4, year: 2025 }), parseRolls);
}

function neighborCount(rolls: Rolls, row: number, col: number): number {
	return A.filter(NEIGHBORS, ([dr, dc]) =>
		HashSet.has(rolls, Coord(row + dr, col + dc)),
	).length;
}

function isAccessible(rolls: Rolls, coord: Coord): boolean {
	return neighborCount(rolls, coord[0], coord[1]) < 4;
}

function getAccessibleRolls(rolls: Rolls): Rolls {
	return HashSet.filter(rolls, (coord) => isAccessible(rolls, coord));
}

function removeAccessible(rolls: Rolls): Rolls {
	return HashSet.filter(rolls, (coord) => !isAccessible(rolls, coord));
}

function countTotalRemovable(rolls: Rolls, total = 0): number {
	const count = HashSet.size(getAccessibleRolls(rolls));
	return count === 0
		? total
		: countTotalRemovable(removeAccessible(rolls), total + count);
}

function main() {
	return Effect.gen(function* () {
		const rolls = yield* parseInput();
		yield* Effect.log(`Part 1: ${HashSet.size(getAccessibleRolls(rolls))}`);
		yield* Effect.log(`Part 2: ${countTotalRemovable(rolls)}`);
	});
}

Effect.runPromise(main()).catch(console.error);
