SELECT i.animal_id, i.name 
from ANIMAL_INS i join ANIMAL_OUTS o
on i.animal_id = o.animal_id
where i.datetime > o.datetime
order by i.datetime;