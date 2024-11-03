class Student:
    def __init__(self, nume:str, note:list[int]):
        self._nume = nume
        self._note = note

    def get_nume(self):
        return self._nume

    def set_nume(self, nume1):
        self._nume = nume1

    def get_note(self):
        return self._note

    def set_note(self, note1:list[int]):
        self._note = note1

    def medie(self):
        sum = 0;
        for nota in self._note:
            sum = sum + nota
        return sum/len(self._note)

    def notepeste4(self):
        for nota in self._note:
            if nota <= 4:
                return False
        return True

def toatepeste4(stud:Student):
    for nota in stud.get_note():
        if nota <=4 :
            return False

    return True


def abc(stud:Student):
    numestud=stud.get_nume()
    note=stud.get_note()
    note.sort(reverse=True)

    print(f"nume:{numestud}, note: {note} ")



student = Student("Mihaila aduca", [8,6,7,8,9])

abc(student);