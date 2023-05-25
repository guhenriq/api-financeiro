from typing import Type
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = 'sqlite:///db.sqlite'
        self.session = None

    def get_engine(self) -> Type[Engine]:
        """
        Return engine database connection
        """
        engine = create_engine(self.__connection_string)
        return engine
    
    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()