import {
	Array as A,
	Effect,
	Number as N,
	Order,
	pipe,
	String as S,
} from "effect";
import { getAocInput } from "./utils/api";

type IngredientRange = { start: number; end: number };

const parseIngredientRange = (line: string): IngredientRange =>
	pipe(line, S.split("-"), A.map(Number), ([start = 0, end = 0]) => ({
		start,
		end,
	}));

const parseInput = () =>
	getAocInput({ day: 5, year: 2025 }).pipe(
		Effect.map(S.trim),
		Effect.map(S.split("\n\n")),
		Effect.map(([freshSection = "", availableSection = ""]) => ({
			freshRanges: pipe(
				freshSection,
				S.split("\n"),
				A.map(parseIngredientRange),
			),
			availableIds: pipe(availableSection, S.split("\n"), A.map(Number)),
		})),
	);

const isIdInRange = (id: number) => (range: IngredientRange) =>
	id >= range.start && id <= range.end;

const isIngredientFresh =
	(freshRanges: IngredientRange[]) =>
	(id: number): boolean =>
		pipe(freshRanges, A.some(isIdInRange(id)));

const rangeLength = (range: IngredientRange): number =>
	range.end - range.start + 1;

const byStartAsc = Order.mapInput(
	Order.number,
	(range: IngredientRange) => range.start,
);

const appendNewRange = (
	accumulated: IngredientRange[],
	current: IngredientRange,
): IngredientRange[] => pipe(accumulated, A.append(current));

const mergeWithLastRange = (
	accumulated: IngredientRange[],
	itemCount: number,
	lastRange: IngredientRange,
	current: IngredientRange,
): IngredientRange[] =>
	pipe(
		A.take(itemCount - 1)(accumulated),
		A.append({
			start: lastRange.start,
			end: Math.max(lastRange.end, current.end),
		}),
	);

const mergeOrAppend = (
	accumulated: IngredientRange[],
	current: IngredientRange,
): IngredientRange[] =>
	pipe(
		accumulated,
		A.match({
			onEmpty: () => [current],
			onNonEmpty: (items) => {
				const lastRange = A.lastNonEmpty(items);
				const itemCount = A.length(items);
				return current.start > lastRange.end + 1
					? appendNewRange(accumulated, current)
					: mergeWithLastRange(accumulated, itemCount, lastRange, current);
			},
		}),
	);

const mergeOverlappingRanges = (ranges: IngredientRange[]): IngredientRange[] =>
	pipe(
		ranges,
		A.sortBy(byStartAsc),
		A.reduce([] as IngredientRange[], mergeOrAppend),
	);

const countFreshIngredientsAvailable = (
	freshRanges: IngredientRange[],
	availableIds: number[],
): number =>
	pipe(availableIds, A.filter(isIngredientFresh(freshRanges)), A.length);

const countTotalFreshIngredientIds = (freshRanges: IngredientRange[]): number =>
	pipe(freshRanges, mergeOverlappingRanges, A.map(rangeLength), N.sumAll);

const main = Effect.gen(function* () {
	const { freshRanges, availableIds } = yield* parseInput();

	const freshAvailableCount = countFreshIngredientsAvailable(
		freshRanges,
		availableIds,
	);
	const totalFreshIdsCount = countTotalFreshIngredientIds(freshRanges);

	yield* Effect.log(`Part 1: ${freshAvailableCount}`);
	yield* Effect.log(`Part 2: ${totalFreshIdsCount}`);
});

Effect.runPromise(main).catch(console.error);
