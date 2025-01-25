import csv

def getCsvData(fileName):
    # create an empty list to store rows
    # those values come from the testdata.csv file
    # this list is going to be passed on to the data decorator
    rows = []

    # open the CSV file
    dataFile = open(fileName, "r")

    # create a CSV reader object from the testdata.csv file
    # which is going to read and iterate over the testdata.csv rows data
    reader = csv.reader(dataFile)
    
    # skip the headers, afterwards run the for loop and read the data
    next(reader)

    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows
    


