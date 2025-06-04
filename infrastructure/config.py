import os
from dotenv import load_dotenv

load_dotenv()

print("DEBUG: Iniciando infrastructure/config.py")

# Descobrir o caminho do .env que python-dotenv tentará carregar
from dotenv import find_dotenv
dotenv_path = find_dotenv()
print(f"DEBUG: Caminho do .env encontrado por find_dotenv(): {dotenv_path}")

# Tentar carregar o .env e verificar se foi bem-sucedido
loaded_successfully = load_dotenv(dotenv_path) # Carrega o .env encontrado
print(f"DEBUG: .env carregado com sucesso? {loaded_successfully}")

# Verificar o valor de DATABASE_URL IMEDIATAMENTE após load_dotenv
# db_url_after_load = os.getenv("DATABASE_URL")
# print(f"DEBUG: Valor de DATABASE_URL (após load_dotenv): '{db_url_after_load}'")
# --- Fim das Modificações para Debug ---

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///app.db") # Esta linha usa o valor de DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --- Adicionar Debug para a URI final ---
    # print(f"DEBUG: Config.SQLALCHEMY_DATABASE_URI definida como: '{SQLALCHEMY_DATABASE_URI}'")
    # --- Fim do Debug para a URI final ---

    DEBUG = os.getenv("DEBUG", "True").lower() == "true"

    @staticmethod
    def init_app(app):
        """Método para inicializar configurações específicas da aplicação"""
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DATABASE_URL", "sqlite:///dev_app.db")


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///app.db")


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}
