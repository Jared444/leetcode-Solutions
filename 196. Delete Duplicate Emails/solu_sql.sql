# Write your MySQL query statement below
Delete d1
from person d1
INNER JOIN person d2 
WHERE d1.email = d2.email and d1.id > d2.id;