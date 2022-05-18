from django.db import models


class chat(models.Model):
    message = models.CharField(max_length=1000)
    message_time = models.DateTimeField(auto_now=True)
    Group_name = models.ForeignKey('Group',on_delete=models.CASCADE)


class Group(models.Model):
        name = models.CharField(max_length=256)
 
        def __str__(self):
           return self.name
  