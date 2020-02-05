import csv

def OpenandlistAtcolumn(filename,column_number):
    with open(filename) as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:      #column names
                print (row[column_number])
                line_count +=1
            else:
                print(row[column_number])
    csv_file.close()


def FindCSVColumnbyTitle(filename,columnName):
    with open(filename, 'r') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        column_iterator=0
        for row in fieldnames:
             if columnName == fieldnames[column_iterator]:
                 print("we have a match",columnName,"at row",column_iterator)
                 break
             column_iterator+=1
    infile.close()
    return column_iterator

def ReturnCSVFieldbyRowAndColumnNumber(filename,columnNumber,rownumber):
    with open(filename) as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=',')
        line_count: int = 0
        for row in csv_reader:
            if line_count == rownumber:      #column names
                print ("field value at row number",row[columnNumber])
                break
            line_count +=1

    csv_file.close()
    return row[columnNumber]

#returns a list for the row
def ReturnCSVRowbyRowNumber(filename,rownumber):
    with open(filename) as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=',')
        line_count: int = 0
        for row in csv_reader:
            if line_count == rownumber:      #column names
                #print ("value at row number",row)
                break
            line_count +=1

    csv_file.close()
    return row








