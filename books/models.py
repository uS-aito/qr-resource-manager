from django.db import models
from django.conf import settings
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
        """
        uuid v4でファイル名をリネームする関数
        :param filename: 元のファイル名
        :return: uuidによるファイル保存パス
        """
        PREFIX = "images/"
        name = str(uuid.uuid4()).replace("-", "")
        extention = os.path.splitext(filename)[-1]
        return PREFIX + name + extention

    def delete_previous_file(function):
        """
        画像差し替え時に古いファイルを削除するデコレータ
        :param function: メイン関数
        :return: wrapper
        """
        def wrapper(*args, **kwargs):
            self = args[0]

            # 保存前のファイル名を取得
            result = Resource.objects.filter(pk=self.pk)
            previous = result[0] if len(result) else None
            super(Resource, self).save()

            # 関数実行
            result = function(*args, **kwargs)

            # 保存前のファイルがあったら削除
            if previous:
                os.remove(settings.MEDIA_ROOT + '/' + previous.resource_image.name)
            return result
        return wrapper

    @delete_previous_file
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super(Resource, self).save()

    @delete_previous_file
    def delete(self, using=None, keep_parents=False):
        super(Resource, self).delete()
    
    def __str__(self):
        return self.resource_name

    resource_name = models.CharField(max_length=200)
    resource_image = models.ImageField(upload_to=get_image_path)
    resource_description = models.TextField(blank=True, null=True)
    resource_checkout_date = models.DateField(blank=True, null=True)
    resource_return_date = models.DateField(blank=True, null=True)

class Book(Resource):
    pass