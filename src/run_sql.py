from sqlalchemy.orm import sessionmaker
from main import engine
from main import Case

Session = sessionmaker(bind=engine)
session = Session()

args = {
    "name" : "name2",
    "no" : "no2",
    "des" : "des2",
    "pre" : "pre2",
    "step" : "step2",
    "auto_type" : "auto_type2",
    "platform" : "platform2",
    "test_env_type" : "env_type2",
    "env_topo" : "env_topo2",
}
case = Case(**args)

session.add(case)
session.commit()
