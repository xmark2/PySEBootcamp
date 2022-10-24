import os


class Config:
    DB_HOST = os.getenv("DB_HOST", "my.database.com")
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")


# echo $TEST_VAR
# export TEST_VAR="env var value"
# echo $TEST_VAR

# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
