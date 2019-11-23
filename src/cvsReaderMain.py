import csv
import csvReader

columntitle = 'column1'
rownumber = 2

#print ("open the file")

#csvReader.Openandlistacolumn('csvfile.csv',0)

#csvReader.FindColumninCSV('csvfile.csv','column2')

columnnumber=csvReader.FindCSVColumnTitle('csvfile.csv',columntitle)


field=csvReader.ReturnCSVFieldbyRowAndColumnNumber('csvfile.csv', columnnumber,rownumber)
print("column title",columntitle,"columnnumber:",columnnumber,"row number:",rownumber,"field content",field)



