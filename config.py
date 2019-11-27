import os

class Config:
<<<<<<< HEAD
   SECRET_KEY=os.environ.get('SECRET_KEY')
   
   #Email configurations
   MAIL_SERVER='smtp.googlemail.com'
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=os.environ.get("MAIL_USERNAME")
   MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD")

   # simple mde  configurations
   SIMPLEMDE_JS_IIFE=True
   SIMPLEMDE_USE_CDN=True

class ProdConfig(Config):
   SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://njoro:njoro@localhost/awesome'
   DEBUG=True
=======
   SECRET_KEY = os.environ.get('SECRET_KEY')	 

class ProdConfig(Config):
   pass

class DevConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://njoro:njoro@localhost/awesome'
   DEBUG = True
>>>>>>> 5e8386819438b482f418774b64bbd2b55e253006

config_options = {
'development':DevConfig,
'production':ProdConfig
}
