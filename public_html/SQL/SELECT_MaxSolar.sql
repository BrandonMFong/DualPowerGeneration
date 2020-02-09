select 	c.Organization_Name,
			max(s.Power) Max
		from Client c
			join Device_Client dc
				on c.ID = dc.Client_ID
			join Device d 
				on d.ID = dc.Device_ID
			join Solar s
				on s.ID = d.Solar_ID