from src.file_reader import FileReader
from src.project import Project
from src.student import Student
from src.output import Output
from copy import deepcopy
from random import shuffle


class Graph ():
    def __init__(self, message: Output):
        self.INPUT_PATH = "input.txt"
        self.N_STUDENTS = 200
        self.N_PROJECTS = 55
        self.messager = message

        self.reader = FileReader() 
        self.original_students = dict()
        self.original_projects = dict()
        self.students = dict()
        self.projects = dict()
        self.studentsNotAssigned = list()

        self.student_matching = dict()
        self.project_matching = dict()

    def addStudentInProject(self, student: Student, project: Project, studentToRemove: Student = None):
        self.messager.change(student, project, studentToRemove)
        if (studentToRemove is not None):
            if len(studentToRemove.preferences) > 0:
                self.studentsNotAssigned.append(studentToRemove.id)
            self.project_matching[project.id] = [s for s in self.project_matching[project.id] if s.id != studentToRemove.id]
            self.student_matching[studentToRemove.id] = ''
            # studentToRemove.preferences.remove(project.id)
            studentToRemove.project_selected = ''
            self.students[studentToRemove.id] = studentToRemove

        self.project_matching[project.id].append(student)
        self.student_matching[student.id] = project.id
        student.project_selected = project.id
        self.students[student.id] = student

        self.project_matching[project.id] = sorted(self.project_matching[project.id], key= lambda x: x.grade)
        project.selected_students = list(self.project_matching[project.id])
        self.projects[project.id] = project


    def build_graph(self):
        with open(self.INPUT_PATH, 'r') as file:
            for _ in range(self.N_PROJECTS):
                project, vacancies, min_grade = self.reader.read_project(next(file))
                self.project_matching[project] = list()
                self.projects[project] = Project(project, vacancies, min_grade)
                self.original_projects[project] = Project(project, vacancies, min_grade)
            for _ in range(self.N_STUDENTS):
                student, preferences, grade = self.reader.read_student(next(file)) 
                self.student_matching[student]  = ''
                self.students[student] = Student(student, preferences, grade)
                self.original_students[student] = Student(student, preferences, grade)
            self.studentsNotAssigned = list(self.student_matching.keys())

    def reset_graph(self):
        for project in self.projects:
            self.project_matching[project] = list()
            self.projects[project] = deepcopy(self.original_projects[project])
        for student in self.students:
            self.student_matching[student]  = ''
            self.students[student] = deepcopy(self.original_students[student])
        self.studentsNotAssigned = list(self.student_matching.keys())
        shuffle(self.studentsNotAssigned)
            
    def GaleShapley(self):

        while len(self.studentsNotAssigned) > 0:
            student = self.studentsNotAssigned.pop()
            student = self.students[student]

            project = student.preferences.pop(0)
            project = self.projects[project]

            if(self.student_matching[student.id]): 
                continue

            if(student.grade < project.min_grade): 
                if(len(student.preferences) > 0):
                    self.studentsNotAssigned.append(student.id)
                continue
            flag = False
            
            if len(self.project_matching[project.id]) < project.vacancies:
                self.addStudentInProject(student, project)
                flag = True
                continue

            elif len(self.project_matching[project.id]) == project.vacancies:
                for currentSelectedStudent in self.project_matching[project.id]: 
                    if (student.grade > currentSelectedStudent.grade):
                        self.addStudentInProject(student, project, currentSelectedStudent)
                        flag = True
                        break    
                    elif (
                        (student.grade == currentSelectedStudent.grade) and
                        (student.preferences_list.index(project.id) < currentSelectedStudent.preferences_list.index(project.id))
                    ):
                        self.addStudentInProject(student, project, currentSelectedStudent)
                        flag = True
                        break    
            
            if (not flag):
                if (len(student.preferences)>0):
                    self.studentsNotAssigned.append(student.id)

    
    def getStudentsSelectedQuantity(self):
        return sum([len(s) for (s) in self.project_matching.values()])