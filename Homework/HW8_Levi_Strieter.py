# # Problem P8.2
finished = False
while finished == False:
    try:
        content = open("Homework/11-0.txt", "r", encoding="utf8")
        phrase = "Alice"
        repeat = 0
        for line in content:
            for x in line.rstrip().strip(",").split(" "):
                if x == phrase: repeat += 1
        finished = True
    except IOError as error:
        print(error)
    finally:
        content.close()
   
print(phrase, "is repeated", repeat, "times")
    


# Problem P8.5

class GradeBook:
    def __init__(self):
        self._gradeBook = dict()
    def addStudent(self, name):
        self._gradeBook[name] = "N/A"
    def deleteStudent(self, name):
        self._gradeBook.pop(name)
    def modifyGrade(self, name, grade):
        self._gradeBook[name] = grade
    def returnGrades(self):
        return self._gradeBook

choices = {
    1: "Add Student",
    2: "Remove Student",
    3: "Modify grades",
    4: "Print all grades"
}

finished = False 
book = GradeBook()
while finished == False:
    for k,v in choices.items():
        print(k,"-",v)
    option = int(input("Enter Choice: "))
    if option not in choices.keys(): print("[!] invalid option [!]\n")

    if option == 1:
        userInput = input("Name of student: ").lower()
        book.addStudent(userInput)
    elif option == 2:
        userInput = input("Name of student to remove: ").lower()
        book.deleteStudent(userInput)
    elif option == 3:
        userInput = input("Name of student: ").lower()
        grade = input("Grade of Student: ").upper()
        book.modifyGrade(userInput, grade)
    elif option == 4:
        grades = book.returnGrades()
        for x, y in grades.items():
            print(x, "-", y)



# Problem P8.17 REVISED
from urllib.request import urlopen
from urllib.request import Request
finished = False
while finished == False:
    try:
        raw_request = Request('https://www.openintro.org/data/tab-delimited/cia_factbook.txt')
        raw_request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0')
        raw_request.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
        resp = urlopen(raw_request)
        raw_html = resp.read().decode("UTF-8")
        data = str(raw_html).replace("\n", "\t").split("\t")
        finished = True
    except IOError as error:
        print(error)
        finished = True 
country = {}

for x in range(11, len(data), 11):
    if x == 2860:
        break
    country[data[x].lower()] = data[x+1]

finished = False
while finished == False:
    userInput = input("Enter a country name (q to quit): ").lower()
    if userInput in country:
        print("Area Code:", country[userInput])
    elif userInput == "q":
        print("See ya later!")
        finished = True
    else:
        print("That country is not in our database")


