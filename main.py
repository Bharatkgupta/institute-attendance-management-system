import tkinter as tk
from tkinter import *
from  tkinter import ttk
from tkinter import messagebox
from datetime import datetime as time
import os

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def main():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x260")
    main_screen.title("Main")
    Label(text="Select Yourself,", bg="#b1abf1", fg="white",
          width="300", height="2", font=("Calibri", 13)).pack(padx=20, pady=23 )
    Button(text="Faculty", height="2", width="15", fg="#c0ecc0",command=facultylogin).pack(padx=1, pady=20)
    Button(text="Student", height="2", width="15",fg="#D8BFD8", command=studentlogin).pack(padx=1, pady=5)
    main_screen.mainloop()

def studentlogin():
    main_screen.destroy()
    global login_screen
    login_screen = Tk()
    login_screen.title("Student Login")
    login_screen.geometry("320x350")
    Label(login_screen,text="Enter Login Details",bg="#c0ecc0", fg="black",
          width="300", height="2",font=("Calibri", 13)).pack(padx=20, pady=23 )
    Label(login_screen, text="").pack()

    global rollno_verify
    global password_verify

    rollno_verify = StringVar()
    password_verify = StringVar()

    global rollno_login_entry
    global password_login_entry

    Label(login_screen, text="Roll no.",fg="black", bg="#c0ecc0").pack()
    rollno_login_entry = Entry(login_screen, textvariable=rollno_verify)
    rollno_login_entry.pack(pady=5)

    Label(login_screen, text="").pack()
    Label(login_screen, text="Password",fg="black", bg="#c0ecc0").pack(pady=5)
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()

    Label(login_screen, text="").pack()
    Button(login_screen, text="Back",width=10,fg="black" ,height=1, command=backtomain).pack(padx=(0,70), side=RIGHT)
    Button(login_screen, text="Login",width=10,fg="black" ,height=1, command=student_login_verify).pack(padx=(70,0), side=LEFT)
    login_screen.mainloop()

def facultylogin():
    main_screen.destroy()
    global login_screen
    login_screen = Tk()
    login_screen.title("Faculty Login")
    login_screen.geometry("320x350")
    Label(login_screen,text="Enter Login Details",bg="#c0ecc0", fg="black",
          width="300", height="2",font=("Calibri", 13)).pack(padx=20, pady=23 )
    Label(login_screen, text="").pack()

    global facid_verify
    global password_verify

    facid_verify = StringVar()
    password_verify = StringVar()

    global facid_login_entry
    global password_login_entry

    Label(login_screen, text="Username",fg="black", bg="#c0ecc0").pack()
    facid_login_entry = Entry(login_screen, textvariable=facid_verify)
    facid_login_entry.pack(pady=5)

    Label(login_screen, text="").pack()
    Label(login_screen, text="Password",fg="black", bg="#c0ecc0").pack(pady=5)
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()

    Label(login_screen, text="").pack()
    Button(login_screen, text="Back",width=10,fg="black" ,height=1, command=backtomain).pack(padx=(0,70), side=RIGHT)
    Button(login_screen, text="Login",width=10,fg="black" ,height=1, command=faculty_login_verify).pack(padx=(70,0), side=LEFT)
    login_screen.mainloop()

def backtomain():
    login_screen.destroy()
    main()

def student_login_verify():
    rollno = rollno_verify.get()
    password = password_verify.get()
    rollno_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    student_dashboard() # to check

    # list_of_files = os.listdir()
    # if rollno in list_of_files:
    #     file1 = open(rollno, "a")
    #     verify = file1.read().splitlines()
    #     if password in verify:
    #         student_dashboard()
    #     else:
    #         password_not_recognised()
    # else:
    #     user_not_found()

def faculty_login_verify():
    facid = facid_verify.get()
    password = password_verify.get()
    facid_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    if(facid == "ADMIN" and password == "terabaap"):
        admin_dasboard()

    faculty_dashboard() # to check

    # list_of_files = os.listdir()
    # if facid in list_of_files:
    #     file1 = open(facid, "a")
    #     verify = file1.read().splitlines()
    #     if password in verify:
    #         faculty_dashboard()
    #     else:
    #         password_not_recognised()
    # else:
    #     user_not_found()

def admin_dasboard():
    login_screen.destroy()
    global dashboard
    dashboard = Tk()
    dashboard.title("Welcome Admin,")
    dashboard.geometry("300x500")
    Label(text="Dashboard", bg="#b1abf1", fg="white",
          width="300", height="2", font=("Calibri", 13)).pack(padx=20, pady=23 )
    Button(text="Institute Courses", height="2", width="15", fg="#c0ecc0",command=Attendence).pack(padx=1, pady=(20,5))
    Button(text="Add Faculty", height="2", width="15",fg="#D8BFD8", command=student_courses).pack(padx=1, pady=5)
    Button(text="Add Student", height="2", width="15",fg="#D8BFD8", command=student_courses).pack(padx=1, pady=5)
    Button(text="Add Course", height="2", width="15",fg="#D8BFD8", command=student_courses).pack(padx=1, pady=5)
    Button(text="Add Schedule", height="2", width="15",fg="#D8BFD8", command=student_courses).pack(padx=1, pady=5)
    Button(text="Logout", height="2", width="15",fg="#D8BFD8", command=dashboardtomain).pack(padx=1, pady=5)
    dashboard.mainloop()

def student_dashboard():
    login_screen.destroy()
    global dashboard
    dashboard = Tk()
    dashboard.title("Welcome 'student_name',")
    dashboard.geometry("300x350")
    Label(text="Dashboard", bg="#b1abf1", fg="white",
          width="300", height="2", font=("Calibri", 13)).pack(padx=20, pady=23 )
    Button(text="Attendence", height="2", width="15", fg="#c0ecc0",command=Attendence).pack(padx=1, pady=(20,5))
    Button(text="My Courses", height="2", width="15",fg="#D8BFD8", command=student_courses).pack(padx=1, pady=5)
    Button(text="Logout", height="2", width="15",fg="#D8BFD8", command=dashboardtomain).pack(padx=1, pady=5)
    dashboard.mainloop()

def faculty_dashboard():
    login_screen.destroy()
    global dashboard
    dashboard = Tk()
    dashboard.title("Welcome 'faculty_name',")
    dashboard.geometry("300x400")
    Label(text="Dashboard", bg="#b1abf1", fg="white",
          width="300", height="2", font=("Calibri", 13)).pack(padx=20, pady=23 )
    Button(text="Attendence", height="2", width="15", fg="#c0ecc0",command=Attendence).pack(padx=1, pady=(20,5))
    Button(text="My Courses", height="2", width="15",fg="#D8BFD8", command=faculty_courses).pack(padx=1, pady=5)
    Button(text="Student's Attendence", height="2", width="15",fg="#D8BFD8", command=student_attendence).pack(padx=1, pady=5)
    Button(text="Logout", height="2", width="15",fg="#D8BFD8", command=dashboardtomain).pack(padx=1, pady=5)
    dashboard.mainloop()

def dashboardtomain():
    dashboard.destroy()
    main()

def Attendence():
    
    now = time.now()
    day = now.weekday()
    hour = now.hour
    minute = now.minute

    course = "#" # get this from database

    messagebox.showinfo("Attendence Marked", "Your attendence for {} course is marked at time {}:{} {}".format(course, hour, minute, days[day]))

def student_courses():
    global courses
    courses = Toplevel(dashboard)
    courses.title("Your courses")
    courses.geometry("500x400")

    c = Frame(courses)
    c.pack()

    Label(c, text="Courses", bg="#b1abf1", fg="white",
          width="300", height="2", font=("Calibri", 13)).pack(padx=20, pady=23 )

    #scrollbar
    cscroll = Scrollbar(c)
    cscroll.pack(side=RIGHT, fill=Y)

    C = ttk.Treeview(c,yscrollcommand=cscroll.set)
    C.pack()

    cscroll.config(command=C.yview)

    #define our column
    C['columns'] = ('player_id', 'player_name', 'player_Rank', 'player_states', 'player_city') # get column names from database

    # format our column
    C.column("#0", width=0,  stretch=NO)
    C.column("player_id",anchor=CENTER, width=80)
    C.column("player_name",anchor=CENTER,width=80)
    C.column("player_Rank",anchor=CENTER,width=80)
    C.column("player_states",anchor=CENTER,width=80)
    C.column("player_city",anchor=CENTER,width=80)

    #Create Headings 
    C.heading("#0",text="",anchor=CENTER)
    C.heading("player_id",text="Id",anchor=CENTER)
    C.heading("player_name",text="Name",anchor=CENTER)
    C.heading("player_Rank",text="Rank",anchor=CENTER)
    C.heading("player_states",text="States",anchor=CENTER)
    C.heading("player_city",text="States",anchor=CENTER)

    #add data 
    C.insert(parent='',index='end',iid=0,text='',
    values=('1','Ninja','101','Oklahoma', 'Moore'))
    C.insert(parent='',index='end',iid=1,text='',
    values=('2','Ranger','102','Wisconsin', 'Green Bay'))
    C.insert(parent='',index='end',iid=2,text='',
    values=('3','Deamon','103', 'California', 'Placentia'))
    C.insert(parent='',index='end',iid=3,text='',
    values=('4','Dragon','104','New York' , 'White Plains'))
    C.insert(parent='',index='end',iid=4,text='',
    values=('5','CrissCross','105','California', 'San Diego'))
    C.insert(parent='',index='end',iid=5,text='',
    values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
    C.insert(parent='',index='end',iid=6,text='',
    values=('7','RayRizzo','107','Colorado' , 'Denver'))
    C.insert(parent='',index='end',iid=7,text='',
    values=('8','Byun','108','Pennsylvania' , 'ORVISTON'))
    C.insert(parent='',index='end',iid=8,text='',
    values=('9','Trink','109','Ohio' , 'Cleveland'))
    C.insert(parent='',index='end',iid=9,text='',
    values=('10','Twitch','110','Georgia' , 'Duluth'))
    C.insert(parent='',index='end',iid=10,text='',
    values=('11','Animus','111', 'Connecticut' , 'Hartford'))
    C.pack()
    

def faculty_courses():
    global courses
    courses = Toplevel(dashboard)
    courses.title("Your courses")
    courses.geometry("500x400")

    c = Frame(courses)
    c.pack()

    Label(c, text="Courses", bg="#b1abf1", fg="white",
          width="300", height="2", font=("Calibri", 13)).pack(padx=20, pady=23 )

    #scrollbar
    cscroll = Scrollbar(c)
    cscroll.pack(side=RIGHT, fill=Y)

    C = ttk.Treeview(c,yscrollcommand=cscroll.set)
    C.pack()

    cscroll.config(command=C.yview)

    #define our column
    C['columns'] = ('player_id', 'player_name', 'player_Rank', 'player_states', 'player_city') # get column names from database

    # format our column
    C.column("#0", width=0,  stretch=NO)
    C.column("player_id",anchor=CENTER, width=80)
    C.column("player_name",anchor=CENTER,width=80)
    C.column("player_Rank",anchor=CENTER,width=80)
    C.column("player_states",anchor=CENTER,width=80)
    C.column("player_city",anchor=CENTER,width=80)

    #Create Headings 
    C.heading("#0",text="",anchor=CENTER)
    C.heading("player_id",text="Id",anchor=CENTER)
    C.heading("player_name",text="Name",anchor=CENTER)
    C.heading("player_Rank",text="Rank",anchor=CENTER)
    C.heading("player_states",text="States",anchor=CENTER)
    C.heading("player_city",text="States",anchor=CENTER)

    #add data 
    C.insert(parent='',index='end',iid=0,text='',
    values=('1','Ninja','101','Oklahoma', 'Moore'))
    C.insert(parent='',index='end',iid=1,text='',
    values=('2','Ranger','102','Wisconsin', 'Green Bay'))
    C.insert(parent='',index='end',iid=2,text='',
    values=('3','Deamon','103', 'California', 'Placentia'))
    C.insert(parent='',index='end',iid=3,text='',
    values=('4','Dragon','104','New York' , 'White Plains'))
    C.insert(parent='',index='end',iid=4,text='',
    values=('5','CrissCross','105','California', 'San Diego'))
    C.insert(parent='',index='end',iid=5,text='',
    values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
    C.insert(parent='',index='end',iid=6,text='',
    values=('7','RayRizzo','107','Colorado' , 'Denver'))
    C.insert(parent='',index='end',iid=7,text='',
    values=('8','Byun','108','Pennsylvania' , 'ORVISTON'))
    C.insert(parent='',index='end',iid=8,text='',
    values=('9','Trink','109','Ohio' , 'Cleveland'))
    C.insert(parent='',index='end',iid=9,text='',
    values=('10','Twitch','110','Georgia' , 'Duluth'))
    C.insert(parent='',index='end',iid=10,text='',
    values=('11','Animus','111', 'Connecticut' , 'Hartford'))
    C.pack()

def student_attendence():
    global attendence_dashboard
    attendence_dashboard = Toplevel(dashboard)
    attendence_dashboard.title("'student's name' Attendence dashboared")
    attendence_dashboard.geometry("500x400")

    c = Frame(attendence_dashboard)
    c.pack()

    Label(c, text="Courses", bg="#b1abf1", fg="white",
          width="300", height="2", font=("Calibri", 13)).pack(padx=20, pady=23 )

    #scrollbar
    cscroll = Scrollbar(c)
    cscroll.pack(side=RIGHT, fill=Y)

    C = ttk.Treeview(c,yscrollcommand=cscroll.set)
    C.pack()

    cscroll.config(command=C.yview)

    #define our column
    C['columns'] = ('player_id', 'player_name', 'player_Rank', 'player_states', 'player_city') # get column names from database

    # format our column
    C.column("#0", width=0,  stretch=NO)
    C.column("player_id",anchor=CENTER, width=80)
    C.column("player_name",anchor=CENTER,width=80)
    C.column("player_Rank",anchor=CENTER,width=80)
    C.column("player_states",anchor=CENTER,width=80)
    C.column("player_city",anchor=CENTER,width=80)

    #Create Headings 
    C.heading("#0",text="",anchor=CENTER)
    C.heading("player_id",text="Id",anchor=CENTER)
    C.heading("player_name",text="Name",anchor=CENTER)
    C.heading("player_Rank",text="Rank",anchor=CENTER)
    C.heading("player_states",text="States",anchor=CENTER)
    C.heading("player_city",text="States",anchor=CENTER)

    #add data 
    C.insert(parent='',index='end',iid=0,text='',
    values=('1','Ninja','101','Oklahoma', 'Moore'))
    C.insert(parent='',index='end',iid=1,text='',
    values=('2','Ranger','102','Wisconsin', 'Green Bay'))
    C.insert(parent='',index='end',iid=2,text='',
    values=('3','Deamon','103', 'California', 'Placentia'))
    C.insert(parent='',index='end',iid=3,text='',
    values=('4','Dragon','104','New York' , 'White Plains'))
    C.insert(parent='',index='end',iid=4,text='',
    values=('5','CrissCross','105','California', 'San Diego'))
    C.insert(parent='',index='end',iid=5,text='',
    values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
    C.insert(parent='',index='end',iid=6,text='',
    values=('7','RayRizzo','107','Colorado' , 'Denver'))
    C.insert(parent='',index='end',iid=7,text='',
    values=('8','Byun','108','Pennsylvania' , 'ORVISTON'))
    C.insert(parent='',index='end',iid=8,text='',
    values=('9','Trink','109','Ohio' , 'Cleveland'))
    C.insert(parent='',index='end',iid=9,text='',
    values=('10','Twitch','110','Georgia' , 'Duluth'))
    C.insert(parent='',index='end',iid=10,text='',
    values=('11','Animus','111', 'Connecticut' , 'Hartford'))
    C.pack()

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("ERROR")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("ERROR")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen,fg="red", text="User Not Found!").pack(pady=20)
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def delete_login_success():
    login_success_screen.destroy()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("320x350")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Enter Details Below to Login!",bg="#D8BFD8", fg="black",
          width="300", height="2",font=("Calibri", 13)).pack(padx=20, pady=23 )
    Label(register_screen, text="").pack()

    unLabel = Label(register_screen, text="Username",fg="black", bg="#D8BFD8")
    unLabel.pack(pady=5)

    unEntry = Entry(register_screen, textvariable=username)
    unEntry.pack()

    passLabel = Label(register_screen, text="Password",fg="black" , bg="#D8BFD8")
    passLabel.pack(pady=5)

    passEntry = Entry(register_screen,textvariable=password, show='*')
    passEntry.pack()

    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, fg="black", command=register_user).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

main()