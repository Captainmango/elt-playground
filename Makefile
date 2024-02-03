.PHONY: test-elt
test-elt:
	python -m unittest discover -v -s ./elt-script -p '*_test.py'

.PHONY: start-databases
start-databases:
	docker compose up source_postgres destination_mysql -d

.PHONY: connect-source-database
connect-source-database:
	docker exec -it source_db psql -U postgres -d src_db

.PHONY: connect-destination-database
connect-destination-database:
	docker exec -it destination_db mysql dest_db