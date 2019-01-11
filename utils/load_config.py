import yaml

from utils.decorators import static_vars
from utils.logger import get_logger

logging = get_logger()


@static_vars(config=None)
def load_config(config_file='etc/config.yaml'):
    if load_config.config is None:
        try:
            with open(config_file, 'r') as conf:
                load_config.config = yaml.load(conf)
                logging.info("Config file loding")
        except Exception as e:
            logging.exception(e)

    return load_config.config


if __name__ == '__main__':
    print(load_config())
    print(load_config())
    print(load_config())
