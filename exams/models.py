from django.db import models

# Create your models here.

class Course(models.Model):
    course_name= models.CharField(max_length=200)
    ch_num = models.IntegerField(default=0)
    def __str__(self):
        return self.course_name

class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,default=1)
    ch_name = models.CharField(max_length=200)
    def __str__(self):
        return self.ch_name

class Question(models.Model):
    Objective_Level=(
        (1, "reminding,"),
        (2, "understanding,"),
        (3, "creativity")
    )
    Difficult_level=(
        (0, "simple"),
        (1, "Difficult")      
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE,default=1)
    question_text=models.CharField(max_length=3000)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    q_difficulty = models.IntegerField(choices=Difficult_level,
                  default="simple")
    q_obj=models.IntegerField(choices=Objective_Level,
                  default="reminding")
    f_answer=models.CharField(max_length=200)              
    s_answer=models.CharField(max_length=200)
    correct_answer=models.CharField(max_length=200)

    def __str__(self):
        return self.question_text        

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=300)
    def __str__(self):
        return self.teacher_name

class Exam(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,default=1)
    grade = models.IntegerField(default=0)
    question=models.ManyToManyField(Question,default=1)
 