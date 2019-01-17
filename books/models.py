from django.db import models
from django.conf import settings
import uuid
import os.path

# Create your models here.
class Resource(models.Model):
    """
    リソースのモデル
    name: リソース名(str: 200文字以内)
    image: リソースイメージ
    checkout_date: リソース貸出日
    return_date: リソース返却日
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
            def need_delete_image(previous):
                # 以前のファイルが存在するか
                if not previous == None:
                    if "path" in previous.image.__dict__.keys():
                        if os.path.exists(previous.image.path):
                            # 以前のファイルと新しいファイルが同一ではないか(要するに画像の変更なし)
                            if not previous.image.name == self.image.name:
                                return True
                return False

            self = args[0]
            # 保存前のファイル名を取得
            result = Resource.objects.filter(pk=self.pk)
            if len(result):
                previous = result[0]
                before = previous.image.name
                super(Resource, self).save()
            else:
                previous = None

            # 関数実行
            result = function(*args, **kwargs)
            
            # 保存前のファイルがあり、かつ画像ファイルが新しくアップロードされていたら削除
            if need_delete_image(previous):
                os.remove(settings.MEDIA_ROOT + '/' + previous.image.name)
            return result
        return wrapper

    @delete_previous_file
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super(Resource, self).save()

    @delete_previous_file
    def delete(self, using=None, keep_parents=False):
        super(Resource, self).delete()
    
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True, default=settings.IMAGE_URL + 'no_image.png')
    description = models.TextField(blank=True, null=True)
    checkout_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    username = models.CharField(max_length=200, default="", blank=True, null=True)

class Book(Resource):
    pass

class Monitor(Resource):
    pass