import time

__info__ = \
    f"""
    Henry Post,
    Lab 06: OOP With Classes

    ITMD413,
    IIT Spring 2018,
    Ran on {time.strftime("%c")}
    """


class Student:
    Scores = {}

    def __init__(self, name, grade):  # Initializing constructor method
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"{self.name}: {self.grade}"

    def getScores(self):
        answer_key = []
        # read into answer_key list, the answer key from file
        answer_key = [line.strip() for line in open("answers.txt", 'r')]

        student_answers = []
        # read into student_answers list, student answers from file
        student_answers = [line.strip().split(',') for line in open("data.txt", 'r')]

        total_score = 100

        '''
        Finish the processing logic below marked within the commented lines to
        correctly grade each student by creating a loop(s) to correctly score
        students using the lists created above (namely the answer_key list and
        the student_answers list) by matching each of the student answers to
        each answer key item

        Each incorrect answer deducts 10 points from the 'total_score'
        variable shown (intialized) just above
        '''

        # ---start your loop processing logic here---#

        student_answers_d = {}

        for answer in student_answers:
            name = answer[0]
            answers = answer[1:]
            student_answers_d[name] = answers

        for i in range(len(student_answers_d[self.name])):
            if student_answers_d[self.name][i] != answer_key[i]:
                total_score -= 10

        # ---end your loop processing logic here---#

        Student.Scores[self.getName()] = total_score;

    def getName(self):
        return self.name;

    @staticmethod
    def sortDict():
        return sorted(Student.Scores.items());


student_objs = [
    Student(line.split(',')[0], -1) for line in open("data.txt", 'r')
]

for index in range(len(student_objs)):
    student_objs[index].getScores();

sortList = Student.sortDict();

for k, v in sortList:
    print(k, "has score:", v)
