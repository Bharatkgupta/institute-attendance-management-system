import tkinter as tk
from tkinter import *
import os

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
    global attendence

def student_courses():
    global courses

def faculty_courses():
    global courses

def student_attendence():
    global attendence_dashboard

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