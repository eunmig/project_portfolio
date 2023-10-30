from django.db import models

# Create your models here.
# 영화제목, 줄거리 입력 필드 2개 지정 

class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()