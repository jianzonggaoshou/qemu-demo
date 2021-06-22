from sqlalchemy.orm import sessionmaker
from main import engine
from main import Case

Session = sessionmaker(bind=engine)
session = Session()

case = session.query(Case)
print(case.all())