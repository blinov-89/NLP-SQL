#Create databa
#create database nlpproj

#Use database
use nlpproj

#Create table student
"""
	Student => sId | name | sex | addrees | phone | cgpa | 
"""
CREATE TABLE student (
 sId INTEGER PRIMARY KEY,
 name VARCHAR(20) NOT NULL,
 sex CHAR(7),
 address VARCHAR(50),
 phone CHAR(20),
 cgpa INTEGER
);


#Create table department
CREATE TABLE department (
 dId INTEGER PRIMARY KEY,
 name VARCHAR(30),
 buildingCode INTEGER
);

#Create users table
CREATE TABLES users (
	userid  VARCHAR(30) PRIMARY KEY,
	password VARCHAR(30),
	access INTEGER,
	name VARCHAR(30),
);

CREATE TABLE propuska (
ID varchar(50),
	Series varchar(50),
 	Number varchar(50),
  	ValidFrom varchar(50),
   	ValidTo varchar(50),
    Zone varchar(50),
    Status varchar(50),
    CancelDate varchar(50),
    global_id varchar(50)
);
CREATE TABLE sport(
section varchar(50),
	subsection varchar(50),
 	title varchar(50),
  	description varchar(50),
   	start varchar(50),
    stop varchar(50),
    addres varchar(50),
    participant varchar(50)
);


