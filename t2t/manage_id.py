#!/usr/bin/env python3
import logging
import configparser
from configparser import ConfigParser, ExtendedInterpolation

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.disabled = True

config_ini = 'config.ini'

class Tw_user(object):
    def __init__(self):
        self.tag = None
        self.last_id = 0
        self.channel_id = ''

    def store_id(self, last_id):
        logger.info(f"Storing id {last_id} for user {self.tag}")
        config = configparser.ConfigParser()
        config.read(config_ini)

        config.set(self.tag, 'last_id', str(last_id))
        with open(config_ini, 'w') as configfile:
            config.write(configfile, True)
        del config

    def get_user_stored_id(self):
        logger.info(f"Retrieving stored id from user {self.tag}")
        last_id = 0
        config = configparser.ConfigParser()
        config.read(config_ini)

        if self.tag in config:
            last_id = config.getint(self.tag, 'last_id')
        else:
            print("Error")
        del config
        
        return last_id


def list_tw_users():
    tw_users = []
    config = configparser.ConfigParser(interpolation=ExtendedInterpolation())
    config.read(config_ini)
    sections = config.sections()

    for section in sections:
        if section == 'CHANNELS':
            continue

        tw_user = Tw_user()
        tw_user.tag = section
        logger.info(f"Procesing section {section}")
        try:
            tw_user.channel_id = config[section]['channel_id']
        except:
            print(f"Section {section} don't have channel_id")
        if not config[section]['last_id']:
            tw_user.last_id = 0
        else:
            tw_user.last_id = config[section]['last_id']
        tw_users.append(tw_user)

    del config
    return tw_users

def init_config_file(screen_name):
    config = configparser.ConfigParser()
    config.read(config_ini)
    if not config.has_section(screen_name):
        config.add_section(screen_name)
    with open(config_ini, 'w') as configfile:
        config.write(configfile, True)
    del config


