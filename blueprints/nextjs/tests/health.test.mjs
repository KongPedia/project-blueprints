import assert from "node:assert/strict";
import test from "node:test";
import { GET } from "../src/app/api/health/route.ts";

test("health route returns a successful JSON starter status", async () => {
  const response = GET();
  assert.equal(response.status, 200);
  assert.equal(response.headers.get("content-type"), "application/json");
  assert.deepEqual(await response.json(), { status: "ok" });
});
