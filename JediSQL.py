# -*- coding: utf-8 -*-
import MySQLdb
import config

class JediMaster:
    def __init__(self):
        self.db = {}
        self.jedi = MySQLdb.connect(u"localhost", config.user, config.password)
        self.set_encoding(self.jedi)

    def get_database(self, database = None):
        if not database: return self.jedi
        if database not in self.db:
            self.db[database] = MySQLdb.connect(u"localhost", config.user, config.password, database)
            self.set_encoding(self.db[database])
        return self.db[database]

    def set_encoding(self, db):
        db.set_character_set('utf8')
        cursor = db.cursor()
        cursor.execute(u'SET NAMES utf8;')
        cursor.execute(u'SET CHARACTER SET utf8;')
        cursor.execute(u'SET character_set_connection=utf8;')

    def create_database(self, db):
        cursor = self.get_database().cursor()
        cursor.execute(u"CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci".format(db))

    def create_table(self, database, table, columns):
        cursor = self.get_database(database).cursor()
        for i in xrange(len(columns)): columns[i] = u" ".join(columns[i])
        columns = u", ".join(columns)
        command = u"CREATE TABLE IF NOT EXISTS {} ({})".format(table, columns)
        cursor.execute(command)

    def insert_column(self, database, table, column):
        cursor = self.get_database(database).cursor()
        s = u", ".join([u"%s"] * len(column))
        cursor.execute(u"INSERT INTO {} VALUES ({})".format(table, s), column)

    def insert_column_custom(self, database ,table, column):
        cursor = self.get_database(database).cursor()
        key = []
        value = []
        for k in column.keys():
            key.append(k)
            value.append(u"%({})s".format(k))
        key = ", ".join(key)
        value = ", ".join(value)
        cursor.execute(u"INSERT INTO {} ({}) VALUES ({})".format(table, key, value), column)

    def execute(self, database, query):
        cursor = self.get_database(database).cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def commit(self, database):
        db = self.get_database(database)
        db.commit()
