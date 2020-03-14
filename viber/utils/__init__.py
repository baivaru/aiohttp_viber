import configparser
from pathlib import Path


def load_app_configuration():
    config = configparser.ConfigParser()
    config.read(Path("viber/working_dir/config.ini"))

    return config
