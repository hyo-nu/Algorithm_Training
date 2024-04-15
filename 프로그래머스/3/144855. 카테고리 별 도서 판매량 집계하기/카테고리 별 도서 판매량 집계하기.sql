SELECT b.category, sum(sales) as total_sales
from book_sales s join book b 
on s.book_id = b.book_id
where to_char(s.sales_date,'YYYY-MM') = '2022-01'
group by b.category
order by b.category;

