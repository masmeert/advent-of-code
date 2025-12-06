import {
	Array as A,
	Effect,
	Number as N,
	Option as O,
	pipe,
	String as S,
} from "effect";
import { getAocInput } from "./utils/api";
import { transpose } from "./utils/array";

type Operator = "+" | "*";

const operations: Record<Operator, (n: number[]) => number> = {
	"+": N.sumAll,
	"*": N.multiplyAll,
};

const isOperator = (c: string): c is Operator => c in operations;

const fetchInput = getAocInput({ day: 6, year: 2025 }).pipe(Effect.map(S.trim));

const evaluate = (expr: string) =>
	pipe(
		S.split(expr, "+"),
		A.map((t) => pipe(S.split(t, "*"), A.map(Number), N.multiplyAll)),
		N.sumAll,
	);

const toColumns = (input: string): string[][] =>
	pipe(
		S.split(input, "\n"),
		(lines) =>
			A.map(lines, (l) =>
				l.padEnd(pipe(lines, A.map(S.length), A.reduce(0, Math.max))),
			),
		A.map((l) => S.split(l, "")),
		transpose,
	);

const tokenRows = (input: string) =>
	pipe(
		S.split(input, "\n"),
		A.map((l) => pipe(S.split(l, /\s+/), A.filter(S.isNonEmpty))),
	);

const part1 = (input: string) =>
	pipe(
		tokenRows(input),
		(rows) =>
			A.zip(
				O.getOrElse(A.last(rows), () => [] as string[]),
				transpose(A.dropRight(rows, 1)),
			),
		A.map(([op, nums]) => operations[op as Operator](A.map(nums, Number))),
		N.sumAll,
	);

const part2 = (input: string) =>
	pipe(
		toColumns(input),
		A.reduce({ op: "+" as Operator, expr: "" }, ({ op, expr }, col) => {
			const nextOp = isOperator(col.at(-1) ?? "") ? (col.at(-1) as Operator) : op;
			const digits = pipe(col, A.dropRight(1), A.join(""), S.trim);
			return {
				op: nextOp,
				expr: digits ? `${expr}${digits}${nextOp}` : `${expr.slice(0, -1)}+`,
			};
		}),
		({ expr }) => evaluate(expr.slice(0, -1)),
	);

const main = Effect.gen(function* () {
	const input = yield* fetchInput;
	yield* Effect.log("Part 1:", part1(input));
	yield* Effect.log("Part 2:", part2(input));
});

Effect.runPromise(main);
