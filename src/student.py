class Student():
    def __init__(self, id: str, preferences: list[str] , grade: int) -> None:
        self.id = id
        self.preferences = list(preferences)
        self.preferences_list = list(preferences)
        self.grade = grade
        self.project_selected = ""