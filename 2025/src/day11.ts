import {
	Array as A,
	Effect,
	flow,
	Number as N,
	Option as O,
	pipe,
	String as S,
} from "effect";
import { getAocInput } from "./utils/api";

type Device = [string, string[]];
type Devices = Map<string, string[]>;

const parseLine = (line: string): O.Option<Device> =>
	pipe(
		line,
		S.match(/^(\w+):\s*(.+)$/),
		O.flatMap(([, name, outputs]) =>
			name && outputs
				? O.some([name, outputs.split(/\s+/)] as const)
				: O.none(),
		),
	);

const parseDevices: (input: string) => Devices = flow(
	S.split("\n"),
	A.filterMap(parseLine),
	(entries) => new Map(entries),
);

const countPaths = (devices: Devices): number => {
	const count = (node: string): number =>
		node === "out" ? 1 : N.sumAll(devices.get(node)?.map(count) ?? []);
	return count("you");
};

const countPathsThrough = (devices: Devices): number => {
	const count = (node: string, need: Set<string>): number => {
		const next = (need.delete(node), need);
		return node === "out"
			? next.size === 0
				? 1
				: 0
			: N.sumAll(devices.get(node)?.map((n) => count(n, new Set(next))) ?? []);
	};
	return count("svr", new Set(["dac", "fft"]));
};

const main = Effect.gen(function* () {
	const devices = yield* pipe(
		getAocInput({ day: 11, year: 2025 }),
		Effect.map(parseDevices),
	);

	yield* Effect.log(`Part 1: ${countPaths(devices)}`);
	yield* Effect.log(`Part 2: ${countPathsThrough(devices)}`);
});

Effect.runPromise(main).catch(console.error);
