
from app.models.database import (
    DatabaseModel
)

from app.models.environment import (
    EnvironmentModel
)

from app.models.file import (
    FileModel
)



class Model(object):

    def __init__(self, Controller) -> None:
        super(Model, self).__init__()
        self.Controller = Controller

        self.EnvironmentModel = EnvironmentModel(self.Controller)
        self.EnvironmentModel.create_storage_directory()
        self.EnvironmentModel.create_scripts_directory()
        self.EnvironmentModel.create_local_database()

        self.DatabaseModel = DatabaseModel(self.Controller)
        self.DatabaseModel.set_local_database(
            self.EnvironmentModel.attr['path']['storage']['local']
        )

        self.FileModel = FileModel()
