### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
A relational database management system that supports both SQL and JSON querying

- What is the difference between SQL and PostgreSQL?
SQL means Structured Query Langauge. It is a languague for managing databases. PostgreSQL is a database management system that uses SQL, but has additional features 

- In `psql`, how do you connect to a database?
command line: '\c database_name'

- What is the difference between `HAVING` and `WHERE`?
WHERE filters rows before grouping, while HAVING filters groups after grouping

- What is the difference between an `INNER` and `OUTER` join?
An INNER join returns records with matching values in both tables. OUTER join returns records records from one table and matched records in the second table

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
LEFT OUTER returns all records from left table, and matching records on the right table. RIGHT OUTER does the opposite as LEFT OUTER

- What is an ORM? What do they do?
Object-Relational Mapping: Converting data between incompatible types using object oriented programming. It creates a "bridge" between relational databases.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
AJAX requests are made from client side and can update the webpage without reloading, while server side requests are made from backend, requiring reloading

- What is CSRF? What is the purpose of the CSRF token?
Cross Site Request Forgery: A CSRF token is a unique, secret value used to prevent CSRF attacks

- What is the purpose of `form.hidden_tag()`?
Generates hidden fields that include CSRF tokens
