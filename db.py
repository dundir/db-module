from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
import models
from sqlalchemy.orm import sessionmaker


class data:
  ''' Variables
      self.dbname
      self.engine
      self.session
  '''
  def __init__(self,dbname = 'temp.db'):
      self.engine = create_engine('sqlite:///' + dbname, echo = True)
      self.dbname = dbname

  def connect(self):
      print('Connecting to: ' + 'sqlite:///' + self.dbname)
      Base.metadata.create_all(self.engine)

  def session(self):
      Session = sessionmaker(bind = self.engine)
      self.session = Session()
