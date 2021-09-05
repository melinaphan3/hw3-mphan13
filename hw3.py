#question1
import time
start = time.time()

def FizzBuzz():
for num in range(1, 100):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')

    elif num % 3 == 0:
        print('Fizz')
    
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

seconds = time.time() - start

print('It took', seconds, 'seconds to execute the program')

#https://stackoverflow.com/questions/14452145/how-to-measure-time-taken-between-lines-of-code-in-python

#question2
def VolumeofSphere(R):
    pi = 3.14
    result = (4/3) * pi
    
    R = R ** (1/3.)
    result = result * R
    return result

print(VolumeofSphere(20))
csvPath = "/home/mphan13/hw3/"

list = []
with open (csvPath, newline = '') as csv file:
    line = csv.reader (csv file, del)

    for row in line:
        list.append(row)

list.pop(0)

#https://newbedev.com/how-to-read-and-write-csv-file
#https://docs.python.org/3/library/csv.html

#question3
import csv
def getCsv(booksDict, csvFile):

    keys = list(booksDict.keys())
    items = booksDict[keys[0]]
    f = open(csvFile, "w")

    for j in range(len(items)):
        prt = ""

    for key in booksDict:
        prt += booksDict[key][j] +"," 

        f.write(prt[:-1]+"\n")

    f.close()
    print("\nBooks data have been written to the file", csvFile, "\n")

#question4
import csv

with open('books.csv', mode = 'r') as infile:
    reader = csv.reader(infile)
    with open('coors_new.csv', mode='w') as outfile:
    writer = csv.writer(outfile)
    for rows in reader:
        k = rows[0]
        v = rows[1]
        mydict = {k:v for k, v in rows}
    print(mydict)

#https://stackoverflow.com/questions/6740918/creating-a-dictionary-from-a-csv-file

#question5
def readWrite(booksDict, csvFile):

    keys = list(booksDict.keys())
    items = booksDict[keys[0]]
    f = open(csvFile, "w")

    for j in range(len(items)):
        prt = ""
    for key in booksDict:
        prt += booksDict[key][j] +"," 

    f.write(prt[:-1]+"\n")
    f.close()

    print("\nBooks data have been written to the file", csvFile, "\n")  

    try:
        fhand = open(csvFile)
    except:
        print("can't open the file: " + csvFile)
        exit()
    
    books = {
        "Title" : [],
        "Author" : [],
        "ISBN13" : [],
        "Pages" : []
    }

    lineNum = 1 
    for line in fhand:

        if(line[-1] == "\n"):
            line = line[:-1]
        records = list(map(str, line.split(",")))    

        if lineNum == 1:
            lineNum +=1    
        else:
            books["Title"].append(records[0])   
            books["Author"].append(records[1])    
            books["ISBN13"].append(records[2])   
            books["Pages"].append(records[3]) 

    f = open(csvFile, "w")
    f.write("")
    f.close()

    print("\nDictionary object has been created, \n\nData has been deleted from the temporary file!!!")
    return books           

if __name__ == "__main__":
    
    booksDict = {'Title': ['1984', 'Animal Farm', 'Brave New World', 'Fahrenheit 451', 'Jane Eyre', 'Wuthering Heights', 'Agnes Grey', 'Walden', 'Walden Two', '"Eats Shoots & Leaves"'], 'Author': [' George Orwell', ' George Orwell', ' Aldous Huxley', ' Ray Bradbury', ' Charlotte BrontÃ«', ' Emily BrontÃ«', ' Anne BrontÃ«', ' Henry David Thoreau', ' B. F. Skinner', ' Lynne Truss'], 'ISBN13': [' 978-0451524935', ' 978-0451526342',
    ' 978-0060929879', ' 978-0345342966', ' 978-0142437209', ' 978-0141439556', '978-1593083236', ' 978-1420922615', ' 978-0872207783', ' 978-1592400874'], 'Pages': [' 268', ' 144', ' 288', ' 208', '532', ' 416', ' 256', ' 156', ' 301', '209']}

    returnedDict = readWrite(booksDict, "books.csv")

    print("\nFollowing is the dictionary: \n\n", returnedDict, "\n")

    #https://docs.python.org/3/library/tempfile.html
