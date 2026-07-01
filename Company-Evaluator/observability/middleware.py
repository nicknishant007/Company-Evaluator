import uuid

from starlette.middleware.base import BaseHTTPMiddleware

from observability.request_context import request_id


class RequestContextMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        rid = str(uuid.uuid4())

        request_id.set(rid)

        response = await call_next(request)

        response.headers["X-Request-ID"] = rid

        return response