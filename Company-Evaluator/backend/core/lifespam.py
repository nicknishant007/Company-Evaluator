from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.core.logger import logger


@asynccontextmanager
async def lifespan(
    app: FastAPI,
):

    logger.info(
        "Starting Company Evaluator..."
    )

    yield

    logger.info(
        "Shutting Down..."
    )