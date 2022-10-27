.PHONY: start start_build stop unit_tests check_typing

UNIT_TEST=pytest tests

start:
	@docker-compose up -d

start_build:
	@docker-compose up --build -d

stop:
	@docker-compose down

unit_tests:
	@docker-compose exec -T app-test $(UNIT_TEST)

unit_tests_local:
	$(UNIT_TEST)

check_typing:
	@docker-compose exec -T app-test mypy .
