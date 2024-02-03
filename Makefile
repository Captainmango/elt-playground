
.PHONY: start-source-database
start-source-database:
	docker compose up source_postgres -d

.PHONY: connect-source-database
connect-source-database:
	docker exec -it source_db psql -U postgres -d src_db