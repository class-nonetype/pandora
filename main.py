# -*- coding: utf-8 -*-


import sys
import os
import shutil
import logging
import platform




from app.controllers.controller import (
    Controller
)




def get_logger() -> logging.Logger:

    global Logger

    Logger = logging.getLogger('Logger')

    if platform.system() == 'Windows':
        log_file = struct['app']['path']['log'] + '\\' + 'DEBUG.txt'

    elif platform.system() == 'Linux':
        log_file = struct['app']['path']['log'] + '/' + 'DEBUG.txt'

    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        encoding='utf-8',
        format='%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )

    log_formatter = logging.Formatter(
        fmt='%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(log_formatter)

    Logger.addHandler(console_handler)

    Logger.info('Logger instanciado.')

    return Logger


def get_app_structure() -> dict:

    global struct

    if platform.system() == 'Windows':

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

    elif platform.system() == 'Linux':

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
        'app': {
            'path': {
                'app': app_path,
                'controller': controllers_path,
                'model': models_path,
                'view': views_path,
                'log': log_path
            }
        }
    }

    for directory in struct['app']['path'].values():

        if not os.path.exists(directory):
            os.mkdir(directory)

    return struct


def get_controller(Logger) -> Controller:
    try:
        controller = Controller(Logger)

        return controller

    except Exception as exception:
        Logger.warning(
            f'Exception\t{exception}'
        )


def main():

    struct = get_app_structure()

    Logger = get_logger()

    try:
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
                Logger.warning(
                    msg=f'Exception\t{exception}'
                )
                return False

        Controller = get_controller(Logger)

        cleaner = clear_pycache(**struct)

        if cleaner:
            return Controller.execute()

    except Exception as exception:

        Logger.warning(
            msg=f'Exception\t{exception}'
        )


if __name__ == '__main__':
    sys.exit(main())
