import datetime
class student:
    def __init__(self, name, birthday, date_of_joining, marks, salery):
        self.name = name
        self.birthday = birthday
        self.date_of_joining = date_of_joining
        self.marks = marks
        self.salery = salery

    def avarage_mark(self):
        '''визначення середнього балу'''
        self.n = 0
        for i in range(len(self.marks)):
            self.n += self.marks[i][1]
        print(self.n / len(self.marks))

    def bed_marks(self):
        '''виведення дисциплін, бал з яких є нижчим за середній'''
        self.bad = []
        self.n = 0
        for i in range(len(self.marks)):
            self.n += self.marks[i][1]
        self.n = self.n / len(self.marks)
        for i in range(len(self.marks)):
            if self.marks[i][1] < self.n:
                self.bad.append(self.marks[i][0])
        print(self.bad)

    def age(self):
        '''знаходження віку студента'''
        self.n = 0
        if datetime.datetime.today().month <= self.birthday[1] and (datetime.datetime.today().day < self.birthday[0]):
            self.n = 1
        print(datetime.datetime.today().year - self.birthday[2] - self.n)

    def end_of_suffering(self):
        '''знаходження року закінчення навчання'''
        print(self.date_of_joining + 6)




# student1 = student('myro',(25,6,2003),2020,(['discret',3],['math',4],['programming',5]),54)
# student1.avarage_mark()
# student1.bed_marks()
# student1.age()
# student1.end_of_suffering()