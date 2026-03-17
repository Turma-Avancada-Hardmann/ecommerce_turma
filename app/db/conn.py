from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = "postgresql://projeto_ecommerce_ep7y_user:X0Czq95MqDUkrVW3yQfHf5dZMjnHpTYc@dpg-d6s9gqhaae7s73d7ae70-a/projeto_ecommerce_ep7y"

engine = create_engine(DB_URL, pool_pre_ping=True)
Session = sessionmaker(bind=engine)
