SELECT MEMBER_ID, MEMBER_NAME, GENDER, to_char(DATE_OF_BIRTH,'YYYY-MM-DD')
from MEMBER_PROFILE 
where to_char(DATE_OF_BIRTH, 'MM') = 3 
        and GENDER Like 'W'
        and TLNO is not null
order by MEMBER_ID;