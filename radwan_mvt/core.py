from .wsgi import WsgiServer
import os, json

class Server:

    def __init__(
            self,
            URLS:dict={},
            APPS_LIST:list=[],
            TEMPLATES_FOLDER_NAME:str='templates',
            STATIC_FOLDER_NAME:str='static',
            db_conf:dict={},
    ) -> None:
        
        CURRENT_PATH = os.environ.get('CURRENT_PATH')
        
        TEMPLATES_FOLDER_NAME = os.path.join(CURRENT_PATH, TEMPLATES_FOLDER_NAME)
        STATIC_FOLDER_NAME = os.path.join(CURRENT_PATH, STATIC_FOLDER_NAME)
        
        self.URLS = URLS
        os.environ.setdefault('TEMPLATE_FOLDER', TEMPLATES_FOLDER_NAME)
        os.environ.setdefault("STATIC_FODLER", STATIC_FOLDER_NAME)
        # os.environ.setdefault("URLS", json.dumps(URLS))

        self.APPS_LIST = APPS_LIST
        # self.TEMPLATE_FOLDER_NAME = os.path.join(CURRENT_PATH, TEMPLATE_FOLDER_NAME)
        # self.STATIC_FOLDER_NAME = os.path.join(CURRENT_PATH, STATIC_FOLDER_NAME)
        self.db_conf = db_conf


    def run (self, host='localhost', port=8080) : 
        self.host = host
        self.port = port
        WsgiServer(host, port)
        

    def get_host(self) : 
        return f"http://{self.host}:{self.port}"
