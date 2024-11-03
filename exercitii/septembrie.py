class Student:
    def __init__(self, nume:str, media:float):
        self._nume = nume
        self._media = media

    def get_nume(self):
        return self._nume

    def set_nume(self, nume1:str):
        self._nume = nume1


    def get_media(self):
        return self._media

    def set_media(self, media1:float):
        self._media = media1

    def toString(self):
        return f"{self._nume} {self._media}"


class StudentBursier(Student):
    def __init__(self, nume:str, media:float, tipBursa:str):
        super().__init__(nume, media)
        self.__tipBursa = tipBursa

    def get_tipbursa(self):
        return self.__tipBursa

    def set_tipbrusa(self, tipBursa1):
        self.__tipBursa = tipBursa1

    def toString(self):
        return f"{super().toString()} {self.__tipBursa}"



student = Student("Mihaila Aduca", 9.00)
print(student.toString())

student_bursier=StudentBursier("Muha Alecsanda", 10, "merit")
print(student_bursier.toString())

#VECTOR
vector = [
    Student("Mihaila Aduca", 9.00),
    Student("AAA Aduca", 9.00),
    StudentBursier("C NAECBR", 10, "MERIT")
]

vector1 = sorted(vector, key=lambda student:student._nume)

def ord(vector1):
    return vector1.sort(key=lambda x:x.nume)
for i in vector1:
    print(i.toString())


#vector<StudentBursier> filter(vector<StudentBursier> stud, float nota, string tipBursa){
 #vector<StudentBursier> rez;
# for(size_t i =0; i<size(stud), i++){
#     if (stud[i].get_media() > nota and stud[i].get_tipbursa() == tipBursa){
 #    rez.push_back(stud[i]);
  #   }
   # }
 #return rez;}
