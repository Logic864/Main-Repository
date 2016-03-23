#Add to portfolio:

#add this link to the App to point to the Stock Brokers: http://portfolio.morningstar.com/RtPort/reg/addtoportfolio.aspx?ticker=AAPL&name=Apple Inc

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 03 15:58:23 2015

@author: Baruch_Student




"""



class Stock:
    Stock_Name = ""    
    roe = 0
    de_ratio = 0
    share_price = 0
    revenue_increase_list = []
    debt_equity = []
    nmp = 0
    recommend = 0


import urllib
import smtplib
import numpy 
import matplotlib.pylab as plt
import csv
import datetime as dt
import matplotlib.dates as mdates
import getpass
from officialgui import *

    
def Buffett_Analyzer(ticker, s): 
    buffet_agrees_count = 0.0
           
    #Part A: analize revenue
    if (s.revenue_increase_list[0] < s.revenue_increase_list[len(s.revenue_increase_list) - 1]):
        buffet_agrees_count += 1
        print "Buffet loves the revenue increase of this company!!!"
    
    #In case if YR2010 > YR2015, but REVENUE was increasing for the last 3 years, we will grant only partial credit to the "buffet counter" - percentage
    elif (s.revenue_increase_list[len(s.revenue_increase_list) - 1]>s.revenue_increase_list[len(s.revenue_increase_list) - 2]) and (s.revenue_increase_list[len(s.revenue_increase_list) - 2]>s.revenue_increase_list[len(s.revenue_increase_list) - 3]) and (s.revenue_increase_list[len(s.revenue_increase_list) - 3]>s.revenue_increase_list[len(s.revenue_increase_list) - 4]):
        percentage = s.revenue_increase_list[len(s.revenue_increase_list) - 1]/float(s.revenue_increase_list[0])
        buffet_agrees_count += percentage   
    #___________________________________________________________
    #part A ends

    #Part B:Debt to Equity   
       
    #compare YR 2015 to YR 2014 (D/E in 2015 should be less that in 2014) 
    #AND less than 25% (both cases)
    if (s.debt_equity[len(s.debt_equity) -1] <= s.debt_equity[len(s.debt_equity) - 2]) and (s.debt_equity[len(s.debt_equity) - 1] < 0.25):
        buffet_agrees_count += 1
        print "D/E has been improving!!!"#reword later

    #if D/E in 2015 is higher than in 2014
    #calculate the D/E 5YR AVG and give partial credit to the Buffet Counter    
    elif s.debt_equity[len(s.debt_equity)-1] < 0.25:
        avg = numpy.mean(s.debt_equity)
        buffet_agrees_count += avg/s.debt_equity[len(s.debt_equity)-1]
        print "D/E is less than 25%!!!"
    #___________________________________________________________
    #part B ends

    #PART C - ROE > 20%
    if s.roe > 20:
        buffet_agrees_count += 1
        print "Buffet loves the ROE!!! YAY"
    else:
        print "Buffet thinks ROE is too low =(("
    #___________________________________________________________
    #part C ends

    #Part D: Net Profit Margin
    if s.npm > 0.10:
        buffet_agrees_count += 1
        print "YAY!!"
    #print npm
        
    #Part E:Stock price > $10
    if s.share_price > 10:
        buffet_agrees_count += 1
    
    #Return Results for Recommendation    
    return buffet_agrees_count
        
        



def Create_Stock_Info(ticker):
    
    #emplty list to store records
    stock = Stock() 

    stock.Stock_Name = ticker
   
    #___________________________________________________________
    #File 1: "Income Statement"
    #As an option we can add different report types, in this case we would have to replace variable "report_type"
    #we don't need it now
    report_type = "is"
    #download file
    url = "http://financials.morningstar.com/ajax/ReportProcess4CSV.html?t=" + ticker + "&reportType=" + report_type + "&period=12&dataType=A&order=asc&columnYear=5&number=3"

    #TO DO: change the path (save this file in APP folder)
    file_name = "C:\\Users\\" + str(getpass.getuser()) + "\\" + ticker + "Income_Satements.csv"
    urllib.urlretrieve(url, file_name)

    #Read file
    #TO DO: change the path (retrieve file from APP folder)
    new_file = open("C:\\Users\\" + str(getpass.getuser()) + "\\" + ticker + "Income_Satements.csv", "r")
    file_data = new_file.read().splitlines()
    new_file.close()
    #TEST:print file_data
    
    
    revenue = file_data[2].split(",")
    #print revenue
    for i in range(1, len(revenue)):
        if (i != ""):
            stock.revenue_increase_list.append(i)
       
    #print 
    #Testing part:
    #revenue_increase_list = [19740, 3711, 5089, 7872, 12466, 15938]
       
    #File 2: "Key Ratios"
    #download file
    url = "http://financials.morningstar.com/ajax/exportKR2CSV.html?t=" + ticker

    #TODO change the path (save in APP folder)
    file_name = "C:\\Users\\" + str(getpass.getuser()) + "\\" + ticker + "Key_Ratios.csv"
    urllib.urlretrieve(url, file_name)

    #Read file
    new_file = open("C:\\Users\\" + str(getpass.getuser()) + "\\" + ticker + "Key_Ratios.csv", "r")
    file_data1 = new_file.read().splitlines()
    new_file.close()


    de = file_data1[99].split(",")
    for i in range(6, len(de)):
        if de[i] == "":
            #debt_equity[i] = int(debt_equity[i])
            stock.debt_equity.append(0.0)
        else:
            stock.debt_equity.append(float(de[i]))
            
    ROE = file_data1[37].split(",")
    stock.roe = float(ROE[len(ROE)-1])
    
    #Part D - Net Profit Margin
    NPM = file_data[14].split(",")
    a = float(NPM[len(NPM)-1])
    b = float(stock.revenue_increase_list[len(stock.revenue_increase_list) - 1])
    stock.npm = a/b
    
    #File 3: Stock Price    
    url = "http://ichart.finance.yahoo.com/table.csv?s=" + ticker 
    file_stock = "C:\\Users\\" + str(getpass.getuser()) + "\\" + ticker + ".csv"
    urllib.urlretrieve(url, file_stock)

    #a)open file
    new_file = open("C:\\Users\\" + str(getpass.getuser()) + "\\" + ticker + ".csv", "r")
    file_data2 = new_file.readlines()
    stock_price = file_data2[1].split(",")
    new_file.close()
    
    stock.share_price = float(stock_price[4])
              
    #all data is collected now
    return stock  

#In case where portfolio is empty
#Lets talk more about it next time we meet
portfolio = []
ticker = "FB"
st = Create_Stock_Info(ticker)
buffet_agrees = Buffett_Analyzer(ticker, st)
print "Buffet_agrees Count is %s" % buffet_agrees

#Possible values of "recommend" variable:
#buy stok == 3
#hold == 2
#sell == 1

if buffet_agrees >= 3.5:
    st.recommend = 3
elif buffet_agrees < 3.5 and buffet_agrees >= 2:
    st.recommend = 2
else:
    st.recommend = 1
    
#add stock to portfolio    
portfolio.append(st) 
  
#FOR GRAPH OUTPUT 
"""
def getYearsList(): 
    new_file = open("/Users/BettyFung/Downloads/" + ticker + ".csv", "r")
    stock_data = new_file.read().splitlines()
    del stock_data[0]
    new_file.close()
    
    years_available = []
 
    #format for years in csv file is different for each computer for some reason, my years are the first 4 digits 
    for data in stock_data: 
        col = data.split(",")
        yearColumn = col[0]
        year = yearColumn[:4]
        closePrice = col[4]
        
        for data in closePrice:
            stockClosePrice.append(data)
    
        if year not in years_available:
            years_available.append(year)  
    
    return years_available 
"""
new_file = open("C:\\Users\\" + str(getpass.getuser()) + "\\" + ticker + ".csv", "r")
stock_data = new_file.read().splitlines()
del stock_data[0]
new_file.close()

years_available = []
 
#format for years in csv file is different for each computer for some reason, my years are the first 4 digits 
for data in stock_data: 
    col = data.split(",")
    yearColumn = col[0]
    year = yearColumn[:4]

    if year not in years_available:
        years_available.append(year)  

    
#stuff = urllib.urlopen(url)   
#del stock_data[0]
#

f = open("C:\\Users\\" + str(getpass.getuser()) + "\\" + ticker + ".csv", "r")
lines = f.read().splitlines()
del lines[0]
stockClosePrice = []
for line in lines:    
    col = line.split(",")
    closePrice = col[4]
    
    stockClosePrice.append(closePrice)

#print stockClosePrice
floatStockClosePrice = [float(i) for i in stockClosePrice]
floatYearsAvailable = [float(i) for i in years_available]
#print floatStockClosePrice

floatStockClosePrice.reverse()
years_available.reverse()
plt.plot(floatStockClosePrice)
plt.xlabel("Years")
plt.ylabel("Prices")

plt.xticks(range(len(years_available)), years_available)
plt.show()