from django.db import models
import datetime
from datetime import datetime, timedelta
from django.template.defaultfilters import slugify
# Create your models here.

class Reports(models.Model):
    snowfall = models.IntegerField()
    bottom_mintemp = models.IntegerField()
    bottom_maxtemp = models.IntegerField()
    mid_mintemp = models.IntegerField()
    mid_maxtemp = models.IntegerField()
    top_mintemp = models.IntegerField()
    top_maxtemp = models.IntegerField()
    todays_date = models.DateTimeField(auto_now_add=True, )
    resort_id = models.ForeignKey(
        'Resorts', on_delete = models.CASCADE, to_field='id', unique = True)



    

class Resorts(models.Model):
    resort_name = models.CharField(max_length=200, unique = True)
    location = models.CharField(max_length=30)
    slug = models.SlugField(max_length=200, unique = True, null = True)

    def save(self, *args, **kwargs):    
            super(Resorts, self).save(*args, **kwargs)
            if not self.slug:
                self.slug = slugify(self.resort_name.title) + '-' + str(self.id)
                self.save

    def __str__(self):
        return self.resort_name



    