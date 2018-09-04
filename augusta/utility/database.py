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

    # ------------------------------------ GENERIC DATABASE FUNCTIONS ---------------------------------

    def connect(self, database):
        """
        Connects to the specified database

        :param database: the database to connect to
        :return: True if the connection was successful. False if not
        """
        try:
            self.connection = sqlite3.connect(database)
            return True
        except sqlite3.Error as e:
            print("Connection failed.")
            print("Error:", e.args[0])
            return False

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
        Unsafe query executor. Used when query output doesn't matter

        Don't use this unless the query has been preprocessed.

        :param query: The query to be executed
        :return: (True, "Success") if the query executed fine. (False, "Message") otherwise
        """
        try:
            with self.connection:
                self.connection.execute(query)
        except sqlite3.Error as e:
            return (False, e.args[0])
        return (True, "Success")

    def execute_and_get(self, query):
        """
        Unsafe query executor. Used when query output matters.

        :param query: query to execute
        :return: Cursor object that was used to execute the query. None if query was unsuccessful
        """
        try:
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute(query)

                return cursor
        except sqlite3.Error as e:
            print("Error executing query: \n{}\n{}".format(query, e.args[0]))
            return None

    # ------------------------------------ BOT SPECIFIC FUNCTIONS -------------------------------------

    def user_known(self, slack_id):
        """
        Determines whether the user that issued the command is in the database

        :param slack_id: the user to check for
        :return: True if the user exists in the database. False otherwise
        """
        query = "SELECT * FROM users WHERE slack_id=\'{}\'".format(slack_id)
        cursor = self.execute_and_get(query)

        if cursor:
            rows = cursor.fetchall()
            if rows:
                if len(rows) > 1:
                    raise Exception("Excuse me what the fuck. Duplicate Slack IDs are NOT A THING.")
                return True

        return False

    def add_user(self, slack_id, first = "", last = "", student_id = ""):
        """
        Adds the user's Slack ID to the user's information

        - Checks for Last, First name match
        - Checks for Student ID if duplicate names

        :param slack_id:        the Slack ID to pair the user with
        :param first:           the user's first name
        :param last:            the user's last name
        :param student_id:      the user's student ID
        :return (True, "Success") if user was added successfully. (False, "Message") otherwise.
        """
        query = "UPDATE users SET slack_id=\'{}\' WHERE ".format(slack_id)
        if student_id:
            return self.execute(query + "sid=\'{}\'".format(student_id))

        if first and last:
            cursor = self.execute_and_get("SELECT * FROM users WHERE first=\'{}\' AND last=\'{}\'".format(first, last))
            if cursor:
                rows = cursor.fetchall()
                if len(rows) > 1:
                    return (False, "Multiple users with the same name.")

                return self.execute(query + "first=\'{}\' AND last=\'{}\'".format(first, last))
            else:
                return (False, "Query failed.")