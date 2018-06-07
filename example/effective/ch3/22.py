import collections

Grade = collections.namedtuple('grade', ('score', 'weight'))

class SimpleGradebook(object):


    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return round(sum(grades) / float(len(grades)), 2)

book = SimpleGradebook()
book.add_student('Danny Hsiao')
book.report_grade('Danny Hsiao', 90)
book.report_grade('Danny Hsiao', 70)
book.report_grade('Danny Hsiao', 70)
print(book.average_grade('Danny Hsiao'))


class BySubjectGradebook(object):


    def __init__(self):
        self.__grades = {}
    
    def add_student(self, name):
        self.__grades[name] = {}
    
    def report_grade(self, name, subject, grade):
        by_subject = self.__grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(grade)
    
    def average_grade(self, name):
        by_subject = self.__grades[name]
        total, count = 0.0, 0.0 
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return round((total / count), 2)      

book2 = BySubjectGradebook()
book2.add_student('a')
book2.report_grade('a', 'math', 100)
book2.report_grade('a', 'chinese', 90)
book2.report_grade('a', 'math', 90)
print(book2.average_grade('a'))

class WeightedGradebook(object):
    
    
    def report_grade(self, naem, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append((score,weight))
    
    def average_grade(self, name):
        by_subject = self._grades[name]
        score_sum, score_count = 0.0, 0.0
        for subject, score in by_subject.items():
            subject_avg, total_weight = 0.0, 0.0
            for score, weight in scores:
                score = score * weight
        return round(score_sum / score_count)           










