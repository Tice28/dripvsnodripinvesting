"""
Author: Trisston Icenhower
Program: Dividend Reinvestment Caculator
Version: 1.0.0
Date: 7/8/2022
Updated: 7/26/2022

Description: This app takes a specific ticker and a
             monthly investment amount and caculates
             a yearly graph showing reinvestment amounts
             as well as total.
"""

import yfinance as yf
import PySimpleGUI as sg
import json
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

#A class to hold all data for the ticker
class TickerData:
    currentDividend = 0.0
    sharesOwned = 0.0
    stockPrice = 0.0
    dividendRate = 0.0
    distributionsPerYear = 0

#A class for contribution information
class ContributionData:
    monthlyContribution = 0.0
    yearsContributing = 0.0
    startingContribution = 0.0

class ListType:
    timeList = []
    valueList = []
    noReinValueList = []

def main():
    #Variables
    tickerVal = TickerData()
    contributions = ContributionData()
    lists = ListType()

    #Layout reads input from user
    layout = [ [sg.Text("Enter ticker symbol")],
             [sg.Input()],
             [sg.Text("Enter starting value")],
             [sg.Input()],
             [sg.Text("Enter Monthly Contribution")],
             [sg.Input()],
             [sg.Text("Enter Years Contributing")],
             [sg.Input()],
             [sg.Button('Continue')] ]

    window = sg.Window("Dividend Reinvestment", layout)
    event, values = window.read()
    
    #Gathers info from user
    msft = yf.Ticker(values[0])
    contributions.startingContribution = float(values[1])
    contributions.monthlyContribution = float(values[2])
    contributions.yearsContributing = int(values[3])
    
    #Retrieves Ticker's information and stores neccessary values
    stockStats = msft.stats()

    tickerVal.currentDividend = stockStats.get("defaultKeyStatistics")['lastDividendValue']
    tickerVal.stockPrice = stockStats.get("price")['regularMarketPrice']
    tickerVal.dividendRate = stockStats.get("summaryDetail")['dividendRate']

    #This is a rough calculation to determine how often dividends are distributed
    #Accurate for test cases "O" and "PG" (12 and 4 respectively)
    tickerVal.distributionsPerYear = round(tickerVal.dividendRate / tickerVal.currentDividend)

    lists.valueList = calculateReinvestment(tickerVal, contributions, lists)
    lists.noReinValueList = calculateInvestment(tickerVal, contributions, lists)
    for i in range(contributions.yearsContributing):
        lists.timeList.append(i)
    
    createGraph(lists, contributions)
    
    print("end")

def createGraph(lists, contributions):
    #Sets X and Y values according to calculations done to the data holding lists
    yearsX = lists.timeList 
    reinY = lists.valueList
    invY = lists.noReinValueList
    reinInterest = reinY[contributions.yearsContributing]
    del reinY[contributions.yearsContributing]
    invInterest = invY[contributions.yearsContributing]
    del invY[contributions.yearsContributing]
    print(int(invInterest))
    print( int(reinInterest))

    graph, ax = plt.subplots()

    reinvestmentGraph, = ax.plot(yearsX,reinY,color='green',marker = ".", label = "Reinvestment Value")
    investmentGraph = ax.plot(yearsX,invY, color='red', marker='.', label = "Investment Value")
    ax.set_title("Difference Between Investing Strategies")
    ax.set_xlabel("Time")
    ax.set_ylabel("Total Value (USD)")
    ax.legend()
    
    graph.savefig("figure.pdf")
    graph.show()

#Calculates reinvestment value of a stock
def calculateReinvestment(ticker, contributions, lists):
    i = 0
    j = 0
    totalValue = contributions.startingContribution
    totalInterest = 0.0
    
    while(i < contributions.yearsContributing):
        while(j < 12):
            if(ticker.distributionsPerYear == 12):
                #Calculates numbers of shares owned for dividend yield
                ticker.sharesOwned = totalValue / ticker.stockPrice
                #Calculates the dividend distribution based off number of shares owned
                totalValue += (ticker.sharesOwned * (ticker.dividendRate / ticker.distributionsPerYear))
                totalInterest += (ticker.sharesOwned * (ticker.dividendRate / ticker.distributionsPerYear))
            elif(j % ticker.distributionsPerYear == 2 or j == 0):
                ticker.sharesOwned = totalValue / ticker.stockPrice
                totalValue += (ticker.sharesOwned * (ticker.dividendRate / ticker.distributionsPerYear))
                totalInterest += (ticker.sharesOwned * (ticker.dividendRate / ticker.distributionsPerYear))
            totalValue += contributions.monthlyContribution
            j += 1
        #Adds all values to array to be passed to graphing function
        lists.valueList.append(totalValue)
        i += 1
        j = 0
    lists.valueList.append(totalInterest)
    return lists.valueList

#Calculates value of the stock without reinvestment
def calculateInvestment(ticker, contributions, lists):
    i = 0
    j = 0
    totalValue = contributions.startingContribution
    totalInterest = 0.0
    
    while(i < contributions.yearsContributing):
        while(j < 12):
            if(ticker.distributionsPerYear == 12):
                #Calculates numbers of shares owned for dividend yield
                ticker.sharesOwned = totalValue / ticker.stockPrice
                #Calculates the dividend distribution based off number of shares owned
                totalInterest += (ticker.sharesOwned * (ticker.dividendRate / ticker.distributionsPerYear))
            elif(j % ticker.distributionsPerYear == 2 or j == 0):
                ticker.sharesOwned = totalValue / ticker.stockPrice
                totalInterest += (ticker.sharesOwned * (ticker.dividendRate / ticker.distributionsPerYear))
            totalValue += contributions.monthlyContribution
            j += 1
        #Adds all values to array to be passed to graphing function
        lists.noReinValueList.append(totalValue)
        i += 1
        j = 0
    lists.noReinValueList.append(totalInterest)
    return lists.noReinValueList

#THE ACTUAL CALL TO MAIN THAT MAKES THIS EXECUTE
main()
    

