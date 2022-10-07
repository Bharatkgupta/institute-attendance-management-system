import mysql.connector as mysql
import dbconnect as db

day = 1
tnow = "{}:00:00".format(5)

conn = mysql.connect(**db.dbConfig)
cursor = conn.cursor(buffered=True)
cursor.execute("select course_code from courses_taken where roll_no=%s and course_code in (select course_code from courses_sch where day=%s and start_time=%s)", ('1', day, tnow))
rowcount = cursor.rowcount
for course_code in cursor:  # type: ignore
    print(course_code)
print(rowcount)
cursor.close()
conn.close()