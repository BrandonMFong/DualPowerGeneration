select 	c.Organization_Name,
        s.*
    from Client c
        join Device_Client dc
            on c.ID = dc.Client_ID
        join Device d 
            on d.ID = dc.Device_ID
        join Solar s
            on s.ID = d.Solar_ID