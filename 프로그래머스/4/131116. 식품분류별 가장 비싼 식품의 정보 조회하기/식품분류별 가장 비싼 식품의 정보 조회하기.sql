select category, price as max_price, product_name
from food_product
where price in (
    SELECT max(price) as max_price
    from  food_product
    where category in ('과자','국','김치','식용유')
    group by category) and category in  ('과자','국','김치','식용유')
order by price desc
