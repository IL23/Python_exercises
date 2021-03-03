# Ir dots tuple ar vārdiem (“Alex”, “Carl”, “Hannah”).
# Izveidot klasi Student, kurai ir atribūts name.
# Izveidot sarakstu ar Student klases objektiem.


names = ("Alex", "Carl", "Hannah")


class Student:
    def __init__(self, name):
        self.name = name


students_list = [Student(name) for name in names]