# -*- coding: utf-8 -*-


import sys
import os
import shutil
import logging

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




    def app_structure() -> dict:

        try:
            if controller.Model.EnvironmentModel.attr['system']['os'] == 'Windows':
                    
                app_path =\
                    os.getcwd() + '\\' + 'app'
                    

                controllers_path =\
                    app_path + '\\' + 'controllers'


                models_path =\
                    app_path + '\\' + 'models'


                views_path =\
                    app_path + '\\' + 'views'


                log_path =\
                        app_path + '\\' + 'log'


                log_file =\
                    log_path + '\\' + 'DEBUG.txt'
                
            elif controller.Model.EnvironmentModel.attr['system']['os'] == 'Linux':
                    
                app_path =\
                    os.getcwd() + '/' + 'app'
                    

                controllers_path =\
                    app_path + '/' + 'controllers'


                models_path =\
                    app_path + '/' + 'models'
                        

                views_path =\
                        app_path + '/' + 'views'
                    

                log_path =\
                        app_path + '/' + 'log'
                    

                log_file =\
                    log_path + '/' + 'DEBUG.txt'
            
            struct = {
                'app' : {
                    'path' : {
                        'app'           : app_path,
                        'controller'    : controllers_path,
                        'model'         : models_path,
                        'view'          : views_path,
                        'log'           : log_file
                    }
                }
            }

            return struct
        
        except Exception as exception:
            exceptions.append(exception)
        

    def clear_pycache(**struct) -> bool:

        try:
            
                
                
            pycache = '__pycache__'
                
            if os.path.exists(struct['app']['path']['app']):
                for obj in os.scandir(struct['app']['path']['controller']):
                    if obj.name == pycache:
                        shutil.rmtree(obj.path)
                    
                for obj in os.scandir(struct['app']['path']['model']):
                    if obj.name == pycache:
                        shutil.rmtree(obj.path)
                            
                for obj in os.scandir(struct['app']['path']['view']):
                    if obj.name == pycache:
                        shutil.rmtree(obj.path)
            
            return True
                    
        except Exception as exception:
            exceptions.append(exception)

            return False
    

    struct = app_structure()




    logger = logging.getLogger('logger')
    
    logging.basicConfig(
        filename = struct['app']['path']['log'],
        level = logging.DEBUG,
        encoding = 'utf-8',
        format = '%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt = '%Y-%m-%d %H:%M:%S',
    )

    log_formatter = logging.Formatter(fmt = '%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt= '%Y-%m-%d %H:%M:%S')


    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(log_formatter)

    logger.addHandler(console_handler)
    
    logger.debug('Logger instanciado.')
                



    pycache = clear_pycache(**struct)

    if pycache:
        controller.set_logger(logger)

        return controller.get_main_window()



if __name__ == '__main__':
    main()

    sys.exit(qApp.exec())