import os

import pymysql

from .base import *

pymysql.version_info = (1, 4, 0, "final", 0)
pymysql.install_as_MySQLdb()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "tripresso_local",
        "USER": "root",
        "PASSWORD": "qwerty",
        "HOST": os.getenv("LOCAL_DB_HOST") or "127.0.0.1",
        "PORT": 3306,
        "OPTIONS": {
            "charset": "utf8mb4",
            "init_command": "SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));",
        },
        "TEST": {"CHARSET": "utf8mb4", "COLLATION": "utf8mb4_unicode_ci"},
    },
}
DATABASE_CATEGORY = "MYSQL"

MIDDLEWARE += ["silk.middleware.SilkyMiddleware"]

INSTALLED_APPS += ["silk"]
