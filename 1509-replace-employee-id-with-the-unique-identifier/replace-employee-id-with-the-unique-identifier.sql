# Write your MySQL query statement below
SELECT unique_id, name 
FROM EmployeeUNI EU RIGHT JOIN Employees E 
ON EU.id=E.id;