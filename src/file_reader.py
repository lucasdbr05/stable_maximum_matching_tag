import re 

class FileReader():
    def read_project(self, data: str):
        pattern = r'\((\w+), (\d+), (\d+)\)'
        match = re.match(pattern, data)
        project_code = match.group(1)
        vacancies = int(match.group(2))
        min_grade = int(match.group(3))
        return (project_code, vacancies, min_grade)

    def read_student(self, data: str):
        pattern_3preferences = r'\((\w+)\):\((\w+), (\w+), (\w+)\) \((\d+)\)'
        pattern_2preferences = r'\((\w+)\):\((\w+), (\w+)\) \((\d+)\)' 
        match = None
        for pattern in [pattern_3preferences, pattern_2preferences]:
            match = re.match(pattern, data)
            if match: break
        student = match.group(1)
        projects = [match.group(i) for i in range(2, len(match.groups()))]
        grade = int(match.group(len(match.groups())))
        return (student, projects, grade)
