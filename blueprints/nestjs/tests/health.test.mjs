import "reflect-metadata";
import assert from "node:assert/strict";
import test from "node:test";
import { NestFactory } from "@nestjs/core";
import { AppModule } from "../dist/app.module.js";

test("GET /health returns the starter status over HTTP", async (context) => {
  const app = await NestFactory.create(AppModule, { logger: false, abortOnError: false });
  context.after(() => app.close());
  await app.listen(0, "127.0.0.1");
  const response = await fetch(`${await app.getUrl()}/health`, { signal: AbortSignal.timeout(5000) });
  assert.equal(response.status, 200);
  assert.deepEqual(await response.json(), { status: "ok" });
});
