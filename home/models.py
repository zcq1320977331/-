from django.db import models
# $ python manage.py migrate   # 创建表结构
# $ python manage.py makemigrations home  # 让 Django 知道我们在我们的模型有一些变更
# $ python manage.py migrate home   # 创建表结构
# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=200)