/*
 * Problem: 176. Second Highest Salary
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/second-highest-salary/
 * Language: mysql
 * Date: 2026-03-10
 */

select max(salary) as SecondHighestSalary
from employee
where salary <(select max(salary) from employee);
