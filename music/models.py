from django.db import models


# Create your models here.
class Playlist(models.Model):
    play_name = models.CharField('歌单', max_length=100)
    play_id = models.IntegerField("网易云id", blank=True, null=True)
    add_time = models.DateTimeField('时间', auto_now_add=True)

    # play_url = models.CharField('图片地址', max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'play_list'
        # ordering = ['-date_time']
        verbose_name = '歌单'
        verbose_name_plural = '歌单管理'


class Songlist(models.Model):
    song_name = models.CharField('歌名', max_length=100)
    song_id = models.IntegerField("网易云id", blank=True, null=True)
    song_pic = models.CharField("歌曲图片", max_length=1000,blank=True, null=True)
    song_url = models.CharField("歌曲地址", max_length=1000,blank=True, null=True)
    song_lyrics = models.TextField("歌曲歌词", blank=True, null=True)
    play =  models.ForeignKey(Playlist,related_name="songs")
    class Meta:
        db_table = 'song_list'

        verbose_name = '歌曲'
        verbose_name_plural = '歌曲管理'
