FROM ghcr.io/dbt-labs/dbt-postgres:1.7.5
COPY . /dbt
CMD ["run", "--profiles-dir", "/dbt", "--project-dir", "/dbt"]