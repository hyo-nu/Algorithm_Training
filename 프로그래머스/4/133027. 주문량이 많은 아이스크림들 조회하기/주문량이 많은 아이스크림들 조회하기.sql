-- 코드를 입력하세요


select n.flavor
from(
    select rownum as num, e.*
    from(
        select flavor, sum(total_order) as sum_order
        from (
            SELECT f.flavor as flavor, (f.total_order + j.total_order) as total_order
            from first_half f full outer join july j 
            on f.flavor = j.flavor) 
        group by flavor
        order by sum_order desc) e
    ) n where num <= 3;