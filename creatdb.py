from sqlalchemy import Column,Integer, String, Float,Date, Boolean, create_engine, exc, orm, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine=create_engine("sqlite:///as1.db")
engine.connect()
session= sessionmaker(bind=engine)()

meta = MetaData()

stock = Table(
	'login', meta, 
	Column('user', String(10), primary_key = True),	
	Column('password', String(10), primary_key=True), 
	Column('isfaculty', Integer),
)

portfolio=Table(
	'faculty', meta, 
	Column('cname', String(10), primary_key = True),	
	Column('fac', String(10)),
)


record=Table(
	'stud', meta, 
	Column('studname', String(10), primary_key = True),	
	Column('courses', String(10), primary_key=True),  
)


users = Table(
   'attend', meta,
	Column('studname', String(10), primary_key = True), 
	Column('course', String(10), primary_key = True), 
	Column('date', Date, primary_key = True), 
	Column('present', Integer), 
)




perc = Table(
   'perc', meta,
	Column('studname', String(10), primary_key = True), 
	Column('course', String(10), primary_key = True), 
	Column('perc', Float),  
)







meta.create_all(engine)

