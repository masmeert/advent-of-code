import { Array as A, Effect, Number as N, pipe, String as S } from "effect";
import { getAocInput } from "./utils/api";

type Box = [number, number, number];
type Circuit = Set<string>;
type Circuits = Set<Circuit>;

const parseBox = (line: string): Box => line.split(",").map(Number) as Box;

const fetchInput = getAocInput({ day: 8, year: 2025 }).pipe(
	Effect.map(S.trim),
	Effect.map(S.split("\n")),
	Effect.map(A.map(parseBox)),
);

const key = (b: Box) => b.join();

const distance = (a: Box, b: Box) =>
	Math.hypot(b[0] - a[0], b[1] - a[1], b[2] - a[2]);

const sortedPairs = (boxes: Box[]) =>
	boxes
		.flatMap((a, i) => boxes.slice(i + 1).map((b) => [a, b] as const))
		.sort((p, q) => distance(...p) - distance(...q));

const getCircuits = (boxes: Box[]): Circuits =>
	new Set(boxes.map((b) => new Set([key(b)])));

const findCircuit = (circuits: Circuits, k: string) =>
	[...circuits].find((c) => c.has(k))!;

const merge = (circuits: Circuits, a: Box, b: Box): Circuits => {
	const cA = findCircuit(circuits, key(a));
	const cB = findCircuit(circuits, key(b));
	if (cA === cB) return circuits;
	return new Set([...circuits].filter((c) => c !== cA && c !== cB)).add(
		new Set([...cA, ...cB]),
	);
};

const part1 = (boxes: Box[]) =>
	pipe(
		sortedPairs(boxes).slice(0, 1000),
		A.reduce(getCircuits(boxes), (c, [a, b]) => merge(c, a, b)),
		(circuits) => [...circuits].map((c) => c.size).sort((a, b) => b - a),
		(sizes) => N.sumAll(sizes.slice(0, 3)),
	);

const part2 = (boxes: Box[]) => {
	const pairs = sortedPairs(boxes);

	type State = {
		circuits: Circuits;
		idx: number;
		lastPair: [Box, Box];
	};

	return Effect.iterate(
		{ circuits: getCircuits(boxes), idx: 0, lastPair: pairs[0] } as State,
		{
			while: (s) => s.circuits.size > 1,
			body: (s) => {
				const pair = pairs[s.idx];
				const next = merge(s.circuits, pair[0], pair[1]);
				const merged = next !== s.circuits;
				return Effect.succeed({
					circuits: next,
					idx: s.idx + 1,
					lastPair: merged ? pair : s.lastPair,
				});
			},
		},
	).pipe(Effect.map((s) => s.lastPair[0][0] * s.lastPair[1][0]));
};

const main = Effect.gen(function* () {
	const input = yield* fetchInput;
	yield* Effect.log(`Part 1: ${part1(input)}`);
	yield* Effect.log(`Part 2: ${part2(input)}`);
});

Effect.runPromise(main).catch(console.error);
