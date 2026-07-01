from fastapi import FastAPI
from fastapi.responses import JSONResponse


def add_exception_handlers(
    app: FastAPI,
):

    @app.exception_handler(Exception)

    async def global_exception_handler(

        request,

        exc,

    ):

        return JSONResponse(

            status_code=500,

            content={

                "status": "error",

                "message": str(exc),

            },

        )