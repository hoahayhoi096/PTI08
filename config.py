import os

class Config():
    LOCAL_DIR = os.getcwd()
    UI_DIR = os.path.join(LOCAL_DIR, "ui")

    ANIME_JSON_PATH = 'data/data.json'
    ACCOUNT_JSON_PATH = 'data/account.json'
