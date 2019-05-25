from sqlalchemy import create_engine
#from sqlalchemy.ext.declarative import declarative_base
from models import Base
from sqlalchemy.orm import sessionmaker


class ConnectionManager:
  ''' Variables
      self.dbname
      self.engine
  '''
  def __init__(self,dbname = 'temp.db'):
      self.engine = create_engine('sqlite:///' + dbname, echo = True)
      self.dbname = dbname

  def connect(self):
      print('Connecting to: ' + 'sqlite:///' + self.dbname)
      Base.metadata.create_all(self.engine)


class SessionManager():
    def __init__(self,ConnectionManager):
        Session = sessionmaker(bind=ConnectionManager.engine)
        self.session = Session()
