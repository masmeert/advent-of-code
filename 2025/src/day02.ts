import { Array as A, Effect, Number as N, pipe } from "effect";
import { getAocInput } from "./utils/api";

type IdRange = { left: number; right: number };

function parseRange(s: string): IdRange {
	const [left = 0, right = 0] = s.split("-").map(Number);
	return { left, right };
}

function buildRange(range: IdRange): number[] {
	return A.range(range.left, range.right);
}

function parseInput() {
	return getAocInput({ day: 2, year: 2025 }).pipe(
		Effect.map((input) => pipe(input.trim().split(","), A.map(parseRange))),
	);
}

function isExactlyTwice(id: number): boolean {
	return /^(.+)\1$/.test(id.toString());
}

function isAtLeastTwice(id: number): boolean {
	return /^(.+)\1+$/.test(id.toString());
}

function sumInvalidIds(
	ranges: IdRange[],
	predicate: (id: number) => boolean,
): number {
	return pipe(ranges, A.flatMap(buildRange), A.filter(predicate), N.sumAll);
}

function main() {
	return Effect.gen(function* () {
		const ranges = yield* parseInput();

		yield* Effect.log(sumInvalidIds(ranges, isExactlyTwice));
		yield* Effect.log(sumInvalidIds(ranges, isAtLeastTwice));
	});
}

Effect.runPromise(main());
