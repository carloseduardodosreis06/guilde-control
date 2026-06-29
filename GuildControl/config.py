SECRET_KRY = "guildcontrol2026"

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
    BASE_DIR
    "database",
    "database.db"
)

SQLALCHEMY_TRANCK_MODIFICATIONS = False 
FREE_GUILDAS = 1
FREE_LINES = 10

PLUS_GUILDA = 3
PLUS_LINES = 20

PRO_GUILDA = 999
PRO_LINES = 999

# ==========================
# CONFIGURAÇÃO DO PIX
# ==========================

PIX_CHAVE = "ce023233@gmail.com"
