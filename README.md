# TinyURL
One Simple Solution could be Hashing. Use a hash function to convert long string to short string. In hashing, that may be collisions (2 long URLs map to same short URL) and we need a unique short URL for every long URL so that we can access long URL back.

A Better Solution is to use the integer id stored in the database and convert the integer to a character string that is at most 6 characters long. This problem can basically seen as a base conversion problem where we have a 10 digit input number and we want to convert it into a 6 character long string. 

Below is one important observation about possible characters in URL. 

A URL character can be one of the following 
1) A lower case alphabet [‘a’ to ‘z’], total 26 characters 
2) An upper case alphabet [‘A’ to ‘Z’], total 26 characters 
3) A digit [‘0’ to ‘9’], total 10 characters

There are total 26 + 26 + 10 = 62 possible characters.
So the task is to convert a decimal number to base 62 number. 
To get the original long URL, we need to get URL id in the database. The id can be obtained using base 62 to decimal conversion.