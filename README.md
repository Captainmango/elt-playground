# ELT Crash Course

This is me playing about with an ELT pattern as a data engineer. This isn't a serious thing, just me trying out some tools and seeing what I like and don't like.

## Usage
Set up a .env in the root of the project for use with the docker compose file. There is a Makefile for running things easier.

### Example env
```
SOURCE_DB=src_db
SOURCE_USER=postgres
SOURCE_PASS=password
SOURCE_PORT=5432

DEST_DB=dest_db
DEST_USER=mysql
DEST_ROOT_PASS=password
DEST_PORT=3306
```

### Makefile
- `make start-databases` Starts the source and destination databases and seeds the source with initial data (queries in source_db_init/init.sql)
- `make connect-source-db` Connect to the source database using the psql client
- `make connect-destination-db` Connect to the destination database using the mysql client
- `make test-elt` Run the ELT script's tests
- `make start-elt` Start the ELT script
- `make run` Run the docker compose file that starts the databases and the ELT script once both DBs are healthy