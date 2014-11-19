
panaface

Access Postgres from command line

	sudo -u postgres psql

	CREATE USER panasimon with PASSWORD 'password';

	GRANT ALL PRIVILEGES ON DATABASE "panadb" to panasimon;
	