from django.db import models

# Create your models here.

class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True) # 금융상품코드
    kor_co_nm = models.TextField()              # 금융회사명
    fin_prdt_nm = models.TextField()            # 금융상품명
    etc_note = models.TextField()               # 금융상품설명
    join_deny = models.IntegerField()           # 가입제한(1:무제한, 2:서민, 3:일부제한)
    join_member = models.TextField()            # 가입대상
    join_way = models.TextField()               # 가입방법
    spcl_cnd = models.TextField()               # 우대조건


class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField(default=-1)
    intr_rate2 = models.FloatField(default=-1)
    save_trm = models.IntegerField()