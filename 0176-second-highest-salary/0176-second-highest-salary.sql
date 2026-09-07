with rnk as (
    select id,salary,
dense_rank() over(order by salary desc) as rnk_id
from Employee)
select max(salary) as SecondHighestSalary
from rnk
where rnk_id = 2