from app import init_load


def read_mongo():
    data = init_load.mongo.db.sample.find({})
    return data