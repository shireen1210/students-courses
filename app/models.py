from django.db import models

# Create your models here.

class Course(models.Model):
    cname=models.CharField(max_length=255)
    cid=models.CharField(max_length=255)
    
    totalenrolled=models.CharField(max_length=255)

    def __str__(self):
        return self.cid
    

class Student(models.Model):
    # studentid=models.CharField(max_length=255)
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    contactnum=models.CharField(max_length=255)
    estatus=models.BooleanField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    dateenrolled=models.DateTimeField(auto_now_add=True)
    image=models.FileField(upload_to="blog/app/media/posts", null=True, blank=True)
    
    def __str__(self):
        return self.firstname
    


    



