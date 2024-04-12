select p.product_id, p.product_name, (p.price * o.amount) as total_sales
from food_product p join (
    select product_id, sum(amount) as amount
    from food_order
    where to_char(produce_date,'YYYY-MM') like '2022-05'
    group by product_id) o 
on p.product_id = o.product_id
order by total_sales desc, p.product_id;
