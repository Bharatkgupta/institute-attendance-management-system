from tkinter import *
from  tkinter import ttk
from tkinter import messagebox
from datetime import datetime as time
from datetime import date
import mysql.connector as mysql
import dbconnect as db

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
    login_screen.title("Professor Login")
    login_screen.geometry("320x350")
    Label(login_screen,text="Enter Login Details",bg="#c0ecc0", fg="black",
          width="300", height="2",font=("Calibri", 13)).pack(padx=20, pady=23 )
    Label(login_screen, text="").pack()

    global profid_verify
    global password_verify

    profid_verify = StringVar()
    password_verify = StringVar()

    global profid_login_entry
    global password_login_entry

    Label(login_screen, text="Professor ID",fg="black", bg="#c0ecc0").pack()
    profid_login_entry = Entry(login_screen, textvariable=profid_verify)
    profid_login_entry.pack(pady=5)

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

    if rollno == "" or password == "":
        messagebox.showerror("Information",'Error Enter username & password')
    else:
        try:
            conn = mysql.connect(**db.dbConfig)
            cursor = conn.cursor(buffered=True)
            cursor.execute("select name from students where roll_no=%s and password=%s", (rollno, password))
            rowcount = cursor.rowcount
            if rowcount == 1:
                messagebox.showinfo('Information', "Login Successfully")
                for name in cursor:  
                    Name = name[0]
                student_dashboard(rollno,Name) 
            else:
                messagebox.showinfo('Information', "Login failed,Invalid Username or Password.Try again!!!")
            cursor.close()
            conn.close()
        except Exception as es:
            messagebox.showinfo('Error', f"due to :{str(es)}")

def faculty_login_verify():
    profid = profid_verify.get()
    password = password_verify.get()
    profid_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    if(profid == "ADMIN" and password == "terabaap"):
        admin_dasboard()

    if profid == "" or password == "":
        messagebox.showerror("Information",'Error Enter username & password')
    else:
        try:
            conn = mysql.connect(**db.dbConfig)
            cursor = conn.cursor(buffered=True)
            cursor.execute("select name from professors where prof_id=%s and password=%s", (profid, password))
            rowcount = cursor.rowcount
            if rowcount == 1:
                messagebox.showinfo('Information', "Login Successfully")
                for name in cursor:  
                    Name = name[0]
                faculty_dashboard(profid,Name)
            else:
                messagebox.showinfo('Information', "Login failed,Invalid Username or Password.Try again!!!")
            cursor.close()
            conn.close()
        except Exception as es:
            messagebox.showinfo('Error', f"due to :{str(es)}")

def admin_dasboard():
    login_screen.destroy()
    global dashboard
    dashboard = Tk()
    dashboard.title("Welcome Admin,")
    dashboard.geometry("300x500")
    Label(text="Dashboard", bg="#b1abf1", fg="white",
          width="300", height="2", font=("Calibri", 13)).pack(padx=20, pady=23 )
    Button(text="Institute Courses", height="2", width="15", fg="#c0ecc0",command=allcourses).pack(padx=1, pady=(20,5))
    # Button(text="Add Faculty", height="2", width="15",fg="#D8BFD8", command=student_courses).pack(padx=1, pady=5)
    # Button(text="Add Student", height="2", width="15",fg="#D8BFD8", command=student_courses).pack(padx=1, pady=5)
    # Button(text="Add Course", height="2", width="15",fg="#D8BFD8", command=student_courses).pack(padx=1, pady=5)
    # Button(text="Add Schedule", height="2", width="15",fg="#D8BFD8", command=student_courses).pack(padx=1, pady=5)
    Button(text="Logout", height="2", width="15",fg="#D8BFD8", command=dashboardtomain).pack(padx=1, pady=5)
    dashboard.mainloop()

def allcourses():
    global courses_dasboard
    courses_dasboard = Toplevel(dashboard)
    courses_dasboard.title("Courses")
    courses_dasboard.geometry("300x350")

    c = Frame(courses_dasboard)
    c.pack()

    Label(c, text="All Courses", bg="#b1abf1", fg="white",
          width="300", height="2", font=("Calibri", 13)).pack(padx=20, pady=23 )

    #scrollbar
    cscroll = Scrollbar(c)
    cscroll.pack(side=RIGHT, fill=Y)

    C = ttk.Treeview(c,yscrollcommand=cscroll.set)
    C.pack()

    cscroll.config(command=C.yview)

    #define our column
    C['columns'] = ('Course_Code', 'Course_Name') # get column names from database

    # format our column
    C.column("#0", width=0,  stretch=NO)
    C.column("Course_Code",anchor=CENTER, width=80)
    C.column("Course_Name",anchor=CENTER,width=80)

    #Create Headings 
    C.heading("#0",text="",anchor=CENTER)
    C.heading("Course_Code",text="Course code",anchor=CENTER)
    C.heading("Course_Name",text="Course name",anchor=CENTER)

    #add data
    conn = mysql.connect(**db.dbConfig)
    cursor = conn.cursor(buffered=True)

    cursor.execute("select course_code, course_name from courses")

    for coursecode, coursename in cursor:
        print(coursecode, coursename)
        C.insert(parent='',index='end',text='', values=(coursecode, coursename))
    C.pack()

    cursor.close()
    conn.close()

def student_dashboard(rollno,name):
    login_screen.destroy()
    global dashboard
    dashboard = Tk()
    dashboard.title("Welcome {}".format(name))
    dashboard.geometry("300x350")
    Label(text="Dashboard", bg="#b1abf1", fg="white",
          width="300", height="2", font=("Calibri", 13)).pack(padx=20, pady=23)
    Button(text="Attendence", height="2", width="15", fg="#c0ecc0",command=lambda: Attendence(rollno)).pack(padx=1, pady=(20,5))
    Button(text="My Courses", height="2", width="15",fg="#D8BFD8", command=lambda: student_courses(rollno)).pack(padx=1, pady=5)
    Button(text="Logout", height="2", width="15",fg="#D8BFD8", command=dashboardtomain).pack(padx=1, pady=5)
    dashboard.mainloop()

def faculty_dashboard(profid, name):
    login_screen.destroy()
    global dashboard
    dashboard = Tk()
    dashboard.title("Welcome {}".format(name))
    dashboard.geometry("300x400")
    Label(text="Dashboard", bg="#b1abf1", fg="white",
          width="300", height="2", font=("Calibri", 13)).pack(padx=20, pady=23)
    Button(text="My Courses", height="2", width="15",fg="#D8BFD8", command=lambda: faculty_courses(profid)).pack(padx=1, pady=5)
    Button(text="Student's Attendence", height="2", width="15",fg="#D8BFD8", command=lambda: student_attendence(profid)).pack(padx=1, pady=5)
    Button(text="Logout", height="2", width="15",fg="#D8BFD8", command=dashboardtomain).pack(padx=1, pady=5)
    dashboard.mainloop()

def dashboardtomain():
    dashboard.destroy()
    main()

def Attendence(rollno):
    now = time.now()
    day = now.weekday()
    hour = now.hour
    minute = now.minute
    tnow = "{}:00:00".format(hour)

    conn = mysql.connect(**db.dbConfig)
    cursor = conn.cursor(buffered=True)

    cursor.execute("select course_code from courses_taken where roll_no=%s and course_code in (select course_code from courses_sch where day=%s and start_time=%s)", (rollno, day, tnow))
    if(cursor.rowcount == 0):
        cursor.close()
        conn.close()
        messagebox.showerror("Information","You have no Lectures at this moment")
        return

    for course_code in cursor:
        course = course_code[0]

    cursor.execute("select course_name from courses where course_code=%s", (course,))
    course_name = ""
    for cc in cursor:
        course_name = cc[0]

    cursor.execute("insert into attendance (roll_no, course_code, date) values (%s, %s, %s)", (rollno, course, date.today()))
    cursor.close()
    conn.close()

    messagebox.showinfo("Attendence Marked", "Your attendence for {} course is marked at time {}:{} {}".format(course_name, hour, minute, days[day]))

def student_courses(rollno):
    global courses
    courses = Toplevel(dashboard)
    courses.title("Your courses")
    courses.geometry("300x350")

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
    C['columns'] = ('Course_Code', 'Course_Name') # get column names from database

    # format our column
    C.column("#0", width=0,  stretch=NO)
    C.column("Course_Code",anchor=CENTER, width=80)
    C.column("Course_Name",anchor=CENTER,width=80)

    #Create Headings 
    C.heading("#0",text="",anchor=CENTER)
    C.heading("Course_Code",text="Course code",anchor=CENTER)
    C.heading("Course_Name",text="Course name",anchor=CENTER)

    #add data
    conn = mysql.connect(**db.dbConfig)
    cursor = conn.cursor(buffered=True)

    cursor.execute("select course_code, course_name from courses where course_code in (select course_code from courses_taken where roll_no=%s)", (rollno,))

    for coursecode, coursename in cursor:
        print(coursecode, coursename)
        C.insert(parent='',index='end',text='', values=(coursecode, coursename))
    C.pack()

    cursor.close()
    conn.close()
    

def faculty_courses(profid):
    global courses
    courses = Toplevel(dashboard)
    courses.title("Your courses")
    courses.geometry("300x350")

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
    C['columns'] = ('Course_Code', 'Course_Name') # get column names from database

    # format our column
    C.column("#0", width=0,  stretch=NO)
    C.column("Course_Code",anchor=CENTER, width=80)
    C.column("Course_Name",anchor=CENTER,width=80)

    #Create Headings 
    C.heading("#0",text="",anchor=CENTER)
    C.heading("Course_Code",text="Course code",anchor=CENTER)
    C.heading("Course_Name",text="Course name",anchor=CENTER)

    #add data
    conn = mysql.connect(**db.dbConfig)
    cursor = conn.cursor(buffered=True)

    cursor.execute("select course_code, course_name from courses where prof_id=%s", (profid,))

    for coursecode, coursename in cursor:
        print(coursecode, coursename)
        C.insert(parent='',index='end',text='', values=(coursecode, coursename))
    C.pack()

    cursor.close()
    conn.close()

def student_attendence(profid):
    global attendence_dashboard
    attendence_dashboard = Toplevel(dashboard)
    attendence_dashboard.title("Attendence dashboared")
    attendence_dashboard.geometry("500x450")

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
    C['columns'] = ('Course_Code', 'Attendence') # get column names from database

    # format our column
    C.column("#0", width=0,  stretch=NO)
    C.column("Course_Code",anchor=CENTER, width=80)
    C.column("Attendence",anchor=CENTER,width=80)

    #Create Headings 
    C.heading("#0",text="",anchor=CENTER)
    C.heading("Course_Code",text="Course code",anchor=CENTER)
    C.heading("Attendence",text="Attendence count",anchor=CENTER)

    Label(c, text="").pack()

    global rollno_verify
    rollno_verify = StringVar()
    Label(c, text="Students roll no.",fg="black", bg="#c0ecc0").pack(pady=1)
    rollno_login_entry = Entry(c, textvariable=rollno_verify)
    rollno_login_entry.pack(pady=5)

    Button(c, text="Go",width=5,fg="black" ,height=1, command=lambda: tableattendance(C,profid)).pack(padx=2)

def tableattendance(C,profid):
    rollno = rollno_verify.get()

    for row in C.get_children():
        C.delete(row)

    conn = mysql.connect(**db.dbConfig)
    cursor = conn.cursor(buffered=True)

    cursor.execute("select course_code, count(attend_id) as count from attendance where roll_no=%s and course_code in (select course_code from courses where prof_id=%s) group by course_code", (rollno,profid))

    for coursecode, count in cursor:
        C.insert(parent='',index='end',text='', values=(coursecode, count))
    C.pack()

    cursor.close()
    conn.close()

main()