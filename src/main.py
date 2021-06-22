from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///testcase.db', echo=False)

Base = declarative_base()

class Case(Base):
    __tablename__ = 'case'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    no = Column(String(32))
    level = Column(String(32))
    des = Column(String(32))
    pre = Column(String(32))
    step = Column(String(32))
    auto_type = Column(String(32))
    platform = Column(String(32))
    test_env_type = Column(String(32))
    env_topo = Column(String(32))

    def __repr__(self):
        res = "<User(id = {}, name = {}, no = {}, level = {}, des = {}, pre = {}, step = {}, auto_type = {}, platform = {}, test_env_type = {}, env_topo = {})>".format(
            self.id, self.name, self.no, self.level, self.des, self.pre, self.step, self.auto_type, self.platform, self.test_env_type, self.env_topo)
        return res


Case.__table__

Base.metadata.create_all(engine, checkfirst=True)
