Tested with Gimp 2.10.14

# Merge multiple PDF pages into one page
Many times I needed to print a huge PDF file (usually lecture slides for an exam), but printing only one PDF page per A4 sheet sounded like a waste of money, paper and time. So here is a script that basically puts the PDF pages into the groups of 9 (or 16 or whatever), so you can print them together. Yay!

Usage: 
1. open Gimp
2. File > Open, and choose the PDF file you want to edit 
3. In the new dialog, choose option *open pages as layers*
4. All layers should be named with integers starting from 1
5. Choose Filters > Python-Fu > Console...
6. In the script *split_layers_into_groups*: pick your value for n (the number of slides per page, its square root should be an integer)
7. Paste the script into the console
8. After a while you should get a set of new layers consisting of smaller and positioned n slides
9. Choose File > Export As... 
10. Choose PDF type and in the new dialog *layers as pages* option

Voila

![screenshot](screen.png)
