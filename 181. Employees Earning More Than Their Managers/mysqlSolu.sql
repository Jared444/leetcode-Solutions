# Write your MySQL query statement below
select a.name As Employee
from Employee a
join Employee m on a.managerId = m.id
where a.salary > m.salary