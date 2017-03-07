
# class and instance

class Student (object);
        def __init__(self,name,score):
                self.name=name
                self.score=score

        def print_score(self):
                print("%s:%s" % (self.name,self.score))

        def get_grade(self):
                if self.score>=90:
                        return 'A'
                elif self.score>=60:
                        return 'B
                else :
                        return 'C'
bart=Student('Bart',59)
lisa=Student ('Lisa',87)

print ('bart.name=',bart.name)
print ('lisa.score=',bart.score)
bart.print_score()

print ('grade of Bart :',bart.get_grade())
print ('grade of Lisa :',lisa.get_grade())

