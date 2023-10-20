select HISTORY_ID, round(daily_fee*(DATEDIFF(h.end_date,h.start_date)+1)
                        *(case
                         when datediff(end_date,start_date)+1<7 then 1
                         when datediff(end_date,start_date)+1<30 then 0.95
                         when datediff(end_date,start_date)+1<90 then 0.92
                         else 0.85 end))as FEE

from CAR_RENTAL_COMPANY_CAR as c 
    join CAR_RENTAL_COMPANY_RENTAL_HISTORY as h
    on c.CAR_ID = h.CAR_ID
    join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as p
    on c.CAR_TYPE = p.CAR_TYPE
where c.car_type = '트럭'
group by history_id
order by FEE desc, HISTORY_ID desc