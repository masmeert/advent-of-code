import {
	Array as A,
	Effect,
	flow,
	Number as N,
	Option as O,
	pipe,
	String as S,
} from "effect";
import { init } from "z3-solver";
import { getAocInput } from "./utils/api";

type Machine = { lights: number; wirings: number[]; joltage: number[] };

const match = (re: RegExp) =>
	flow(
		(s: string) => s.match(re),
		O.fromNullable,
		O.flatMap((m) => O.fromNullable(m[1])),
	);

const nums = flow(S.split(","), A.map(Number));
const bits = flow(
	A.map((i: number) => 1 << i),
	N.sumAll,
);

const parseLights = flow(
	match(/^\[([.#]*)\]/),
	O.map(
		flow(
			S.split(""),
			A.map((c, i) => (c === "#" ? 1 << i : 0)),
			N.sumAll,
		),
	),
	O.getOrElse(() => 0),
);

const parseWirings = flow(
	(line: string) => [...line.matchAll(/\(([^)]+)\)/g)],
	A.filterMap((m) => O.fromNullable(m[1])),
	A.map(flow(nums, bits)),
);

const parseJoltage = flow(
	match(/\{([^}]+)\}$/),
	O.map(nums),
	O.getOrElse((): number[] => []),
);

const parseMachine = (line: string): Machine => ({
	lights: parseLights(line),
	wirings: parseWirings(line),
	joltage: parseJoltage(line),
});

const parseInput = flow(S.trim, S.split("\n"), A.map(parseMachine));

const stepsForLights = ({ lights: target, wirings }: Machine): number => {
	const seen = new Set([0]);
	let frontier = [0];

	for (let depth = 0; frontier.length > 0; depth++) {
		if (frontier.includes(target)) return depth;

		frontier = pipe(
			frontier,
			A.flatMap((mask) => A.map(wirings, (w) => mask ^ w)),
			A.dedupe,
			A.filter((m) => {
				if (seen.has(m)) return false;
				seen.add(m);
				return true;
			}),
		);
	}
	return -1;
};

const stepsForJoltages = ({ wirings, joltage }: Machine) =>
	Effect.gen(function* () {
		const { Context } = yield* Effect.promise(init);
		const ctx = Context("main");
		const opt = new ctx.Optimize();

		const btns = wirings.map((_, i) => ctx.Int.const(`b${i}`));
		for (const b of btns) opt.add(b.ge(0));

		for (const [j, target] of joltage.entries()) {
			const terms = A.zip(wirings, btns)
				.filter(([m]) => m & (1 << j))
				.map(([, b]) => b);
			if (terms.length) opt.add(terms.reduce((a, b) => a.add(b)).eq(target));
		}

		opt.minimize(btns.reduce((a, b) => a.add(b)));
		if ((yield* Effect.promise(() => opt.check())) !== "sat") return 0;

		return pipe(
			btns,
			A.map((b) => Number(opt.model().eval(b).toString())),
			N.sumAll,
		);
	});

const totalStepsForLights = flow(A.map(stepsForLights), N.sumAll);

const totalStepsForJoltages = flow(
	A.map(stepsForJoltages),
	Effect.all,
	Effect.map(N.sumAll),
);

const main = Effect.gen(function* () {
	const machines = yield* pipe(
		getAocInput({ day: 10, year: 2025 }),
		Effect.map(parseInput),
	);

	const p1 = totalStepsForLights(machines);
	const p2 = yield* totalStepsForJoltages(machines);

	yield* Effect.log(`Part 1: ${p1}`);
	yield* Effect.log(`Part 2: ${p2}`);
});

Effect.runPromise(main).catch(console.error);
