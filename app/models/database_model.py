import os
import pandas as pd


from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5 import QtSql
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QTableWidgetItem,  QPushButton
from PyQt5.QtCore import Qt

import sqlite3

class DatabaseModel(object):
    def __init__(self, Controller):

        super(DatabaseModel, self).__init__()

        self.Controller = Controller
        
    def set_local_database(self, path : str):

        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()

        return self.connection, self.cursor
    

    def insert_data(self, query : str, parameters : tuple):

        self.cursor.execute(query, parameters)
        self.connection.commit()
    
    def get_id(self):
        try:
            self.cursor.execute('SELECT max(id) FROM playlist')

            for parameter in self.cursor.fetchall():
                
                id_ = int(parameter[0])
                id_+=1

                return id_
        
        except Exception as exception:
            print(exception)
            pass
