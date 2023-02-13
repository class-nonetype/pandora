from app.controllers.controller import (
    
    # Class
    Controller,
    
    # Libraries
    os,
    
    # Functions
    get_path,
    get_logger,
    clear_project
    
)



execution_path = get_path(os.path.dirname(os.path.realpath(__file__)))

app_path = get_path(os.path.join(execution_path, 'app'))

if os.path.exists(app_path):
    
    models_path =\
        get_path(os.path.join(app_path, 'models'))

        
    controller_path =\
        get_path(os.path.join(app_path, 'controllers'))


    views_path =\
        get_path(os.path.join(app_path, 'views'))


    resources_path =\
        get_path(os.path.join(app_path, 'resources'))
    
    database_path =\
        get_path(os.path.join(app_path, 'database', 'local'))
    
    log_path =\
        get_path(os.path.join(app_path, 'log'))

    
    if not os.path.exists(database_path):
        os.mkdir(database_path)
    
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    
    
    logger = get_logger(log_path)
    
    
    clear_project(
        get_path,
        struct = {
            'execution' : execution_path,
            'controllers' : controller_path,
            'models' : models_path,
            'views' : views_path,
            'database' : get_path(os.path.join(app_path, 'database')),
            'functions' : get_path(os.path.join(models_path, 'functions')),
            'log' : log_path
        }
    )
    
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')


        Controller(
            logger,
            struct = {
                'controllers' : controller_path,
                'models' : models_path,
                'views' : views_path,
                'resources' : resources_path,
                'database' : database_path,
                'log' : log_path
            }
        ).get_main_view()
    except Exception as exception:
        
        logger.critical(
            msg = f'Exception : {exception}'
        )