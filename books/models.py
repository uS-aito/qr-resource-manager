from django.db import models
import uuid
import os.path

# Create your models here.
class Resource(models.Model):
    """
    リソースのモデル
    resource_name: リソース名(str: 200文字以内)
    resource_image: リソースイメージ
    resource_checkout_date: リソース貸出日
    resource_return_date: リソース返却日
    """
    def get_image_path(self, filename):
        """uuid v4でファイル名をリネームする関数"""
        PREFIX = "/images"
        name = str(uuid.uuid4()).replace("-", "")
        extention = os.path.splitext(filename)[-1]
        return PREFIX + name + extention

    resource_name = models.CharField(max_length=200)
    resource_image = models.ImageField(upload_to=get_image_path)
    resource_checkout_date = models.DateField()
    resource_return_date = models.DateField()