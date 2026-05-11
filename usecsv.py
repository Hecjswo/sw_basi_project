import csv

def opencsv(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    f.close()
    return output

def writecsv(filename, a_list):
    f = open(filename, 'w', newline = '')
    csvobject = csv.writer(f, delimiter = ',')
    csvobject.writerows(a_list)
    f.close()
