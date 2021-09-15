import outputs

def clearCsv():
    fileVariable = open(outputs.filename, 'r+')
    fileVariable.truncate(0)
    fileVariable.close()