#!/usr/bin/env python3
import logging
import configparser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

config_ini = 'config.ini'

def get_sections():
    config = configparser.ConfigParser()
    config.read(config_ini)
    return config.sections()

def init_config_file():
    config = configparser.ConfigParser()
    config.read(config_ini)
    if not config.has_section('MAX_ID'):
        config.add_section('MAX_ID')
    with open(config_ini, 'w') as configfile:
        config.write(configfile, True)
    del config

def store_user_id(screen_name, max_id):
    logger.info(f"Storing id {max_id} for user {screen_name}")
    config = configparser.ConfigParser()
    config.read(config_ini)
    if not config.read('MAX_ID', screen_name):
        config.set('MAX_ID', screen_name, '0')
        with open(config_ini, 'w') as configfile:
            config.write(configfile, True)
    del config

def get_user_stored_id(screen_name):
    logger.info(f"Retrieving stored id from user {screen_name}")
    max_id = 0
    config = configparser.ConfigParser()
    config.read(config_ini)

    if not config.has_section('MAX_ID'):
        init_config_file()
        config.read(config_ini)

    if config.read('MAX_ID', screen_name):
        max_id = config.getint('MAX_ID', screen_name)
    else:
        store_user_id(screen_name, 0)

    return max_id

