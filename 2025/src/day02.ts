import { Array as A, Effect, Number as N, pipe } from "effect";
import { getAocInput } from "./utils/api";

type IdRange = { left: number; right: number };

function parseRange(s: string): IdRange {
	const [left = 0, right = 0] = s.split("-").map(Number);
	return { left, right };
}

function parseInput() {
	return getAocInput({ day: 2, year: 2025 }).pipe(
		Effect.map((input) => pipe(input.trim().split(","), A.map(parseRange))),
	);
}

function isRepeatedPattern(str: string, patternLen: number): boolean {
	const pattern = str.slice(0, patternLen);
	const repetitions = str.length / patternLen;
	return pattern[0] !== "0" && str === pattern.repeat(repetitions);
}

function isRepeatingSequence(
	times: (n: number) => boolean,
): (id: number) => boolean {
	return (id: number): boolean => {
		const str = id.toString();
		const len = str.length;

		return pipe(
			A.range(1, len - 1),
			A.filter((patternLen) => len % patternLen === 0),
			A.filter((patternLen) => times(len / patternLen)),
			A.some((patternLen) => isRepeatedPattern(str, patternLen)),
		);
	};
}

function sumInvalidIds(
	ranges: IdRange[],
	predicate: (id: number) => boolean,
): number {
	return pipe(
		ranges,
		A.flatMap(({ left, right }) => A.range(left, right)),
		A.filter(predicate),
		N.sumAll,
	);
}

function main() {
	return Effect.gen(function* () {
		const ranges = yield* parseInput();

		yield* Effect.log(
			sumInvalidIds(
				ranges,
				isRepeatingSequence((n) => n === 2),
			),
		);
		yield* Effect.log(
			sumInvalidIds(
				ranges,
				isRepeatingSequence((n) => n >= 2),
			),
		);
	});
}

Effect.runPromise(main());
