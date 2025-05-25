#!/usr/bin/env python3
"""
Script para inicializar o banco de dados
"""

from flask import Flask
from infrastructure.database import db
from infrastructure.config import Config
import models


def create_app():
    """Factory function para criar a aplicação Flask"""
    app = Flask(__name__)
    app.config["SECRET_KEY"] = Config.SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = Config.SQLALCHEMY_TRACK_MODIFICATIONS

    db.init_app(app)
    return app


def init_database():
    """Inicializa o banco de dados criando todas as tabelas"""
    app = create_app()

    with app.app_context():
        # Remove todas as tabelas existentes e recria
        db.drop_all()
        db.create_all()
        print("✅ Banco de dados inicializado com sucesso!")
        print("📋 Tabelas criadas:")

        # Lista as tabelas criadas
        for table in db.metadata.tables.keys():
            print(f"   - {table}")


if __name__ == "__main__":
    init_database()
