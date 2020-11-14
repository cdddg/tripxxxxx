FROM  mysql:5.7
ENV   MYSQL_DATABASE tripresso_local
ENV   MYSQL_ROOT_PASSWORD qwerty
CMD   ["mysqld", "--character-set-server=utf8mb4", "--collation-server=utf8mb4_unicode_ci"]

