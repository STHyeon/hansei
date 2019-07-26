from django.db import models

class MachineID(models.Model):
    uuid = models.CharField(max_length=255, verbose_name="고유ID", unique=True)
    nickname = models.CharField(max_length=32, verbose_name="닉네임")

    def __str__(self):
        return str(self.nickname)

class Store(models.Model):
    photo = models.ImageField(upload_to='%Y/%m/%d/orig')
    store_name = models.CharField(max_length=255)
    menu = models.TextField(max_length=200)
    tel = models.CharField(max_length=255)
    time = models.TextField(max_length=255)
    day = models.CharField(max_length=255, blank=True)
    park = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=255)
    tag = models.CharField(max_length=222)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.store_name)