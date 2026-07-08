import os
from dotenv import load_dotenv
load_dotenv()



from fastapi import FastAPI

from backend.core.lifespam import lifespan

from backend.api.routes.health import router as health_router
from backend.api.routes.analyze import router as analyze_router
from backend.api.routes.report import router as report_router
from backend.api.routes.pdf import router as pdf_router

from backend.middleware.cors import add_cors
from backend.middleware.exception import add_exception_handlers



app = FastAPI(
    title="Company Evaluator API",
    description="AI Powered Equity Research Platform",
    version="1.0.0",
    lifespan=lifespan
)

add_cors(app)

add_exception_handlers(app)

# Register Routers
app.include_router(health_router)
app.include_router(analyze_router)
app.include_router(report_router)
app.include_router(pdf_router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to Company Evaluator API"
    }