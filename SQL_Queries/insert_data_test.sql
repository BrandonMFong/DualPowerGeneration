
set @Solar_ID = 
(
    select Solar_ID
        from client cl 
            join device_client dc 
                on cl.ID = dc.Client_ID
            join device dev 
                on dev.ID = dc.Device_ID
        where cl.ID = 1000
);

select * 
    from solar 
    where ID = @Solar_ID