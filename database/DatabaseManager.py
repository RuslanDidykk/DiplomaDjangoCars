from contextlib import contextmanager

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import update, delete
from sqlalchemy.orm import sessionmaker

from database.DatabaseModel import Url, Models, Trims
from database.DatabaseModel import Car

from database.DatabaseModel import Session

from helpers.timestamp_generator import generate_timestamp

from config import database_uri


class DatabaseManager():
    def __init__(self):
        self.pool_connetcion = self.poolConnect()

    def poolConnect(self):
        engine = create_engine(database_uri)
        return engine

    @contextmanager
    def getConnection(self):
        self.con = self.pool_connetcion.connect()
        DBSession = sessionmaker(bind=self.con)
        session = DBSession()
        try:
            yield session
        finally:
            session.close()
            self.con.close()

    def get_grouped_listings(self):
        with self.getConnection() as session:
            list_db = session.query(Car.id, Car.make,
                                    Car.model, Car.trim,
                                    Car.year, Car.km,
                                    Car.pc). \
                group_by(Car.make, Car.model,
                         Car.trim, Car.year,
                         Car.pc, Car.id, Car.km).all()
            return list_db

    def set_deal_quality(self, status, listing_id, price_difference):
        with self.getConnection() as session:
            smtp = update(Car).where(Car.id == listing_id). \
                values(quality_deal=str(status),
                       price_difference=price_difference)
            session.execute(smtp)
            session.commit()

    def get_trim_list(self):
        trim_list = []
        with self.getConnection() as session:
            trim_list_ = session.query(Car.trim, Car.make).distinct().all()
            for car in trim_list_:
                try:
                    trim = car[0]
                    make = car[1]
                except IndexError:
                    continue
                if trim is None:
                    continue
                trim_list.append(dict(trim=trim,
                                      make=make))

            return trim_list

    def get_similar_cars_for_graph(self, make, model, trim, year):
        with self.getConnection() as session:
            list_db = session.query(Car.km, Car.days_on_market, Car.quality_deal, Car.location, Car.quality_deal,
                                    Car.pc, Car.first_price, Car.url, Car.status, Car.color). \
                filter(Car.make == make, Car.model == model, Car.trim == trim, Car.year == year). \
                group_by(Car.make, Car.model, Car.trim, Car.year, Car.pc, Car.id, Car.km).distinct().all()

            list_data = []
            list_urls = []
            list_full_data = []
            for data in list_db:
                if data.status == 'Removed':
                    list_data.append([data.km, data.pc, 'point {fill-color: grey'])
                    list_urls.append(data.url)
                else:
                    list_data.append([data.km, data.pc, 'point {fill-color: #0e55c9'])
                    list_urls.append(data.url)

                    try:
                        quality_deal = int(data.quality_deal)
                    except TypeError:
                        row_style = 'table-warning'
                        quality_deal = ''

                    if quality_deal == '':
                        row_style = 'table-warning'
                        quality_deal = ''
                    elif quality_deal > -2 and quality_deal < 2:
                        row_style = 'table-warning'
                    elif quality_deal >= 2 and quality_deal < 5:
                        row_style = 'table-primary'
                    elif quality_deal >= 5 and quality_deal < 8:
                        row_style = 'table-info'
                    elif quality_deal >= 8:
                        row_style = 'table-success'
                    else:
                        row_style = 'table-danger'

                    list_full_data.append([data.km, data.first_price, data.pc, data.days_on_market,
                                           quality_deal, data.location, data.color, data.url, row_style])

            return {
                'data': list_data,
                'full_data': list_full_data,
                'urls': list_urls
            }

    def get_all_make(self):
        with self.getConnection() as session:
            list_db = session.query(
                Car.make.distinct()
            ).group_by(Car.make).all()
            return [''] + [x[0] for x in list_db]

    def get_all_models(self, make):
        with self.getConnection() as session:
            list_db = session.query(Car.model.distinct()). \
                filter(Car.make == make) \
                .group_by(Car.model).all()
            # return [x[0] for x in list_db if x !='']
            return [''] + [x[0] for x in list_db]

    def get_all_trim(self, make, model):
        with self.getConnection() as session:
            list_db = session.query(Car.trim.distinct()). \
                filter(Car.make == make,
                       Car.model == model) \
                .group_by(Car.trim).all()
            # return [x[0] for x in list_db if x != '']
            return [''] + [x[0] for x in list_db]

    def get_all_year(self, make, model, trim):
        with self.getConnection() as session:
            list_db = session.query(Car.year.distinct()). \
                filter(Car.make == make,
                       Car.model == model,
                       Car.trim == trim) \
                .group_by(Car.year).all()
            # return [x[0] for x in list_db if x != '']
            return [''] + [x[0] for x in list_db]


#
if __name__ == '__main__':
    # for i in DatabaseManager().get_similar_cars_for_graph(make='BMW', model='3-Series', trim='320i', year=2006):
    #     print (i)
    # for i in DatabaseManager().get_all_year(''):
    #     print
    a = {
        'data': [1, 2, 3],
        'urls': [4, 5, 6]
    }
    print(a['urls'])
