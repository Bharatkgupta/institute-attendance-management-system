from sqlalchemy import Column,Integer, String, Float,Date, Boolean, create_engine, exc, orm, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base=declarative_base()
class Login(Base):
	__tablename__="login"
	user=Column(String(10), primary_key=True)
	password=Column(String(10))
	isfaculty=Column(Integer)
	def __init__(self,user,password,isfaculty):
		self.user= user
		self.password= password
		self.isfaculty= isfaculty
	def __str__(self):
		return self.user+"|"+self.password+"|"+str(self.isfaculty)

class Faculty(Base):
	__tablename__="faculty"
	cname=Column(String(10), primary_key=True)
	fac=Column(String(10))
	def __init__(self,cname,fac):
		self.cname= cname
		self.fac= fac
	def __str__(self):
		return self.cname+"|"+self.fac


class Perc(Base):
	__tablename__="perc"
	studname=Column(String(10), primary_key=True)
	course=Column(String(10), primary_key=True)
	perc=Column(String(10))
	def __init__(self,studname,course,perc):
		self.studname= studname
		self.course= course
		self.perc= perc
	def __str__(self):
		return self.studname+"|"+self.course+"|"+str(self.perc)

class Stud(Base):
	__tablename__="stud"
	studname=Column(String(10), primary_key=True)
	courses=Column(String(10), primary_key=True)	
	def __init__(self,studname,courses):
		self.studname= studname
		self.courses= courses
	def __str__(self):
		return self.studname+"|"+self.courses


class Attend(Base):
	__tablename__="attend"
	studname=Column(String(10), primary_key=True)
	course=Column(String(10), primary_key=True)	
	date=Column(Date, primary_key=True)
	present=Column(Integer)
	def __init__(self,studname,courses,date,present):
		self.studname= studname
		self.course= courses
		self.date= date
		self.present= present
	def __str__(self):
		return self.studname+"|"+self.course+"|"+str(self.date)+"|"+str(self.present)


def addlogin(name,password,isfaculty):
	engine=create_engine("sqlite:///as1.db")
	engine.connect()
	session= sessionmaker(bind=engine)()
	userrow = Login(name,password,isfaculty)
	session.add(userrow)

	session.commit()


def displogin():
	engine=create_engine("sqlite:///as1.db")
	engine.connect()
	session= sessionmaker(bind=engine)()
	result=[r for r in session.query(Login).all()]
	list1=[]
	for i in result:
		list1.append((i.user,i.password,i.isfaculty))
	return list1


def check(uname,password):
	engine=create_engine("sqlite:///as1.db")
	engine.connect()
	session= sessionmaker(bind=engine)()
	result=[r for r in session.query(Login).all()]
	list1=[]
	usernotthere=True
	match=False	
	for i in result:
		if i.user==uname:
			usernottthere=False
		if i.user==uname and i.password==password:
			match=True
	if(match==True and usernottthere==False):
		return 0
	elif(usernotthere==False and match==False):
		return 2
	else:
		return 1
				

def getstudforcourses(cname):
	engine=create_engine("sqlite:///as1.db")
	engine.connect()
	session= sessionmaker(bind=engine)()
	result=[r for r in session.query(Stud).all()]
	list1=[]
	for i in result:
		if(i.courses==cname):
			list1.append(i.studname)
	print(list1)
	return list1


def inserperc(studname,course,perc):
	engine=create_engine("sqlite:///as1.db")
	engine.connect()
	session= sessionmaker(bind=engine)()
	userrow = Perc(studname,course,perc)
	session.add(userrow)
	try:
		session.commit()
	except:
		print("Try Again")
		session.rollback()


def getpercrows():
	engine=create_engine("sqlite:///as1.db")
	engine.connect()
	session= sessionmaker(bind=engine)()
	result=[r for r in session.query(Perc).all()]
	list1=[]
	for i in result:
		if(i.perc<85):
			list1.append((i.user,i.password,i.isfaculty))
	return list1


def dispfaculty():
	engine=create_engine("sqlite:///as1.db")
	engine.connect()
	session= sessionmaker(bind=engine)()

	result=[r for r in session.query(Faculty).all()]
	for i in result:
		print(i)
def displogpar(name,password):
	engine=create_engine("sqlite:///as1.db")
	engine.connect()
	session= sessionmaker(bind=engine)()
	result=[r for r in session.query(Login).all()]
	for i in result:
		if(i.user==name and i.password==password):
			return(i.user,i.password,i.isfaculty)

def markattendance(name,courses,date):
	engine=create_engine("sqlite:///as1.db")
	engine.connect()
	session= sessionmaker(bind=engine)()
	result=[r for r in session.query(Attend).all()]
	presentss=False
	for i in result:
		if(i.studname==name and i.course==courses and i.date==date):
			if(i.present==0):
				i.present=1
			else:
				i.present=0
			try:
				session.commit()
			except:
				print("Try Again")
				session.rollback()			
			presentss=True
	if(presentss==False):
		userrow = Attend(name,courses,date,1)
		session.add(userrow)
		try:
			session.commit()
		except:
			print("Try Again")
			session.rollback()
			

def checkattend(name,course,date):
	engine=create_engine("sqlite:///as1.db")
	engine.connect()
	session= sessionmaker(bind=engine)()
	result=[r for r in session.query(Attend).all()]
	list1=[]
	for i in result:
		if(i.studname==name and i.course==course and i.date==date):
			return(i.present)
	return 0



def getcoursesfac(fac):
	engine=create_engine("sqlite:///as1.db")
	engine.connect()
	session= sessionmaker(bind=engine)()
	result=[r for r in session.query(Faculty).all()]
	list1=[]
	for i in result:
		if(i.fac==fac):
			list1.append(i.cname)
	return list1

def getallcourses():
	engine=create_engine("sqlite:///as1.db")
	engine.connect()
	session= sessionmaker(bind=engine)()
	result=[r for r in session.query(Faculty).all()]
	list1=[]
	for i in result:
		list1.append(i.cname)
	return list1


def addcoursefac(cname,fac):
	engine=create_engine("sqlite:///as1.db")
	engine.connect()
	session= sessionmaker(bind=engine)()
	userrow = Faculty(cname,fac)
	session.add(userrow)
	try:
		session.commit()
	except:
		print("Try Again")
		session.rollback()



def addcoursestud(studname,courses):
	engine=create_engine("sqlite:///as1.db")
	engine.connect()
	session= sessionmaker(bind=engine)()
	userrow = Stud(studname,courses)
	session.add(userrow)
	try:
		session.commit()
	except:
		print("Try Again")
		session.rollback()


"""
import datetime
def addstock():
	print("Enter Stock Name")
	stkname=input()
	print("Enter Day")
	day=int(input())
	print("Enter Month")
	mon=int(input())
	print("Enter Year")
	yr=int(input())	
	dt=datetime.datetime(yr,mon,day)
	print("Enter Highest Price")
	hp=float(input())
	print("Enter Lowest Price")
	lp=float(input())
	print("Enter Base Price")
	bp=float(input())
	print("Enter Ending Price")
	ep=float(input())
	stockrow=Stock(stkname,dt,hp,lp,bp,ep)
	session.add(stockrow)
	try:
		session.commit()
	except:
		print("Already present in table")
		session.rollback()


def sell():
	flag=0
	while(flag==0):
		print("Enter Seller Name")
		seller=input()
		print("Enter Buyer Name")		
		buyer=input()
		print("Enter Stock")		
		stkname=input()
		print("Enter Number")		
		no=int(input())				
		print("Enter Price")		
		price=float(input())
		print("Enter Day")
		day=int(input())
		print("Enter Month")
		mon=int(input())
		print("Enter Year")
		yr=int(input())	
		dt=datetime.date(yr,mon,day)
		result=[r for r in session.query(Stock).all()]
		#Checking if selling price greater than lowest and lesser than highest price for the day		
		xlp=-100000
		yhp=100000		
		for i in result:
			if(i.date==dt and i.name==stkname):
				xlp=i.lp
				yhp=i.hp
				break
		if price < xlp or price > yhp :
			print("Wrong Price")
			break;
		result=[r for r in session.query(Portfolio).all()]
		#Checking if sellers portfolio has enough stocks		
		for i in result:
			if(i.pfname==seller and i.stk==stkname):
				sellerobj=i		
				nos=i.no
				break

		if no >nos:
			print("No sufficient stocks")
			break
		result=[r for r in session.query(Portfolio).all()]
		#To Check if buyer already had some stocks
		exist=False
		for i in result:
			if(i.pfname==buyer and i.stk==stkname):
				buyerobj=i
				exist=True
				break
		
		stockrow=Record(seller,stkname,no,price,dt)
		session.add(stockrow)
		session.commit()


		setattr(sellerobj,'no', sellerobj.no-no)
		session.commit()
		
		if(exist==True):  #You need to update buyers stocks
			setattr(buyerobj,'no', buyerobj.no+no)
		else:		
			stockrow=Portfolio(buyer,stkname,no)
			session.add(stockrow)
			try:
				session.commit()
			except:
				print("Try Again")
				session.rollback()
		flag=1

def dispuser():
	result=[r for r in session.query(Users).all()]
	for i in result:
		print(i)

def dispstock():
	result=[r for r in session.query(Stock).all()]
	for i in result:
		print(i)


def dispport():
	result=[r for r in session.query(Portfolio).all()]
	for i in result:
		print(i)

def disprecord():
	result=[r for r in session.query(Record).all()]
	for i in result:
		print(i)

def highest():
	print("Enter Stock")
	stk=input()	
	print("LOWER BOUND")
	print("Enter Day")
	day=int(input())
	print("Enter Month")
	mon=int(input())
	print("Enter Year")
	yr=int(input())	
	dt1=datetime.date(yr,mon,day)
	print("UPPER BOUND")
	print("Enter Day")
	day=int(input())
	print("Enter Month")
	mon=int(input())
	print("Enter Year")
	yr=int(input())	
	dt2=datetime.date(yr,mon,day)
	result=[r for r in session.query(Stock).all()]
	listprices=[]
	for i in result:
		if i.date>dt1 and i.date<dt2:
			listprices.append(i.hp)
	print("MAXIMUM PRICE IS:",max(listprices))
	
#This function is just to initialize stocks for some people as we assume theres no bank and only trading between users
def give():
	print("Enter Name")
	name=input()
	print("Enter Stock")
	stks=input()
	print("Enter Number")
	nos=int(input())
	result=[r for r in session.query(Portfolio).all()]
	exist=False
	#Check if already has some stocks
	for i in result:
		if(i.pfname==name and i.stk==stks):
			exist=True
			break
	if(exist!=True):  #You need to update buyers stocks
		stockrow=Portfolio(name,stks,nos)
		session.add(stockrow)
		try:
			session.commit()
		except:
			print("Try again")
			session.rollback()

while True:
	print("1: Add User\n2: Add Stock Prices\n3: Sell Stock\n4: Display User\n5: Display Stock\n6: Display Portfolios\n7: Display Records\n8: Highest and Lowest\n9: Give Stocks\n10: Exit")
	ans=int(input())
	if(ans==1):
		adduser()
	elif(ans==2):
		addstock()
	elif(ans==3):
		sell()
	elif(ans==4):
		dispuser()
	elif(ans==5):
		dispstock()
	elif(ans==6):
		dispport()
	elif(ans==7):
		disprecord()
	elif(ans==8):
		highest()
	elif(ans==9):
		give()
	else:
		break
"""
