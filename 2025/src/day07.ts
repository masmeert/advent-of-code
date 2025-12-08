import {
	Array as A,
	Effect,
	Number as N,
	Option as O,
	pipe,
	String as S,
} from "effect";
import { getAocInput } from "./utils/api";

type State = { timelines: number[]; splits: number };

const fetchInput = getAocInput({ day: 7, year: 2025 }).pipe(
	Effect.map(S.trim),
	Effect.map(S.split("\n")),
);

const makeInitialTimelines = (width: number, center: number): number[] =>
	pipe(
		A.makeBy(width, () => 0),
		A.replaceOption(center, 1),
		O.getOrElse(() => []),
	);

const isSplitterAt = (lines: string[], y: number, x: number): boolean =>
	pipe(
		O.fromNullable(lines[y * 2 + 2]),
		O.flatMap((row) => O.fromNullable(row[x])),
		O.map((c) => c === "^"),
		O.getOrElse(() => false),
	);

const splitAt = (timelines: number[], x: number, count: number): number[] =>
	pipe(
		timelines,
		A.modify(x, () => 0),
		A.modify(x - 1, (v) => v + count),
		A.modify(x + 1, (v) => v + count),
	);

const processPosition =
	(lines: string[], y: number) =>
	(state: State, x: number): State =>
		pipe(
			O.fromNullable(state.timelines[x]),
			O.filter((count) => count > 0 && isSplitterAt(lines, y, x)),
			O.match({
				onNone: () => state,
				onSome: (count) => ({
					timelines: splitAt(state.timelines, x, count),
					splits: state.splits + 1,
				}),
			}),
		);

const processRow =
	(lines: string[], center: number) =>
	(state: State, y: number): State =>
		pipe(
			A.range(center - y, center + y),
			A.filter((x) => (x - center + y) % 2 === 0),
			A.reduce(state, processPosition(lines, y)),
		);

const parse = (lines: string[]) =>
	pipe(
		O.fromNullable(lines[0]),
		O.map((firstLine) => {
			const width = firstLine.length;
			const center = width >> 1;
			const rowCount = (lines.length - 1) >> 1;

			const initialState: State = {
				timelines: makeInitialTimelines(width, center),
				splits: 0,
			};

			const finalState = pipe(
				A.range(0, rowCount - 1),
				A.reduce(initialState, processRow(lines, center)),
			);

			return [finalState.splits, A.reduce(finalState.timelines, 0, N.sum)];
		}),
		O.getOrElse(() => [0, 0]),
	);

const main = Effect.gen(function* () {
	const lines = yield* fetchInput;
	const [part1, part2] = parse(lines);
	yield* Effect.log("Part 1:", part1);
	yield* Effect.log("Part 2:", part2);
});

Effect.runPromise(main);
