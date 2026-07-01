from fastapi import APIRouter

router = APIRouter(

    prefix="/health",

    tags=["Health"],

)


@router.get("/")

async def health():

    return {

        "status": "healthy",

        "backend": "running",

        "graph": "available",

        "version": "1.0.0",

    }