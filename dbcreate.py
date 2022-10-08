from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
import dbconnect as db

DB_NAME = 'attendance'
TABLES = {}

TABLES['students'] = (
    "CREATE TABLE `students` ("
    "  `roll_no` int NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(30) NOT NULL,"
    "  `password` varchar(20) NOT NULL,"
    "  PRIMARY KEY (`roll_no`)"
    ") ENGINE=InnoDB")

TABLES['professors'] = (
    "CREATE TABLE `professors` ("
    "  `prof_id` int NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(30) NOT NULL,"
    "  `password` varchar(20) NOT NULL,"
    "  PRIMARY KEY (`prof_id`)"
    ") ENGINE=InnoDB")

TABLES['courses'] = (
    "CREATE TABLE `courses` ("
    "  `course_code` int NOT NULL,"
    "  `course_name` varchar(30) NOT NULL,"
    "  `prof_id` int NOT NULL,"
    "  PRIMARY KEY (`course_code`)"
    "  KEY `prof_id` (`prof_id`),"
    "  CONSTRAINT `prof_course` FOREIGN KEY (`prof_id`) "
    "     REFERENCES `professors` (`prof_id`)"
    ") ENGINE=InnoDB")

TABLES['courses_sch'] = (
    "CREATE TABLE `courses_sch` ("
    "  `course_code` int NOT NULL,"
    "  `day` int NOT NULL,"
    "  `start_time` time NOT NULL,"
    "  `end_time` time NOT NULL,"
    "  PRIMARY KEY (`course_code`,`day`),"
    "  KEY `course_code` (`course_code`),"
    "  CONSTRAINT `course_sch` FOREIGN KEY (`course_code`) "
    "     REFERENCES `courses` (`course_code`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['attendance'] = (
    "  CREATE TABLE `attendance` ("
    "  `attend_id` int NOT NULL AUTO_INCREMENT,"
    "  `roll_no` int NOT NULL,"
    "  `course_code` int NOT NULL,"
    "  `date` date NOT NULL,"
    "  PRIMARY KEY (`attend_id`)"
    "  KEY `roll_no` (`roll_no`),"
    "  KEY `course_code` (`course_code`),"
    "  CONSTRAINT `roll_no_attend` FOREIGN KEY (`roll_no`)"
    "     REFERENCES `students` (`roll_no`),"
    "  CONSTRAINT `course_attend` FOREIGN KEY (`course_code`)"
    "     REFERENCES `courses` (`course_code`)"
    ") ENGINE=InnoDB")

TABLES['courses_taken'] = (
    "CREATE TABLE `courses_taken` ("
    "  `roll_no` int NOT NULL,"
    "  `course_code` int NOT NULL,"
    "  PRIMARY KEY (`roll_no`,`course_code`),"
    "  KEY `roll_no` (`roll_no`),"
    "  KEY `course_code` (`course_code`),"
    "  CONSTRAINT `roll_no_course1` FOREIGN KEY (`roll_no`)"
    "     REFERENCES `students` (`roll_no`) ON DELETE CASCADE,"
    "  CONSTRAINT `roll_no_course2` FOREIGN KEY (`course_code`)"
    "     REFERENCES `courses` (`course_code`)"
    ") ENGINE=InnoDB")

cnx = mysql.connector.connect(**db.dbConfig)
cursor = cnx.cursor()

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()
