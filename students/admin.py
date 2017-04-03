from django.contrib import admin

# Register your models here.


from models.students  import Student
from models.groups import Group
from models.exams import Exam

admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Exam)
