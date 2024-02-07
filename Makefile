.PHONY: test-elt
test-elt:
	python -m unittest discover -v -s ./elt-script -p '*_test.py'

.PHONY: start-elt
start-elt:
	docker compose up elt -d

.PHONY: test-dbt
test-dbt:
	cd elt-script/postgres_transform && poetry run dbt test

.PHONY: run-dbt
test-dbt:
	cd elt-script/postgres_transform && poetry run dbt run

.PHONY: run
run:
	docker compose up -d

.PHONY: start-databases
start-databases:
	docker compose up source_postgres destination_postgres -d

.PHONY: connect-source-database
connect-source-database:
	docker exec -it source_db psql -U postgres -d src_db

.PHONY: connect-destination-database
connect-destination-database:
	docker exec -it destination_db psql -U postgres -d dest_db

