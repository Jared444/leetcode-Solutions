# Write your MySQL query statement below
select C.name As Customers
from Customers C left join Orders O on C.id = O.customerId
where customerId is null