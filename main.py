# -*- coding: utf-8 -*-


import sys
import os
import shutil
import platform


from PyQt5.QtWidgets import (
    QApplication
)


from app.controllers.controller import (
    Controller
)


exceptions = []

qApp = QApplication(sys.argv)


def main():
    
    try:
        controller = Controller()
    
    except Exception as exception:
        exceptions.append(exception)
        print(exceptions)
    
    def clear_pycache():
        if controller.Model.EnvironmentModel.attr['system']['os'] == 'Windows':
            
            app_path = os.getcwd() + '\\' + 'app'
            
            controllers_path = app_path + '\\' + 'controllers'
            models_path = app_path + '\\' + 'models'
            views_path = app_path + '\\' + 'views'
            
        
        elif controller.Model.EnvironmentModel.attr['system']['os'] == 'Linux':
            
            app_path = os.getcwd() + '/' + 'app'
            
            controllers_path =\
                app_path + '/' + 'controllers'

            models_path =\
                app_path + '/' + 'models'
                
            views_path =\
                app_path + '/' + 'views'
        
        
        pycache = '__pycache__'
        
        if os.path.exists(app_path):
            for obj in os.scandir(controllers_path):
                if obj.name == pycache:
                    shutil.rmtree(obj.path)
            
            for obj in os.scandir(models_path):
                if obj.name == pycache:
                    shutil.rmtree(obj.path)
                    
            for obj in os.scandir(views_path):
                if obj.name == pycache:
                    shutil.rmtree(obj.path)

    
    clear_pycache()
    
    return controller.get_main_window()



if __name__ == '__main__':
    main()

    sys.exit(qApp.exec())