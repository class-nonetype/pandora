from app.models.modules import (
    Database,
    
    get_path
)

import os




class Model(object):

    def __init__(self, Controller, **struct) -> None:
        super(Model, self).__init__()
        self.Controller = Controller
        
        self.struct = struct

        
        self.Database = Database(self.Controller)
        self.Database.set_local_database(
            get_path(os.path.join(self.struct['struct']['database'], 'storage.db'))
        )
        

        

