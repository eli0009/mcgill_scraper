# McGill Scraper

THIS SOFTWARE IS STILL IN DEVELOPMENT

A command-line program to make the course selection process easier (and less painful).

## Features (More to be added)
Scrap every course listed in a [math and statistics faculty](https://www.mcgill.ca/mathstat/undergraduate/programs/) undergraduate program's page: 
https://www.mcgill.ca/mathstat/undergraduate/programs/b-sc/minor-statistics-b-sc 


## Problem

Each course has it's own list of prerequisites and restrictions, along with its number of credits. While some prerequisites are straightforward, such as [ECSE 539](https://www.mcgill.ca/study/2022-2023/courses/ecse-539):
>Prerequisite(s): COMP 303 or ECSE 321 or permission of instructor.

Others are not so simple. Taking [ECSE 424](https://www.mcgill.ca/study/2022-2023/courses/ecse-424) as an example:
>Prerequisites: (ECSE 324 and ECSE 250) or (ECSE 324 and COMP 250) or (COMP 251 and COMP 273)

Also, some courses have 3 credits while others have 4, and there are additional requirements that, for example, require you to choose a certain number of courses from each category. Below are some of the restrictions:
>Students may select either COMP 409 or ECSE 420, but not both.

>Restriction(s): Not open to students who have taken or are taking COMP 451.

>15 credits selected from Groups C and D, with at least 9 credits selected from Group C, and at least 3 credits selected from Group D. 

>Prerequisite(s): MATH 208, one of MATH 223, MATH 236, MATH 247, MATH 251; MATH 323 or MATH 356.

To keep track of them can be difficult. As a first year student, dealing with the prerequisites and the requirements was extremely challenging. As such, I wish to make my life easier by making a program that takes care of the annoying stuff.