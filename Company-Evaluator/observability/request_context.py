from contextvars import ContextVar
from typing import Optional

# Stores the current request ID for the active context
_request_id_ctx_var: ContextVar[Optional[str]] = ContextVar(
    "request_id",
    default=None,
)


def set_request_id(request_id: str) -> None:
    """
    Set the request ID for the current execution context.
    """
    _request_id_ctx_var.set(request_id)


def get_request_id() -> Optional[str]:
    """
    Get the current request ID.
    """
    return _request_id_ctx_var.get()


def clear_request_id() -> None:
    """
    Clear the request ID after the request finishes.
    """
    _request_id_ctx_var.set(None)