### Introduction
This file will help to modify the content of any file. It could be .yaml file, .py file , .txt etc.
And also help to run main python program script in loop each time with new modified/updated file.

I have created this script. Because I need to run my main program again and again with different dates in configuration.yaml file.
If I do it manually then I need to change the date manually each time in .yaml file and then need to run main program. I need to do this process
for multiple dates. So I created this script to do it automatically for me just by giving a start_date, previous date , nb_dates, frequency as parameter.

  
Previous_date : date already exist in my configuration.yaml file that I need to replace with new date value.   
Start_date: very first date that I need to change in configuration.yaml file.   
nb_dates: How many number of dates I need to add in datelist from Start_date value.   
frequency: How much should be frequency of dates to create. I have used 7 days. So it will create a date from current day to next 7th day.   

**Algorithmic steps:**

1. So I created a list of dates which I need to modify each time in .yaml file. 
2. Then I have created a for loop which take dates one by one from datelist.
3. I have also created a function that will take the current iteration date value from for loop and replace old date in .yaml file with current date.
4. After running this function It will run the main program file with updated current date configurations