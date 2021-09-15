from urllib.request import urlopen
import csv

import outputs
import clearCsv

def parseData(dataInput):
    # Opens and clears existing CSV file
    clearCsv.clearCsv()

    # Open URL text file
    openUrl = urlopen(dataInput) 

    # Read each line
    lines = openUrl.readlines()

    # Close file
    openUrl.close()

    for line in lines:
        # Remove extra characters, decode
        line = line.strip()
        line = line.decode()

        # Dictionary words - if entire line is uppercase, write to CSV TODO get rid of first line and text at end
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
    