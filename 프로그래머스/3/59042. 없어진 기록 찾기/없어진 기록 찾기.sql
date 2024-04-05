-- 입양 O , 보호소 X 
-- 동물ID, 이름 
-- ID순
SELECT ANIMAL_ID, NAME
from ANIMAL_OUTS 
where ANIMAL_ID not in (
    SELECT i.ANIMAL_ID 
    from ANIMAL_INS i join ANIMAL_OUTS o 
    on i.ANIMAL_ID = o.ANIMAL_ID
)
order by ANIMAL_ID;

