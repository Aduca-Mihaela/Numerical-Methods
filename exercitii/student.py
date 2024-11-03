class Student:
    def __init__(self, nume :str, media :float):
        self.nume=nume
        self.media=media

    def get_nume(self):
        return self.nume

    def set_nume(self, nume:str):
        self.nume=nume

    def get_media(self):
        return self.media

    def set_media(self, media:float):
        self.media=media


    def toString(self):
        return f"{self.nume} {self.media}"

student = Student("Ion Popescu", 9.5)
#print(student.nume)
#print(student.media)

student.nume = "Maria Ionescu"
student.media = 8.7
#print(student.nume)  # Output: Maria Ionescu
#print(student.media)  # Output: 8.7


# Exemplu de utilizare
student = Student("Ion Popescu", 9.5)
#print(student.toString())  # Output: Ion Popescu 9.5

student.nume = "Maria Ionescu"
student.media = 8.7
#print(student.toString())  # Output: Maria Ionescu 8.7


class StudentBursier(Student):
    def __init__(self, nume:str, media:float, tipBursa: str):
        super().__init__(nume, media)
        self.tipBursa=tipBursa

    def getTip(self):
        return self.tipBursa

    def setBursa(self, tipBursa:str ):
        self.tipBursa=tipBursa

    def toString(self):
        return f"{super().toString()} {self.tipBursa}"



# Exemplu de utilizare
student_bursier = StudentBursier("Ion Popescu", 9.5, "Merit")
#print(student_bursier.toString())  # Output: Ion Popescu 9.5 Merit

student_bursier.nume = "XLORINA Ionescu"
student_bursier.media = 8.7
student_bursier.tipBursa = "Social"
#print(student_bursier.toString())  # Output: Maria Ionescu 8.7 Social

student2=Student("Aduca mihaila", 9.16)


lista_vector = [student_bursier, student, student2]

lista = sorted(lista_vector, key=lambda x: x.get_nume())

for element in lista:
    print(element.toString())
