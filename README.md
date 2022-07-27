# dripvsnodripinvesting
A VERY simple graphing utility that shows the difference between reinvesting dividends into a stock vs taking it out. 


<h1>
IMPORTANT
  
</h1>

The math in this appears to be correct; however, I do not have the time to explicitly check every bit of it. It is a simple brute-force approach to calculating dividends. Feel free to let me know if you see anything wrong with it!

<h2>
Classes
</h2>

There are three main classes to this project.

<h3>
TickerData
</h3>
This class is responsible for gathering and storing the information from the Yahoo Finance library. This is connected via API. This gathers realtime data from the stock market. WARNING: This will throw errors with stocks that do not have a dividend yield/ do not show a dividend yield on the Yahoo Finance website. 

<h3>
ContributionData
</h3>
This class gathers information from the user. The data gathered is the put into the investment formulas to calculate the value of the stock/interest over the course of the simulated timeframe.

<h3>
ListType
</h3>
This class holds the different list types to consildate all the lists into a single object. This allows them to be passed into arguments in a simpler way compared to passing them as individual arguments. 

<h2>
Methods
</h2>

There are three main methods to this program.

<h3>
calculateReinvestment
</h3>
This method combines the values of the investments with the interest recieved in order to simulate reinvested dividends. DOES NOT CONSIDER STOCK APPRECIATION. 

<h3>
calculateInvestment
</h3>
This method DOES NOT reinvest dividends in order to simulate taking the dividends out as opposed to reinvesting. DOES NOT CONSIDER STOCK APPRECIATION. 

<h3>
createGraph
</h3>
This method takes the values stored in the ListTypes class to turn them into a graph that the user can see. This makes use of the matplotlib library in python. 

<h1>
Contact info / Socials
</h1>

Email: trisstonprogramming@gmail.com

Twitter: https://twitter.com/Trisston_Ice

