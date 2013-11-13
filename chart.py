

#!/usr/bin/python

# This demo example uses xlsxwriter module to demonstrate the 
#   creation of simple Excel charts using python

import xlsxwriter

#create a workbook
workbook = xlsxwriter.Workbook('chart.xlsx')
 
#creates a worksheet inside workbook
worksheet = workbook.add_worksheet()

#adds chart to workbook and returns a chart object , type of chart is passed as a dictionary argument
chart = workbook.add_chart({'type': 'bar'})

#creates a list of data columns and rows
data = [
    [1, 2, 3, 4, 5],
    [2, 4, 6, 8, 10],
    [3, 6, 9, 12, 15],
]

#writes data-list items to excel specific columns
worksheet.write_column('A1', data[0])
worksheet.write_column('B1', data[1])
worksheet.write_column('C1', data[2])

#adding data values to be used for creatig the chart

chart.add_series({'values': '=Sheet1!$A$1:$A$5'})
chart.add_series({'values': '=Sheet1!$B$1:$B$5'})
chart.add_series({'values': '=Sheet1!$C$1:$C$5'})
worksheet.insert_chart('A7', chart)
workbook.close()
