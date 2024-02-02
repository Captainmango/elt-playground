# ELT Crash Course

This is me playing about with an ELT pattern as a data engineer. This isn't a serious thing, just me trying out some tools and seeing what I like and don't like.

## Usage
Set up a .env in the root of the project for use with the docker compose file. There is a Makefile for running things easier.

### Example env
```
POSTGRES_DB: source_db
POSTGRES_USER: postgres
POSTGRES_PASSWORD: secret
```

### Makefile
- `make start-source-db` Starts the source database and seeds the initial data
- `make connect-source-db` Connect to the source database using the psql client