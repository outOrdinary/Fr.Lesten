import redis


class Config(object):
    SECRET_KEY = "fawefvzcvxzfawefsg23r45;..tb3,4"

    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome_python"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    SESSION_TYPE = "redis"
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    PERMANENT_SESSION_LIFETIME = 86400


class DevelopmenConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


config_dict = {
    "develop": DevelopmenConfig,
    "product": ProductionConfig
}
