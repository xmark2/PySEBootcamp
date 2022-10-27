from pydantic import BaseSettings, PostgresDsn
import os


class Config(BaseSettings):
    # host = PostgresDsn  # os.getenv("db_host")
    host = os.getenv("db_host")
    class Config:
        env_prefix = "db_"


# echo $TEST_VAR
# export TEST_VAR="env var value"
# echo $TEST_VAR

# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
