# db_config.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from urllib.parse import quote_plus

# Carrega variáveis do .env
load_dotenv()

# Caminho do banco SQLite (arquivo dentro do projeto)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "sgb.db")

db = SQLAlchemy()

def init_app(app: Flask):
    db_type = os.getenv("DB_TYPE", "sqlite")  # sqlite é o padrão

    if db_type == "mysql":
        user = os.getenv("DB_USER")
        password = quote_plus(os.getenv("DB_PASSWORD", ""))
        host = os.getenv("DB_HOST", "127.0.0.1")
        port = os.getenv("DB_PORT", "3306")
        dbname = os.getenv("DB_NAME", "sgb")

        app.config["SQLALCHEMY_DATABASE_URI"] = (
            f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{dbname}"
        )
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    return app