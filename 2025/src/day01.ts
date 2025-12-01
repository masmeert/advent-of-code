import { Array as A, Effect, pipe } from "effect";
import { getAocInput } from "./utils/api";

function parseInput() {
	return getAocInput({ day: 1, year: 2025 }).pipe(
		Effect.map((input) =>
			input
				.trim()
				.split("\n")
				.map((line) => line.replace("R", "").replace("L", "-"))
				.map(Number),
		),
	);
}

function countOccurences(
	start: number,
	target: number,
	instructions: number[],
): number {
	return instructions.reduce(
		(acc, i) => {
			const pos = (acc.pos + i) % 100;
			return { pos, count: acc.count + (pos === target ? 1 : 0) };
		},
		{ pos: start, count: 0 },
	).count;
}

function countCrossings(
	start: number,
	target: number,
	instructions: number[],
): number {
	const _count = (instruction: number): number =>
		pipe(
			A.range(1, Math.abs(instruction)),
			A.filter((j) => (start + Math.sign(instruction) * j) % 100 === target),
			A.length,
		);

	return instructions.reduce(
		(acc, i) => ({
			pos: (acc.pos + i) % 100,
			count: acc.count + _count(i),
		}),
		{ pos: start, count: 0 },
	).count;
}

function main() {
	return Effect.gen(function* () {
		const instructions = yield* parseInput();
		yield* Effect.log(
			`Occurences of 0: ${countOccurences(50, 0, instructions)}`,
		);
		yield* Effect.log(`Passes over 0: ${countCrossings(50, 0, instructions)}`);
	});
}

Effect.runPromise(main());
