class Student:
    def __init__(self, nume: str, note: list[int]):
        self.nume = nume
        self.note = note


    def get_nume(self):
        return self.nume

    def set_nume(self, value:str):
        self.nume = value

    def get_note(self):
        return self.note

    def set_note(self, note:list[int]):
        self.note=note

    def getNotePeste4(Student):
        for nota in Student.get_note():
            if nota <= 4:
                return False
            return True

# Exemplu de utilizare
student = Student("Ion Popescu", [8, 9, 10, 7, 6])
print(f"Numele studentului: {student.nume}")  # Output: Numele studentului: Ion Popescu
print(f"Notele studentului: {student.note}")  # Output: Notele studentului: [8, 9, 10, 7, 6]
print(f"Media notelor: {student.getNotePeste4()}")  # Output: Media notelor: 8.00

student.nume = "Maria Ionescu"
student.note = [10, 9, 8, 9, 10]
print(f"Numele studentului: {student.nume}")  # Output: Numele studentului: Maria Ionescu
print(f"Notele studentului: {student.note}")  # Output: Notele studentului: [10, 9, 8, 9, 10]
print(f"Media notelor: {student.getNotePeste4()}")  # Output: Media notelor: 9.20
