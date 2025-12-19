from sqlalchemy import create_engine, text, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
engine = create_engine('mysql+pymysql://root:parsa1386@localhost')
with engine.connect() as conn:
    conn.execute(text('CREATE DATABASE IF NOT EXISTS student_db'))
engine = create_engine('mysql+pymysql://root:parsa1386@localhost/student_db')
Base = declarative_base()
Robotfactory = sessionmaker(bind=engine)
parsa = Robotfactory()
class Student(Base):
    __tablename__ = 'Students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(50), nullable=False)
    Last_name = Column(String(50), nullable=False)
    Score = Column(Float, nullable=False)
Base.metadata.create_all(engine)