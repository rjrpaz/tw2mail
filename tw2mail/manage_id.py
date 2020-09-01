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

def init_config_file(screen_name):
    config = configparser.ConfigParser()
    config.read(config_ini)
    if not config.has_section(screen_name):
        config.add_section(screen_name)
    with open(config_ini, 'w') as configfile:
        config.write(configfile, True)
    del config

def store_user_id(screen_name, last_id):
    logger.info(f"Storing id {last_id} for user {screen_name}")
    config = configparser.ConfigParser()
    config.read(config_ini)

    config.set(screen_name, 'last_id', str(last_id))
    with open(config_ini, 'w') as configfile:
        config.write(configfile, True)
    del config

def get_user_stored_id(screen_name):
    logger.info(f"Retrieving stored id from user {screen_name}")
    last_id = 0
    config = configparser.ConfigParser()
    config.read(config_ini)

    if screen_name in config:
        last_id = config.read[screen_name, 'last_id']
        print(f"ENTRE {last_id}")
    else:
        print("NO ANDA")
    del config
    
    return last_id

