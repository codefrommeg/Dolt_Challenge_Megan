# This project opens a text file URL, organizes the 
# Webster’s Unabridged Dictionary data (TODO), and then 
# writes it to a CSV. The first word is "A" and the last is "ZYTHUM" 
# -- TODO need to get rid of 1st line and text at bottom.
# -Megan Smith

from urllib.request import urlopen
import parseData
import inputs

#TODO
def main():
    parseData.parseData(inputs.dataUrl)

if __name__ == '__main__':
    main()
