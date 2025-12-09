import { Array as A, Effect, Option, pipe } from "effect";
import { getAocInput } from "./utils/api";
import { combinations } from "./utils/array";

type Point = [number, number];
type Rect = [Point, Point]; // [[minX, minY], [maxX, maxY]]

const fetchInput = getAocInput({ day: 9, year: 2025 }).pipe(
	Effect.map((input) =>
		input
			.trim()
			.split("\n")
			.map((line) => line.split(",").map(Number) as Point),
	),
);

const gridArea = ([[x1, y1], [x2, y2]]: Rect): number =>
	(x2 - x1 + 1) * (y2 - y1 + 1);

const findMaxArea = (points: Point[]): number =>
	pipe(points, combinations(2), A.map(gridArea), A.reduce(0, Math.max));

const normalize = ([[x1, y1], [x2, y2]]: [Point, Point]): Rect => [
	[Math.min(x1, x2), Math.min(y1, y2)],
	[Math.max(x1, x2), Math.max(y1, y2)],
];

const adjacentPairs = <T>(items: T[]): [T, T][] =>
	pipe(
		items,
		A.filterMap((item, i) =>
			pipe(
				A.get(items, (i + 1) % items.length),
				Option.map((next) => [item, next] as [T, T]),
			),
		),
	);

const doesSegmentCrossesRect = (
	[[p, q], [r, s]]: Rect,
	[[x, y], [u, v]]: Rect,
): boolean => p < u && q < v && r > x && s > y;

const getGreenSegments = (redTiles: Point[]): Rect[] =>
	pipe(redTiles, adjacentPairs, A.map(normalize));

const findMaxValidArea = (redTiles: Point[]): number => {
	const greenSegments = getGreenSegments(redTiles);

	const isValidRect = (rect: Rect): boolean =>
		!A.some(greenSegments, (seg) => doesSegmentCrossesRect(seg, rect));

	return pipe(
		redTiles,
		combinations(2),
		A.map(normalize),
		A.filter(isValidRect),
		A.map(gridArea),
		A.reduce(0, Math.max),
	);
};

const main = Effect.gen(function* () {
	const input = yield* fetchInput;
	yield* Effect.log(`Part 1: ${findMaxArea(input)}`);
	yield* Effect.log(`Part 2: ${findMaxValidArea(input)}`);
});

Effect.runPromise(main).catch(console.error);
