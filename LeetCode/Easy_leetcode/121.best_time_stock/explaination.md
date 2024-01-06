this question want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

So this works by providing array of values of each day stock price.

so we'll consider left and right pointers to run through the array. And a maximum profit varibale maxP.

check whether the left day is greater than the right day if that is the case calculate the profit by differencing them. 
then calculate the max profit by whether the max profit is greater or the current profit that is calculated.

if the left day is not greater than the right day we will change the left variable to right. 

finally r is incremented.