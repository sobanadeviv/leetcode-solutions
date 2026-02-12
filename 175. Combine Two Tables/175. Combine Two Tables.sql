/*
 * Problem: 175. Combine Two Tables
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/combine-two-tables/
 * Language: mysql
 * Date: 2026-02-12
 */

SELECT 
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person p
LEFT JOIN Address a
ON p.personId = a.personId;
