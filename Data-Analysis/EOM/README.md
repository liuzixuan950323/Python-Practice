1.	Load data from the SPY.csv file used in class on 20180823.   

2.	Compute 1-day rates of return based on the “Adj Close” column.

3.	Create a new column named “EOM3” that is equal to 0 on all days except for the third business day before the end of the month.  On those days, the EOM3 column should equal 1.   For example, if the last three business days of the month are the 27th, 28th, and 29th, then the 27th would have EOM3=1 and all other days will have EOM3=0.

4.	Compute the average return over all days and only over the EOM3=1 subset.
