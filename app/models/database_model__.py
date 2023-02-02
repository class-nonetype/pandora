import os
import pandas as pd


from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5 import QtSql
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QTableWidgetItem,  QPushButton
from PyQt5.QtCore import Qt



class DatabaseModel(object):
    def __init__(self, Controller):

        super(DatabaseModel, self).__init__()

        self.Controller = Controller
        
    def set_local_database(self, database_path : str) -> bool:
        service = 'QSQLITE'
        status = False

        try:
            self.connection = QSqlDatabase.addDatabase(service)
            self.connection.setDatabaseName(database_path)

            if not self.connection.open():
                return status

            status = True
            return status

        except Exception as exc:
            print(exc)
        
    def close_local_connection(self):
        self.Controller.View.MainWindowView.ModelItemListViewPlaylist.setRowCount(0)

        return self.connection.close()
    
    def load_tables(self):

        self.ModelItemListViewPlaylist = QtGui.QStandardItemModel()
        self.Controller.View.MainWindowView.listViewPlaylist.setModel(self.ModelItemListViewPlaylist)
        self.Controller.View.MainWindowView.listViewPlaylist.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            
        for table in self.connection.tables():
            item = QtGui.QStandardItem(table)
            self.ModelItemListViewTables.appendRow(item)
        #self.Controller.View.MenuWindowView.PushButtonCloseConnection.setEnabled(True)
        self.Controller.View.MainWindowView.listViewPlaylist.doubleClicked.connect(self.list_table)

    def list_table(self, index):
        try:
            self.table = self.ModelItemListViewPlaylist.itemFromIndex(index)
            self.table = self.table.text()

            self.load_data()
            
        except Exception as exc:
            print(exc)

    
    def save_status(self):
        return self.connection.commit()

    def execute_query(self, query):

        if 'SELECT' in query:
            _queryModel = QSqlQueryModel()
            _queryModel.setQuery(query)

            self.Controller.View.MenuWindowView.tableViewAnalysis.setModel(_queryModel)
        
        else:
            _query = QSqlQuery(query)
            _query.exec_()

        self.save_status()
    
        return
    
    def delete_data(self, column, selected_data):
        status = False


        try:
            _query = QSqlQuery(f'DELETE FROM {self.table} WHERE {column} = "{selected_data}"')
            _query.exec_()
            self.saveStatus()
            self.loadData()
            status = True
            
        except Exception as exc:
            print(exc)
        
        finally:
            if status:
                print(status)


    def _add_data(self):
        status = False

        tables = self.connection.database().tables()
        
        def get_columns(tables):
            columns = str(tables).replace('[', '')
            columns = str(columns).replace(']', '')
            columns = str(columns).replace("'", '')
            return columns
        
        def get_values():

            columnCount = self.Controller.View.MenuWindowView.tableViewAnalysis.model().columnCount()
            values = []

            for value in range(columnCount):
                value = 'None'
                values.append(value)

            values = str(values).replace('[', '')
            values = str(values).replace(']', '')
            #values = str(values).replace("'", '"')

            return values

        try:
            #columns = getColumns(tables)
            #values = getValues()


            row_position = self.Controller.View.MainWindowView.listViewPlaylist.model().rowCount()
            self.Controller.View.MenuWindowView.tableViewAnalysis.model().insertRow(row_position)


            _model = QtSql.QSqlTableModel(self.Controller.View.MenuWindowView.tableViewAnalysis, self.Connection)
            _model.setTable(self.table)
            _model.select()

            self.saveStatus()
            #self.loadData()

            #print(f'''INSERT INTO {self.table} VALUES ({values})''')
            #_query = QSqlQuery(f'''INSERT INTO {self.table} VALUES ({values});''')
            #_query.exec_()


            status = True

            
        except Exception as exc:
            print(exc)
        
        finally:
            if status:
                print(status)


    def add_data(self, table : str, name : str, data : str):
        try:
            time = '!'

            if table == 'playlist':

                query = QSqlQuery("INSERT INTO playlist (name, file_path) VALUES (:name, :file_path)")
                query.addBindValue(name)
                query.addBindValue(data)
                print("INSERT INTO playlist (name, file_path) VALUES (:name, :file_path)")
                query.exec_()

                self.connection.commit()
        
        except Exception as exc:
            print(exc)
            pass

    def importData(self, dataRow : list):
        row = str(dataRow).replace('[', '')
        row = str(row).replace(']', '')



        _query = QSqlQuery(f'''INSERT INTO {self.table} VALUES({row})''')
        _query.exec_()
        print(f'''INSERT INTO {self.table} VALUES({row})''')
        self.saveStatus()



        _model = QtSql.QSqlTableModel(self.Controller.View.MenuWindowView.tableViewAnalysis, self.Connection)
        _model.setTable(self.table)
        _model.select()

        self.loadData()
    
    def load_data(self):
        _ModelTable = QSqlTableModel(self.Controller.View.MenuWindowView.tableViewAnalysis, self.connection)
        _ModelTable.setTable(self.table)
        _ModelTable.select()

        if _ModelTable.canFetchMore():
            _ModelTable.fetchMore()
            self.Controller.View.MenuWindowView.tableViewAnalysis.setModel(_ModelTable)
        else:
            self.Controller.View.MenuWindowView.tableViewAnalysis.setModel(_ModelTable)

        self.Controller.View.MenuWindowView.tableViewAnalysis.resizeColumnsToContents()
    
