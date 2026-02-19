from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = "mysql+mysqlconnector://root:Felipe2015%23@localhost:3306/loja_hardmann"

engine = create_engine(DB_URL, pool_pre_ping=True)
Session = sessionmaker(bind=engine)
