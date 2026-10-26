import "reflect-metadata";
import { NestFactory } from "@nestjs/core";
import { AppModule } from "./app.module.js";

const app = await NestFactory.create(AppModule, { abortOnError: false });
app.enableShutdownHooks();
try {
  await app.listen(3000, "127.0.0.1");
} catch (error) {
  await app.close();
  throw error;
}
