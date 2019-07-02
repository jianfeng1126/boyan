from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30,null=False)
    userpassward = models.CharField(max_length=50, null=False)

    def __str__(self):
        return "<Emp:({id},{username},{userpassward})>".format(id=self.id, username=self.username, userpassward=self.userpassward)

