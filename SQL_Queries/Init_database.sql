create table Client 
(
	Organization_Name varchar(255),
    Admin_FirstName varchar(255),
    Admin_LastName varchar(255),
    ID int
);

create table Device_Client
(
	Device_ID int,
	Client_ID int
);

create table Device
(
	ID int,
	Solar_ID int,
	Wind_ID int,
	Start_Date datetime
	
);

create table Solar 
(
	ID int,
<<<<<<< HEAD
	Time Datetime
=======
	Time Datetime,
	Power double
>>>>>>> releases
);

create table Wind 
(
	ID int,
<<<<<<< HEAD
	Time Datetime
=======
	Time Datetime,
	Power double
<<<<<<< HEAD
>>>>>>> releases
=======
);

create table Password 
(
	Client_ID int,
	Password varchar(255)
>>>>>>> releases
);