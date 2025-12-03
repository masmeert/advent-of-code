import { Array as A, Effect, Number as N, Order as O, pipe } from "effect";
import { getAocInput } from "./utils/api";

type State = { pos: number; digits: string };

function parseInput() {
	return getAocInput({ day: 3, year: 2025 }).pipe(
		Effect.map((input) => input.trim().split("\n")),
	);
}

function orderByDigitAt(s: string): O.Order<number> {
	return O.mapInput(O.string, (i: number) => s.charAt(i));
}

function maxJoltage(bank: string, count: number): number {
	const initial: State = { pos: 0, digits: "" };

	const pickNextDigit = ({ pos, digits }: State, i: number): State => {
		const searchRange = A.range(pos, bank.length - count + i);
		const bestIndex = pipe(searchRange, A.max(orderByDigitAt(bank)));
		return { pos: bestIndex + 1, digits: digits + bank.charAt(bestIndex) };
	};

	return pipe(
		A.range(0, count - 1),
		A.reduce(initial, pickNextDigit),
		({ digits }) => Number(digits),
	);
}

function sumMaxJoltages(banks: string[], count: number): number {
	return pipe(
		A.map(banks, (bank) => maxJoltage(bank, count)),
		N.sumAll,
	);
}

function main() {
	return Effect.gen(function* () {
		const banks = yield* parseInput();
		yield* Effect.log(sumMaxJoltages(banks, 2));
		yield* Effect.log(sumMaxJoltages(banks, 12));
	});
}

Effect.runPromise(main());
