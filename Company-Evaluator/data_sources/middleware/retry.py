from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
    before_sleep_log,
)

from observability import app_logger

from data_sources.exceptions import (
    ProviderUnavailableError,
)


def retry_on_failure(
    attempts: int = 3,
):
    

    return retry(
        stop=stop_after_attempt(attempts),

        wait=wait_exponential(
            multiplier=1,
            min=2,
            max=10,
        ),

        retry=retry_if_exception_type(
            ProviderUnavailableError
        ),
        before_sleep=before_sleep_log(
            app_logger,
            "WARNING",
        ),
        reraise=True,
    )