from src.student import Student
class Project():
    def __init__(self, id: str, vacancies: int , min_grade: int) -> None:
        self.id = id
        self.vacancies = vacancies
        self.min_grade = min_grade
        self.selected_students = list[str]()

    def add(self, student: Student):
        self.selected_students.append(student)
        self.selected_students = sorted(self.selected_students, key= lambda x: x.grade)
        
    def remove(self, studentId: str):
        self.selected_students = [s for s in self.selected_students if s.id != studentId]