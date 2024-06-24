from abc import ABC, abstractmethod

class Ward:
    def __init__(self, ward_name):
        self.__ward_name = ward_name
        self.__list_person = list()

    def add_person(self, person):
        self.__list_person.append(person)

    def describe(self):
        print(f'ward name: {self.__ward_name}')
        for p in self.__list_person:
            p.describe()

    def count_doctor(self):
        counter = 0
        for p in self.__list_person:
            if isinstance(p, Doctor):
                counter += 1
        return counter

    def sort_age(self):
        return self.__list_person.sort(key=lambda x: x.get_yob(), reverse=True)
    
    def compute_average(self):
        total = 0
        counter = 0
        for t in self.__list_person:
            if isinstance(t, Teacher):
                counter += 1
                total += t.get_yob()
        return total/counter

class Person(ABC):
    def __init__(self, person_name, yob):
        self._person_name = person_name
        self._yob = yob
        
    def get_yob(self):
        return self._yob
    
    @abstractmethod
    def describe(self):
        pass

class Student(Person):
    def __init__(self, person_name, yob, grade):
        super().__init__(person_name=person_name, yob=yob)
        self.__grade = grade

    def describe(self):
        print(f'Name: {self._person_name}, Yob: {self._yob}, Grade: {self.__grade}')

class Teacher(Person):
    def __init__(self, person_name, yob, subject):
        super().__init__(person_name=person_name, yob=yob)
        self.__subject = subject

    def describe(self):
        print(f'Name: {self._person_name}, Yob: {self._yob}, Subject: {self.__subject}')

class Doctor(Person):
    def __init__(self, person_name, yob, specialist):
        super().__init__(person_name=person_name, yob=yob)
        self.__specialist = specialist

    def describe(self):
        print(f'Name: {self._person_name}, Yob: {self._yob}, Specialist: {self.__specialist}')


if __name__ == "__main__":
    student1 = Student(person_name="studentA", yob=2010, grade="7")
    student1.describe()

    teacher1 = Teacher(person_name="teacherA", yob=1969, subject="Math")
    teacher1.describe()

    doctor1 = Doctor(person_name="doctorA", yob=1945, specialist="Endocrinologists")
    doctor1.describe()

    # 2(b)
    print()
    teacher2 = Teacher(person_name="teacherB", yob=1995, subject="History")
    doctor2 = Doctor(person_name="doctorB", yob=1975, specialist="Cardiologists")
    ward1 = Ward(ward_name="Ward1")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    ward1.describe()

    # # 2(c)
    print(f"\nNumber of doctors: {ward1.count_doctor()}")

    # # 2(d)
    print("\nAfter sorting Age of Ward1 people")
    ward1.sort_age()
    ward1.describe()

    # # 2(e)
    print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")
