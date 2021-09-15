from urllib.request import urlopen
import csv

import outputs

def parseData(dataInput):
    # Open URL text file
    openUrl = urlopen(dataInput) 

    # # Read text file to string
    # dataset = str(openUrl.read(), 'utf-8')
    # # print(dataset)

    # Read each line
    lines = openUrl.readlines()

    # Close file
    openUrl.close()

    for line in lines:
        # Remove extra space decode
        line = line.strip()
        line = line.decode()

        # If entire line is uppercase, write to CSV
        if line.isupper():
            lineList = line.split(maxsplit=0) #separates the words so there is one set per cell
            print(lineList)

            # write words to csv, first column
            with open(outputs.filename, 'a', newline='') as f:
                # creating a csv writer object 
                csvwriter = csv.writer(f) 
        
                # writing the data rows 
                csvwriter.writerow(lineList)
        #print(line)