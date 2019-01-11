# -*- coding: utf-8 -*-
import cx_Oracle
from pyhive import hive

from utils.decorators import static_vars
from utils.load_config import load_config
from utils.logger import get_logger

logging = get_logger()


@static_vars(oracle_conn=None, hive_conn=None)
def get_connection(db_type='oracle'):

    logging.info("Connecting to db.")
    config = load_config()

    if db_type == 'oracle':
        if get_connection.oracle_conn is None:
            config = config['oracle_db']
            dsn_config = config['dsn']
            dsn_tns = cx_Oracle.makedsn(**dsn_config)

            connection_config = config['connection']
            connection_config['dsn'] = dsn_tns
            get_connection.oracle_conn = cx_Oracle.connect(**connection_config)
        return get_connection.oracle_conn
    elif db_type == 'hive':
        if get_connection.hive_conn is None:
            config = config['hive_db']
            get_connection.hive_conn = hive.Connection(**config)
        return get_connection.hive_conn
    else:
        raise ValueError("DB Type can be : 'oracle' or 'hive' ")


if __name__ == '__main__':
    # Test static variables creating just one time.
    get_connection("oracle")
    get_connection("hive")
    get_connection("hive")
    get_connection.hive_conn = None
    get_connection()
    get_connection()
