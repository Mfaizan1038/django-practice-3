from .student import Student  
from .top_student_manager import TopStudentManager
class TopStudent(Student):
    objects = TopStudentManager()
    class Meta:
        proxy = True  
        ordering = ['-marks']  

    def is_topper(self):
       return self.marks >= 90