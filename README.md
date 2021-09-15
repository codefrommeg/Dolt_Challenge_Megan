# Dolt_Challenge_Megan
 Webster’s Unabridged Dictionary to CSV
 DoltHub Challenge - Megan Smith - 09/14/2021

 Files:
    challengeAccepted.py - main file, run challengeAccepted.py
    dictionary.csv - the CSV results
    identifyWord.py
    inputs.py - input file path and field labels
    outputs.py - outful CSV file name
    parseData.py - loads and parses the data

Notes:
Original file - https://www.gutenberg.org/cache/epub/29765/pg29765.txt

Data: Webster’s Unabridged Dictionary
Components: word, # of versions/uses of the word?, part of speech (“n.” "adj.” “v.” “p.”), definition (“Defn:”), etymology (“Etym:”), example

Dictionary
    Word (A-Z) - these are in all caps
        n. adj. p. v. -- etc.
        Defn:
        Etym:

Strategy
    Identify the parts of a dictionary
    Get data from the URL
    Recognize patterns in the data
    Write to CSV

Python Pandas?

Resources:
https://www.superteacherworksheets.com/dictionary-skills/dictionary-parts_PARTS.pdf 

https://www.dictionary.com/e/parts-of-speech/ 

https://www.bragitoff.com/2016/03/english-dictionary-in-csv-format/

https://www.mso.anu.edu.au/~ralph/OPTED/

https://www.quora.com/Where-can-I-find-an-English-dictionary-as-a-text-or-SQL-file 

https://github.com/grantshandy/webster-dictionary-json

https://webdamn.com/write-data-to-csv-file-using-golang/
