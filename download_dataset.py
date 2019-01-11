# -*- coding: utf-8 -*-
import argparse
import os
import pandas as pd
import yaml
from tqdm import tqdm

from utils.db_connection import get_connection
from utils.create_dir import create_dir
from utils.logger import get_logger
from utils.read_file import read_file

logging = get_logger()


def download_dataset(sql_file, conn, output_file):
    sql = read_file(sql_file)
    logging.info(sql)

    df = pd.read_sql_query(sql, con=conn, chunksize=100000)
    chunk = next(df)
    chunk.drop_duplicates().to_csv(output_file, mode='w', index=None)
    for chunk in tqdm(df):
        chunk.drop_duplicates().to_csv(output_file, mode='a', index=None, header=None)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--config_file', type=str, default='./etc/foo.cfg')

    args = parser.parse_args()
    logging.info("Args : {}".format(args))

    config = yaml.safe_load(open(args.config_file))
    sql_file = config['sql_file']
    output_file = config['output_file']

    create_dir(os.path.dirname(output_file))

    if os.path.exists(output_file):
        logging.warning('There is already a file with name %s' % output_file)
    else:
        logging.info('Downloading download_dataset from database')
        download_dataset(sql_file, get_connection(config['db']), output_file)
    logging.info("End of file.")
