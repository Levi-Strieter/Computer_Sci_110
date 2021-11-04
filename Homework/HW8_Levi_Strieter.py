from urllib.request import urlopen
# Problem P8.2
finished = False
while finished == False:
    try:
        content = urlopen("https://www.gutenberg.org/files/11/11-0.txt")
        phrase = "Alice"
        repeat = 0
        
        for x in content: 
            if phrase == x: 
                repeat += 1
        finished = True
    except IOError as error:
        print(error)
   
print(repeat)
    


# Problem P8.5

# class GradeBook:
#     def __init__(self):
#         self._gradeBook = dict()
#     def addStudent(self, name):
#         self._gradeBook[name] = "N/A"
#     def deleteStudent(self, name):
#         self._gradeBook.pop(name)
#     def modifyGrade(self, name, grade):
#         self._gradeBook[name] = grade
#     def returnGrades(self):
#         return self._gradeBook

# choices = {
#     1: "Add Student",
#     2: "Remove Student",
#     3: "Modify grades",
#     4: "Print all grades"
# }

# finished = False 
# book = GradeBook()
# while finished == False:
#     for k,v in choices.items():
#         print(k,"-",v)
#     option = int(input("Enter Choice: "))
#     if option not in choices.keys(): print("[!] invalid option [!]\n")

#     if option == 1:
#         userInput = input("Name of student: ").lower()
#         book.addStudent(userInput)
#     elif option == 2:
#         userInput = input("Name of student to remove: ").lower()
#         book.deleteStudent(userInput)
#     elif option == 3:
#         userInput = input("Name of student: ").lower()
#         grade = input("Grade of Student: ").upper()
#         book.modifyGrade(userInput, grade)
#     elif option == 4:
#         grades = book.returnGrades()
#         for x, y in grades.items():
#             print(x, "-", y)



# Problem P8.17 REVISED
from urllib.request import urlopen
finished = False
while finished == False:
    try:
        content = urlopen("https://www.openintro.org/data/tab-delimited/cia_factbook.txt").read()
        for line in content:
            print(line)
        finished = True
    except IOError as error:
        print(error)
   
    



    
