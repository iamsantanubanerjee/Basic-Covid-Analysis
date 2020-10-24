import pandas as pd
import matplotlib.pyplot as plt

#Importing dataset
url_c = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
url_d = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
url_r = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
confirmed = pd.read_csv(url_c)
death = pd.read_csv(url_d)
recovered = pd.read_csv(url_r)

#Printing global data
print('Total confirmed cases(Globally): ',confirmed.iloc[:,-1].sum())
print('Total Deaths(Globally): ',death.iloc[:,-1].sum())
print('Total Recovered(Globally): ',recovered.iloc[:,-1].sum())

#Grouping data by country
confirmed_by_country = confirmed.groupby(['Country/Region'])[confirmed.columns[4:]].sum()
death_by_country = death.groupby(['Country/Region'])[confirmed.columns[4:]].sum()
recovered_by_country = recovered.groupby(['Country/Region'])[confirmed.columns[4:]].sum()
active_by_country = confirmed_by_country - death_by_country - recovered_by_country

#Creating a concise table
data = [confirmed_by_country.iloc[:,-1],recovered_by_country.iloc[:,-1],death_by_country.iloc[:,-1]]
headers = ['Confirmed','Recovered','Death']
table1 = pd.concat(data,axis = 1,keys=headers)
table1['Active'] = table1['Confirmed'] - table1['Death'] - table1['Recovered']
table1['Deaths per 100 people affected'] = (table1['Death'] / table1['Confirmed']) * 100
#table1.sort_values('Confirmed', ascending= False).head(25).to_csv(r'/home/santanu/Desktop/Global Chart.csv')

#Printing the table with top 25 countries in the confirmed column
print(table1.sort_values('Confirmed', ascending= False).head(25))

#Adding a total row so that we can plot and see growth of virus globally over time
confirmed_by_country.loc['Total'] = confirmed_by_country.sum()
death_by_country.loc['Total'] = death_by_country.sum()
recovered_by_country.loc['Total'] = recovered_by_country.sum()

#Adding a row at bottom calculating the daily new cases
confirmed_by_country.loc['Daily New Cases'] = confirmed_by_country.loc['Total'].diff()

table1.sort_values('Confirmed', ascending= True).tail(25).plot.barh(y = 'Confirmed', color = 'b')
plt.xlabel('Number of cases')
plt.show()

#Plotting the graph
'''labels = []
for i in range(0,len(confirmed_by_country.columns),10):
    labels.append(i)
line1, = plt.plot(confirmed_by_country.columns.values,confirmed_by_country.loc['India'].values,'b',marker = '.')
line2, = plt.plot(recovered_by_country.columns.values,recovered_by_country.loc['India'].values,'g',marker = '.')
line3, = plt.plot(death_by_country.columns.values,death_by_country.loc['India'].values,'r',marker = '.')
line4, = plt.plot(active_by_country.columns.values,active_by_country.loc['India'].values,'c',marker = '.')
#plt.yscale('log')
plt.xticks(labels)
plt.xlabel('Date')
plt.ylabel('Number of cases')
plt.legend((line1, line2, line3, line4), ('Confirmed', 'Recovered', 'Death', 'Active'))
plt.show()'''

#Calculating daily new cases and plotting them over time
'''labels = []
for i in range(0,len(confirmed_by_country.columns),10):
    labels.append(i)
plt.plot(confirmed_by_country.columns.values,confirmed_by_country.loc['Daily New Cases'].values,'g',marker = '.')
plt.xticks(labels)
plt.xlabel('Date')
plt.ylabel('Daily new cases (Globally)')
plt.show()'''

#Comparing cases of 7 countries (Top European countries and some neighbours of India)
'''labels = []
for i in range(0,len(confirmed_by_country.columns),10):
    labels.append(i)
line1, = plt.plot(confirmed_by_country.columns.values,confirmed_by_country.loc['US'].values,'b',marker = '.')
line2, = plt.plot(confirmed_by_country.columns.values,confirmed_by_country.loc['Spain'].values,'g',marker = '.')
line3, = plt.plot(confirmed_by_country.columns.values,confirmed_by_country.loc['Italy'].values,'r',marker = '.')
line4, = plt.plot(confirmed_by_country.columns.values,confirmed_by_country.loc['India'].values,'c',marker = '.')
line5, = plt.plot(confirmed_by_country.columns.values,confirmed_by_country.loc['China'].values,'m',marker = '.')
line6, = plt.plot(confirmed_by_country.columns.values,confirmed_by_country.loc['Japan'].values,'y',marker = '.')
line7, = plt.plot(confirmed_by_country.columns.values,confirmed_by_country.loc['Indonesia'].values,'k',marker = '.')
plt.xlabel('Date')
plt.ylabel('Number of cases')
plt.xticks(labels)
#plt.yscale('log')
plt.legend((line1, line2, line3, line4, line5, line6, line7),('US', 'Spain', 'Italy', 'India', 'China', 'Japan', 'Indonesia'))
plt.show()'''
