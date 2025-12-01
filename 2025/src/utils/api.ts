import {
	FetchHttpClient,
	HttpClient,
	HttpClientRequest,
} from "@effect/platform";
import { Config, Effect } from "effect";

export function getAocInput({ day, year }: { day: number; year: number }) {
	return Effect.gen(function* () {
		const session = yield* Config.string("AOC_SESSION");
		const client = yield* HttpClient.HttpClient;

		const response = yield* HttpClientRequest.get(
			`https://adventofcode.com/${year}/day/${day}/input`,
		).pipe(
			HttpClientRequest.setHeader("Cookie", `session=${session}`),
			client.execute,
		);

		return yield* response.text;
	}).pipe(Effect.scoped, Effect.provide(FetchHttpClient.layer));
}
