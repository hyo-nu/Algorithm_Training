
select m.MEMBER_NAME, r.REVIEW_TEXT, to_char(r.REVIEW_DATE, 'YYYY-MM-DD') as dates
from MEMBER_PROFILE m join REST_REVIEW r
on m.MEMBER_ID = r.MEMBER_ID
where m.MEMBER_ID Like (
    select n.MEMBER_ID
    from (
        select rownum as num, e.*
        from(
            select MEMBER_ID, count(MEMBER_ID) as membercnt
            from REST_REVIEW
            group by MEMBER_ID
            order by membercnt desc
            ) e
        ) n where num = 1
)
order by dates , r.REVIEW_TEXT 
;




