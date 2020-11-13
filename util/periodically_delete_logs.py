import datetime
from model.DAO import DAO


def periodically_delete_logs():
    dao = DAO()
    today = datetime.datetime.today()
    week_ago = today - datetime.timedelta(days=7)
    cursor = dao.db.log

    for document in cursor.find({'date': {'$lt': week_ago}}):
        dao.db.log.delete_one(document)


periodically_delete_logs()
