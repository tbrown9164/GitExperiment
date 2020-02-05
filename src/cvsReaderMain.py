import csv
import csvReader

columntitle = 'column1'
rownumber = 2
columnnumber = 1


#print ("open the file")

csvReader.OpenandlistAtcolumn('csvfile.csv',0)

columnnumber = csvReader.FindCSVColumnbyTitle('csvfile.csv',columntitle)


rowlist = csvReader.ReturnCSVRowbyRowNumber('csvfile.csv',rownumber)
print("row:",rownumber, "row list: ", rowlist)

field=csvReader.ReturnCSVFieldbyRowAndColumnNumber('csvfile.csv', columnnumber,rownumber)
print("column title",columntitle,"columnnumber:",columnnumber,"row number:",rownumber,"field content",field)



