import os
import sys
import sqlite3
from sqlite3 import Error
from PyQt5.QtWidgets import QTableWidgetItem


class AppFunctions:
    def __init__(self):
        pass

    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        return conn

    def create_table(self, conn, create_table_sql):
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def create_tables(self, db_folder):
        create_user_table = """ CREATE TABLE IF NOT EXISTS Users (
        USER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USER_NAME TEXT,
        USER_EMAIL TEXT,
        USER_PHONE TEXT
        ); """

        conn = self.create_connection(db_folder)

        if conn is not None:
            self.create_table(conn, create_user_table)
        else:
            print("Error! Cannot create the database connection.")

    def get_all_users(self, db_folder):
        conn = self.create_connection(db_folder)

        get_all_users_query = """ SELECT * FROM Users; """

        try:
            c = conn.cursor()
            c.execute(get_all_users_query)
            return c.fetchall()
        except Error as e:
            print(e)

    def add_user(self, db_folder, user_name, email, phone_no):
        conn = self.create_connection(db_folder)

        insert_person_data_sql = f""" INSERT INTO Users (USER_NAME, USER_EMAIL, USER_PHONE) VALUES ('{user_name}', '{email}', '{phone_no}'); """

        try:
            cursor = conn.cursor()
            cursor.execute(insert_person_data_sql)
            conn.commit()
            print("User added successfully!")
        except Error as e:
            print("Error! Could not insert person data:", e)

    def display_users(self, table_widget, rows):
        table_widget.setRowCount(0)  # Clear the previous data

        for row_index, row_data in enumerate(rows):
            table_widget.insertRow(row_index)
            for col_index, item in enumerate(row_data):
                table_item = QTableWidgetItem(str(item))
                table_widget.setItem(row_index, col_index, table_item)

        # Set vertical header labels (IDs)
        table_widget.setVerticalHeaderLabels([str(row[0]) for row in rows])
