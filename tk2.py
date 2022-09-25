import tkinter as tk
import datetime
from dbcreate import *
from functools import partial

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)

def gr(x,course,y,i,j):
	markattendance(x,course,y)
	col=checkattend(x,course,y)
	print(x,course,y,col)
	if col == 0:
		tk.Button(main_screen, width=10, height=1,bg="red", command = partial(gr,x,course,y,i,j)).grid(row=i,column=j)
	elif col==1:
		tk.Button(main_screen, width=10, height=1,bg="green", command = partial(gr,x,course,y,i,j)).grid(row=i,column=j) 	


def func(x,course,y,i,j):
	col=checkattend(x,course,y)
	if col == 0:
		return "red"
	elif col==1:
		return "green"
def madattendance(x,course,y):
	global main_screen
	main_screen = tk.Tk()
	main_screen.geometry("400x200")
	s=getstudforcourses(course)
	date1=x
	date2=y
	students=[i for i in daterange(date1,date2)]
	students.insert(0,"")
	s.insert(0,"")	
	height=len(s)
	width=len(students)
	for i in range(height): 
		for j in range(width):
			if i==0:
				tk.Button(main_screen,text=students[j], width=10, height=1).grid(row=i,column=j)
			elif j==0:
				tk.Button(main_screen,text=s[i], width=10, height=1).grid(row=i,column=j)
			else:
				tk.Button(main_screen, width=10, height=1,bg=func(s[i],course,students[j],i,j),command = partial(gr,s[i],course,students[j],i,j)).grid(row=i,column=j)
	tk.mainloop()
