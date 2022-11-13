import mysql.connector
import time

config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'nlpproj',
    'raise_on_warnings': True,

}

cnx = mysql.connector.connect(**config)
# print('Successful connection')
cursor = cnx.cursor()

# query = '''CREATE TABLE student (
#  sId INTEGER PRIMARY KEY,
#  name VARCHAR(20) NOT NULL,
#  sex CHAR(7),
#  address VARCHAR(50),
#  phone CHAR(20),
#  cgpa INTEGER,
#  did integer
# );


# #Create table department
# CREATE TABLE department (
#  dId INTEGER PRIMARY KEY,
#  name VARCHAR(30),
#  buildingCode INTEGER
# );

# #Create users table
# CREATE TABLE users (
# 	userid  VARCHAR(30) PRIMARY KEY,
# 	password VARCHAR(30),
# 	access INTEGER,
# 	name VARCHAR(30)
# );

# CREATE TABLE propuska (
#   ID varchar(50),
#   Series varchar(50),
#   Number varchar(50),
#   ValidFrom varchar(50),
#   ValidTo varchar(50),
#   Zone varchar(50),
#   Status varchar(50),
#   CancelDate varchar(50),
#   global_id varchar(50)
# );
# CREATE TABLE sport(
#   section varchar(50),
#   subsection varchar(50),
#   title varchar(50),
#   description varchar(50),
#   start varchar(50),
#   stop varchar(50),
#   addres varchar(50),
#   participant varchar(50)
# );'''
# for i in range(1):
#   cursor.execute(query)
# time.sleep(10)
# Add student details
add_student = "INSERT INTO student (sId,name,sex,address,phone,cgpa,dId) VALUES (%s,%s,%s,%s,%s,%s,%s)"
data_student = []
data_student.append((1, 'Dwayne', 'M', 'Los Angeles', '9562033255', 7, 23))
data_student.append((2, 'Harvey', 'M', 'California', '8109502625', 10, 37))
data_student.append((3, 'Rachel', 'F', 'Los Angeles', '9845913946', 9, 23))
data_student.append((4, 'Mike', 'M', 'Los Angeles', '9962234444', 10, 41))
data_student.append((5, 'Jessica', 'F', 'Texas', '9463688542', 8, 37))
data_student.append((6, 'Louis', 'M', 'New Jersey', '8558098383', 7, 41))
data_student.append((7, 'Donna', 'F', 'California', '9501188856', 8, 29))
data_student.append((8, 'Trevor', 'F', 'Hawaii', '9717366117', 4, 23))
data_student.append((9, 'Daniel', 'M', 'Georgia', '9223237016', 6, 37))
data_student.append((10, 'Dwayne', 'M', 'New York', '7219560267', 9, 41))
for i in range(10):
    cursor.execute(add_student, data_student[i])

# Add department detailsБА
add_department = "INSERT INTO department (dId,name,buildingCode) VALUES (%s,%s,%s)"
data_department = []
data_department.append((23, 'Civil', 101))
data_department.append((29, 'Chemical', 203))
data_department.append((31, 'CS', 104))
data_department.append((37, 'IT', 302))
data_department.append((41, 'Mining', 101))
data_department.append((43, 'Mechanical', 102))
for i in range(6):
    cursor.execute(add_department, data_department[i])

# Add users tables
add_user = "INSERT INTO users (userid,password,access,name) VALUES (%s,%s,%s,%s)"
data_user = []
data_user.append(('admin', 'admin', 1, 'Admin'))
data_user.append(('user', 'user', 2, 'User'))
for i in range(2):
    cursor.execute(add_user, data_user[i])

add_propusk = "INSERT INTO propuska (ID,Series,Number,ValidFrom,ValidTo,Zone,Status,CancelDate,global_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
data_propusk = []
data_propusk.append(
    (103231352, 'БА', '0345914', '15.01.2018', '12.01.2019', 'СК', 'Аннулирован', '18.12.2018', '832197905'))
data_propusk.append(
    (103231352, 'БА', '0345914', '15.01.2018', '12.01.2019', 'СК', 'Аннулирован', '18.12.2018', '832197905'))
data_propusk.append(
    (102601746, 'БА', '0345916', '15.01.2018', '12.01.2019', 'СК', 'Аннулирован', '18.12.2018', '832197907'))
for i in range(3):
    cursor.execute(add_propusk, data_propusk[i])

add_sport = "INSERT INTO sport (section,subsection,title,description,start,stop,address,participants) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
data_sport = []
data_sport.append(('Авиамодельный спорт', 'Основной', 'Кубок россии', 'кордовые модели воздушного', '2008-01-18',
                   '2008-01-20', 'Россия, Тульская обл', '30'))
data_sport.append(('Авиамодельный спорт', 'Основной', 'Кубок россии', 'кордовые модели воздушного', '2008-01-18',
                   '2008-01-20', 'Россия, Приморский край', '40'))
data_sport.append(('Авиамодельный спорт', 'Основной', 'Кубок россии', 'кордовые модели воздушного', '2008-01-18',
                   '2008-01-20', 'Россия, Тульская обл', '50'))
for i in range(3):
    cursor.execute(add_sport, data_sport[i])

cnx.commit()
cursor.close()
cnx.close()
