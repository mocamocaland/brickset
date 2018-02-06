from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Item(models.Model):
    set_number = models.IntegerField('セット番号')
    name = models.CharField('名前', max_length=255)
    image_url = models.URLField('画像URL', blank=True)
    rating = models.FloatField('レーティング', default=0.0)
    piece_count = models.IntegerField('ピース数', default=0)
    minifig_count = models.IntegerField('ミニフィグ数',default=0)
    us_price = models.FloatField('US価格', default=0)
    owner_count = models.IntegerField('オーナー数', default=0)
    want_it_count = models.IntegerField('欲しい数', default=0)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            "id": self.id,
            "set_number": self.set_number,
            "name": self.name,
            "iamge_url": self.image_url,
            "rating": self.rating,
            "piece_count": self.piece_count,
            "minifig_count": self.minifig_count,
            "us_price": self.us_price,
            "owner_count": self.owner_count,
            "want_it_count": self.want_it_count,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    class Meta:
        db_table = "item"


class WishList(models.Model):
    user = models.OneToOneField(User)
    items = models.ManyToManyField(Item)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return 'wish list - {}'.format(self.user.username)
