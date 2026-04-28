from stcore import pms
from core.config import DB_NAME

class Connection:
    cnx = None
    wcnx = None

    def __init__(self):
        self.cnx = Connection.cnx
        self.wcnx = Connection.wcnx

    def get_connection(self):
        Connection.cnx = pms.get_reader_cnx(DB_NAME)
        Connection.wcnx = pms.get_writer_cnx(DB_NAME)

        return Connection.cnx, Connection.wcnx
