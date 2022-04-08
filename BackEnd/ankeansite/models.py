from django.db import models

# Create your models here.


class PlayList(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    price = models.IntegerField()
    bpm = models.IntegerField()
    time = models.IntegerField()
    cover = models.ImageField(upload_to='images/', blank=False)
    beat = models.FileField(upload_to='beats/')
    tag = models.CharField(max_length=70, blank=False, default='')
    #tags = models.CharField('Tag', blank=False, related_name='PlayList')
    link = models.CharField(max_length=70, blank=False, default='')

    def __str__(self):
        return self.title


#class Tag(models.Model):
 #   title = models.CharField(max_length=30, blank=False, default='')

  #  def __str__(self):
   #     return self.title
