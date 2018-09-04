"""
Manages the database for all of Augusta's users
"""

import sqlite3
import csv
import os

class Database(object):
    """
    Object used to abstract away the underlying SQLite database of users and their information
    """

    def __init__(self):
        self.connection = None

    def connect(self, database):
        """
        Connects to the specified database

        :param database: the database to connect to
        :return: None
        """
        try:
            self.connection = sqlite3.connect(database)
        except sqlite3.Error as e:
            print("Connection failed.")
            print("Error:", e.args[0])

    def disconnect(self):
        """
        Closes the connection that was previously connected to

        :return: None
        """
        try:
            self.connection.close()
        except sqlite3.Error as e:
            print("Connection failed to close...")
            print("Error: ", e.args[0])

    def create_table(self, table, **kwargs):
        """
        Creates a table in the DB

        :param table:   The name of the table
        :param kwargs:  The column information in the form (name, ATTRB). ATTRB can dictate any attribute of the column
        :return: (True, "Success") if the table was created successfully. (False, "Message") if otherwise
        """
        query = "CREATE TABLE {name} (".format(name=table)
        for (name, attrb) in kwargs.items():
            query += "{} {},".format(name, attrb)
        query = query[:-1] + ')'

        return self.execute(query)

    def drop_table(self, table):
        """
        Drops a specified table in the DB

        :param table: the table that needs dropping
        :return: None
        """
        query = "DROP TABLE {}".format(table)

        return self.execute(query)

    def insert(self, table, *data):
        """
        Inserts the specified data into the table
        :param table:   the table to insert data into
        :param data:    the data
        :return: (True, "Success") if insertion was successful. (False, "Message") if not. Raises an exception if
        data already exists
        """
        query = "INSERT INTO {table} VALUES (".format(table=table)
        for value in data:
            query += "\'{}\',".format(value)
        query = query[:-1] + ')'

        return self.execute(query)

    def execute(self, query):
        """
        Unsafe query executor. Don't use this unless the query has been preprocessed.

        :param query: The query to be executed
        :return: (True, "Success") if the query executed fine. (False, "Message) otherwise
        """
        try:
            with self.connection:
                self.connection.execute(query)
        except sqlite3.Error as e:
            return (False, e.args[0])
        return (True, "Success")