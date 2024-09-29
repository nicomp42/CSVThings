# utils.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

import csv
def read_CSV_file():
    '''
    Read a particular CSV file into a list of lists.
    monroe-county-crash-data2003-to-2015.csv
    The first row is assumed to be a header and is skipped
    @return list: the list of lists that was created from the file
    '''
    csv_data = []
    # In a Visual Studio project, the default folder is the project folder. It is not the package containing the entry point. 
    with open("./dataFiles/monroe-county-crash-data2003-to-2015.csv", newline='') as f:
        reader = csv.reader(f, delimiter=',')
        header = next(reader)
    #   csv_data.append(header)        # We don't want the header row.
        for row in reader:
            csv_data.append(row)
    
    #print(csv_data)
    #print (type(csv_data))      # It's a list of lists!
    return csv_data