
start-source-database:
	docker compose up source_postgres -d

connect-source-database:
	docker exec -it source_db psql -U postgres