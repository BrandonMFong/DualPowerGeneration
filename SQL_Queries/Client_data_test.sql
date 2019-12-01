-- Making client

insert into Client (Organization_Name, Admin_FirstName, Admin_LastName, ID)
	values ('Org_0', 'Test0', 'User0', 1000);
	
-- Join for client and device
insert into Device_Client (Device_ID, Client_ID)
	values (1500, 1000);
	
-- Device table #5
-- DATETIME - format: YYYY-MM-DD HH:MI:SS
insert into Device (ID, Solar_ID, Wind_ID, Start_Date)
	values (1500, 1501, 1502, current_timestamp());
	
-- Solar TABLE #1
insert into Solar (ID, Time)
	values (1501, current_timestamp());
	
-- Wind TABLE #2
insert into Wind (ID, Time)
	values (1502, current_timestamp());
	
-- ID convention: Clientid-deviceid-solar-wind