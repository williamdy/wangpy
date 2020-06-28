# -*- coding: utf-8 -*-
from django.db import models


# 产品分类表
# class Type(models.Model):
#     id = models.AutoField('id', primary_key=True)
#     type_name = models.CharField('type', max_length=20)
#
#     # 设置返回值
#     def __str__(self):
#         return self.type_name


# 产品信息表
class Product(models.Model):
    id = models.AutoField('id', primary_key=True)
    name = models.CharField('name', max_length=50)
    weight = models.CharField('weight', max_length=20)
    size = models.CharField('size', max_length=20)
    # type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='type')

    # 设置返回值
    def __str__(self):
        return self.name
