import { Effect } from "effect";

import { getAocInput } from "./utils/api";

Effect.runPromise(getAocInput({ day: 1, year: 2025 }))
	.then(console.log)
	.catch(console.error);
