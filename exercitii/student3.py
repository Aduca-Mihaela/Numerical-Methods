class Student:
    def __init__(self, nume:str, note:list[int]):
        self.nume=nume
        self.note=note


    def get_Nume(self):
        return self.nume

    def set_nume(self, nume:str):
        self.nume = nume

    def get_note(self):
        return  self.note

    def set_note(self, note: list[int]):
        self.note=note


    def calculeaza_media(self):
        suma=0
        if not self.note:
            return 0
        for nota in self.note:
            suma = suma+nota

        media=suma/len(self.note)
        return media


# Exemplu de utilizare
student = Student("Ion Popescu", [8, 9, 10, 7, 6])
print(f"Numele studentului: {student.nume}")  # Output: Numele studentului: Ion Popescu
print(f"Notele studentului: {student.note}")  # Output: Notele studentului: [8, 9, 10, 7, 6]
print(f"Media notelor: {student.calculeaza_media()}")  # Output: Media notelor: 8.00

student.nume = "Maria Ionescu"
student.note = [10, 9, 8, 9, 10]
print(f"Numele studentului: {student.nume}")  # Output: Numele studentului: Maria Ionescu
print(f"Notele studentului: {student.note}")  # Output: Notele studentului: [10, 9, 8, 9, 10]
print(f"Media notelor: {student.calculeaza_media()}")  # Output: Media notelor: 9.20