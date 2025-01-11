class Project():
    def __init__(self, id: str, vacancies: int , min_grade: int) -> None:
        self.id = id
        self.vacancies = vacancies
        self.min_grade = min_grade
        self.selected_students = list[str]()
