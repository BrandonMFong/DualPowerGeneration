-- Making client

insert into Client (Organization_Name, Admin_FirstName, Admin_LastName, ID)
	values ('Org_0', 'Test0', 'User0', 1000);
	
-- Join for client and device
insert into Device_Client (Device_ID, Client_ID)
	values (1500, 1000);
	
-- Device table #5
-- DATETIME - format: YYYY-MM-DD HH:MI:SS
insert into Device (ID, Solar_ID, Wind_ID, Start_Date)
<<<<<<< HEAD
	values (1500, 1501, 1502, '2019-11-30 12:00:00');
	
-- Solar TABLE #1
insert into Solar (ID, Time)
	values (1501, '2019-11-30 12:00:00');
	
-- Wind TABLE #2
insert into Wind (ID, Time)
	values (1502, '2019-11-30 12:00:00');
=======
	values (1500, 1501, 1502, current_timestamp());
	
-- Solar TABLE #1
insert into Solar (ID, Time, Power)
	values (1501, current_timestamp(), abs(rand()));
	
-- Wind TABLE #2
insert into Wind (ID, Time, Power)
	values (1502, current_timestamp(), abs(rand()));
>>>>>>> releases
	
-- ID convention: Clientid-deviceid-solar-wind
	
-- Password TABLE #2
insert into Password (Client_ID, Password)
	values 
		(1000, 'dualpower');