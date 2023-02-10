



class FileModel(object):


    def __init__(self) -> None:
        
        super(FileModel, self).__init__()


        self.attr = {
            'file' : {
                'path' : None,
                'metadata' : {
                    'artist' : None,
                    'album' : None,
                    'contributing' : None,
                    'title' : None,
                    'codec' : None,
                    'bitrate' : None,
                    'cover' : None
                }
            }
        }