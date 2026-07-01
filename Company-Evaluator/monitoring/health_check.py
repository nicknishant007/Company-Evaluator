from monitoring.checks.database import (
    check_database
)

from monitoring.checks.redis import (
    check_redis
)


async def get_health_status():

    db_status = await check_database()

    redis_status = await check_redis()

    overall_status = (
        "healthy"
        if db_status and redis_status
        else "unhealthy"
    )

    return {

        "status": overall_status,

        "database": (
            "up"
            if db_status
            else "down"
        ),

        "redis": (
            "up"
            if redis_status
            else "down"
        ),
    }