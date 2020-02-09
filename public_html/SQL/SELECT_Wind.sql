select 	c.Organization_Name,
        w.*
    from Client c
        join Device_Client dc
            on c.ID = dc.Client_ID
        join Device d 
            on d.ID = dc.Device_ID
        join Wind w
            on w.ID = d.Wind_ID