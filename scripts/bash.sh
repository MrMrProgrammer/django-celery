# Network

docker network create -d bridge hame-akhbar

# -----------------------------------------------------------------------------
# PostgreSQL

docker volume create hame_akhbar_pg_data

docker run -d --name PostgreSQL-HameAkhbar --network hame-akhbar \
  -e POSTGRES_DB=hame_akhbar -e POSTGRES_USER=root -e POSTGRES_PASSWORD=1234 \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v hame_akhbar_pg_data:/var/lib/postgresql/data -p 5432:5432 \
  docker.arvancloud.ir/library/postgres:15-alpine

# docker run -d --name BjakPgAdmin --network bjak-network \
#   -e PGADMIN_DEFAULT_EMAIL=admin@example.com \
#   -e PGADMIN_DEFAULT_PASSWORD=admin123 \
#   -p 5050:80 dpage/pgadmin4:latest

# -----------------------------------------------------------------------------
# MySQL

docker volume create hame_akhbar_mysql_data

docker run -d --name MySQL-HameAkhbar --network hame-akhbar \
  -e MYSQL_DATABASE=hame_akhbar -e MYSQL_ROOT_PASSWORD=1234 \
  -v hame_akhbar_mysql_data:/var/lib/mysql -p 3306:3306 mysql

docker run -d --name PhpMyAdmin-HameAkhbar -p 3311:80 \
  --link MySQL-HameAkhbar:db \
  --network hame-akhbar phpmyadmin/phpmyadmin:latest

# -----------------------------------------------------------------------------
