from django.db import models
from db.base_model import BaseModel
# Create your models here.

class PassportManager(models.Manager):
    def add_one_passport(self,username,password,email):
        passport = self.model
        user=passport(username=username,password=password,email=email)
        user.save()
        return user

class Passport(BaseModel):
    username=models.CharField(max_length=24,unique=True,verbose_name='用户名')
    password=models.CharField(max_length=40,verbose_name='密码')
    email=models.EmailField(verbose_name='邮箱地址')
    objects=PassportManager()

    class Meta:
        db_table = 's_user_account'


