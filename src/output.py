from src.student import Student
from src.project import Project

class Output():
    def __init__(self):
        self.OUTPUT_PATH = "output.txt"
        self.clear_output_file()

    def clear_output_file(self):
        with open(self.OUTPUT_PATH, 'r+') as file:
            file.truncate(0)

    def print(self, message):
        with open(self.OUTPUT_PATH, 'a') as file:
            print(message)
            file.write(message + "\n")

    def change(self, assginedStudent: Student, project: Project, studentRemoved: Student = None):
        
        log= None
        if (studentRemoved is None):
            log = f"Student {assginedStudent.id} assigned to project {project.id}"
        else:
            log = f"Student {assginedStudent.id} assigned to project {project.id} and student {studentRemoved.id} was removed"

        self.print(log)
    
    def print_result(self, matching_length: int, matching: dict):
        
        log = None

        log = f"\nIn the final result, the maximum stable matching found was {matching_length}\n"
        self.print(log)

        for(p, project) in matching.items():
            log = f"Project {p}: {[s.id for s in project.selected_students]}"
            self.print(log)
        