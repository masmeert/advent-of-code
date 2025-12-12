import {
	Array as A,
	Effect,
	Number as N,
	Option as O,
	pipe,
	String as S,
} from "effect";
import { getAocInput } from "./utils/api";

type Region = { w: number; h: number; shapeCount: number };

const parseRegion = (line: string): Region => {
	const [w = 0, h = 0, ...counts] = [...line.matchAll(/\d+/g)].map(Number);
	return { w, h, shapeCount: N.sumAll(counts) };
};

const canFit = ({ w, h, shapeCount }: Region) =>
	Math.floor(w / 3) * Math.floor(h / 3) >= shapeCount;

const parseInput = () =>
	getAocInput({ day: 12, year: 2025 }).pipe(
		Effect.map(S.trim),
		Effect.map((input) =>
			pipe(
				S.split(input, "\n\n"),
				A.last,
				O.map((section) => A.map(S.split(section, "\n"), parseRegion)),
				O.getOrElse(() => [] as Region[]),
			),
		),
	);

const solvePart1 = (regions: Region[]) =>
	pipe(regions, A.filter(canFit), A.length);

const main = Effect.gen(function* () {
	const regions = yield* parseInput();
	yield* Effect.log("Part 1:", solvePart1(regions));
});

Effect.runPromise(main).catch(console.error);
