class Config:
    SECRET_KEY = "ASDASDASDASDADAA"

class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST='127.0.0.1'
    MYSQL_USER='Juver'
    MYSQL_PASSWORD='root'
    MYSQL_DB='tickets'

config = {
    'development': DevelopmentConfig
}