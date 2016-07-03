# -*- coding: utf-8 -*-
from sqlalchemy.orm import sessionmaker
from models import Clinicas, db_connect, create_clinicas_table


class ClinicasPipeline(object):
    """DentistasPipeline pipeline for storing scraped items in the database"""
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates Dentists table.
        """
        engine = db_connect()
        create_clinicas_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save Dentists in the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        deal = Clinicas(**item)

        try:
            session.add(deal)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
