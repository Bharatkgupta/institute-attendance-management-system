# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:05:28 2019

@author: vishal
"""
import tkinter
import datetime
import re
from functools import partial
from dbcreate import *
from tk2 import *
def addCourse():
    addCourseWin = tkinter.Tk()
    addCourseWin.title("Add a course")

 
    global addCourseLabel
 
    addCourseLabel = tkinter.StringVar()
 
    global addCourseEntry
   
    tkinter.Label(addCourseWin, text="Course : ").pack()
    
    addCourseEntry = tkinter.Entry(addCourseWin)
    addCourseEntry.pack()
    
    #print(addCourseEntry.get()
    addCourseLabel = addCourseEntry
    
    tkinter.Label(addCourseWin, text="").pack()
    
    tkinter.Button(addCourseWin, text="Submit", width=10, height=1, command = checkAdd).pack()
    

    
def checkAdd():
    print(addCourseLabel.get())
    addcoursefac(addCourseLabel.get(),usernames)

def viewCourse():
    viewWin = tkinter.Tk()
    viewWin.title("Your courses")
    courseList = getcoursesfac(usernames)
    for i in courseList:
        var = tkinter.Button(viewWin, text=i, command=partial(facAttendance,i), bg='gray', fg='white', height="2", width="25")
        var.pack()

def submitBtn(i):

    
    print(fromDate.get(),toDate.get())
    date1 = fromDate.get().split('/')
    date2 = toDate.get().split('/')
    
    x = datetime.date(int(date1[2]),int(date1[1]),int(date1[0]))
    y = datetime.date(int(date2[2]),int(date2[1]),int(date2[0]))
    
    madattendance(x,i,y) #x - the from date and y - to date . course = name of course whose attendance we're seeing

def facAttendance(course):
    attWin = tkinter.Tk()
    attWin.title(course)
    
    global fromDate
    global toDate
    
    global tbFrom
    global tbTo
    
    fromDate = tkinter.StringVar()
    toDate = tkinter.StringVar()

    fDt = tkinter.Label(attWin, text = "Enter front date in the following textbox as (d/m/y)")
    fDt.pack()
    
    tbFrom = tkinter.Entry(attWin)
    tbFrom.pack()
    fromDate = tbFrom
    
    tDt = tkinter.Label(attWin, text = "Enter to date in the following textbox as (d/m/y)")
    tDt.pack()
    
    tbTo = tkinter.Entry(attWin)
    tbTo.pack()
    toDate = tbTo
    
    
    submit = tkinter.Button(attWin, text='Submit',
        command=partial(submitBtn,course), bg='red', fg='white', height="2", width="25")
    submit.pack()
        

def faculty(usernames1):
    global usernames
    usernames=usernames1
    mainWin = tkinter.Tk()
    mainWin.title("Faculty Window")
    
    hello = tkinter.Label(mainWin, text='Faculty')
    hello.pack()
    
    viewBtn = tkinter.Button(mainWin, text='View courses',
        command=viewCourse, bg='red', fg='white', height="2", width="25")
    viewBtn.pack()
    courses = tkinter.Button(mainWin, text='Add course',
        command=addCourse, bg='red', fg='white', height="2", width="25")
    courses.pack()
    
#=================================student part=================================
    
    
def stuAttendance():
    stuAttWin = tkinter.Tk()
    stuAttWin.title("Viewing attendance")


def stuCourse():
    stuCourseWin = tkinter.Tk()
    stuCourseWin.title("courses")
    allCourses = getallcourses() #get all courses here and remove the next list   
    for i in allCourses:
        cBtn = tkinter.Button(stuCourseWin, text=i,command=partial(addStuCourse), bg='lightblue', fg='black', height="2", width="25")
        cBtn.pack()

def addStuCourse():
    addstuCourseWin = tkinter.Tk()
    addstuCourseWin.title("Add a course")

    global addstuCourseLabel
 
    addstuCourseLabel = tkinter.StringVar()
 
    global addstuCourseEntry
   
    tkinter.Label(addstuCourseWin, text="Course : ").pack()
    
    addstuCourseEntry = tkinter.Entry(addstuCourseWin)
    addstuCourseEntry.pack()
    #print(addCourseEntry.get()
    addstuCourseLabel = addstuCourseEntry
    
    tkinter.Label(addstuCourseWin, text="").pack()
    
    tkinter.Button(addstuCourseWin, text="Submit", width=10, height=1, command = checkstuAdd).pack()


def checkstuAdd():
    print(addstuCourseLabel.get())
    if (addstuCourseLabel.get() in getallcourses()):
    	addcoursestud(usernames,addstuCourseLabel.get()) #update daatabase function here
    else:
    	print("No course yet")


def searchFunc():
    pass    

def student(usernames1):
    global usernames
    usernames=usernames1
    stuMain = tkinter.Tk()
    stuMain.title("Student Window")
    
    stu = tkinter.Label(stuMain, text='Student')
    stu.pack()
    
    cBtn = tkinter.Button(stuMain, text='Select Courses',command=stuCourse, bg='red', fg='white', height="2", width="25")
    cBtn.pack()
    
    csBtn = tkinter.Button(stuMain, text='Add Courses',command=addStuCourse, bg='red', fg='white', height="2", width="25")
    csBtn.pack()

    att = tkinter.Button(stuMain, text='My Attendance',command=stuAttendance, bg='red', fg='white', height="2", width="25")
    att.pack()
    
    search = tkinter.Button(stuMain, text='Search', command=searchFunc, bg='red', fg='white', height='2', width='25')
    search.pack()



#to rithvik : add that thing from database isFaculty == 0 => then call student() or else faculty() above



