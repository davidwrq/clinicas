# -*- coding: utf-8 -*-

import config
BOT_NAME = 'clinicas'

SPIDER_MODULES = ['clinicas.spiders']
NEWSPIDER_MODULE = 'clinicas.spiders'


DATABASE = {
    'drivername': 'postgres',
    'host': config.HOST,
    'port': config.PORT,
    'username': config.USER_NAME,
    'password': config.PASSWORD,
    'database':config.NAME_DB,
}


ITEM_PIPELINES = {'clinicas.pipelines.ClinicasPipeline':300}


ROBOTSTXT_OBEY = True
