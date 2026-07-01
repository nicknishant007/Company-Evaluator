from enum import Enum


class Environment(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TESTING = "testing"


DEFAULT_TIMEOUT = 30

DEFAULT_RETRIES = 3

CACHE_TTL = 3600

PROJECT_NAME = "Company Evaluator"