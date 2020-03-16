class Person:
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number


class LearnerMixin:
    def __init__(self):
        self.classes = []

    def enrol(self, course):
        self.classes.append(course)


class TeacherMixin:
    def __init__(self):
        self.courses_taught = []

    def assign_teaching(self, course):
        self.courses_taught.append(course)


class Tutor(Person, LearnerMixin, TeacherMixin):
    def __init__(self, teacher_mixin = None, learner_mixin= None, *args, **kwargs,):
        super(Tutor, self).__init__(*args, **kwargs)



class Person:
    def __init__(self, name, surname, number, learner=None, teacher=None):
        self.name = name
        self.surname = surname
        self.number = number

        self.learner = learner
        self.teacher = teacher

    def enrol(self, course):
        if not hasattr(self, "learner"):
            raise NotImplementedError()

        self.learner.enrol(course)

    def assign_teaching(self, course):
        if not hasattr(self, "teacher"):
            raise NotImplementedError()

        self.teacher.assign_teaching(course)
a = Person("Mark","Solopenko", 12, None, None)




