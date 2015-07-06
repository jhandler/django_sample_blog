from django.db import models
from django.contrib.auth.models import User
 
from datetime import datetime, timedelta
from django.utils import timezone
 
from django.conf import settings
 
# create your models
 
class Blog_Post(models.Model):
        title = models.CharField(max_length=250)
        author = models.ForeignKey(User)
        body = models.TextField()
        date_added = models.DateTimeField('date_added',auto_now_add=True, editable=False)
        date_updated = models.DateTimeField('date_updated',auto_now_add=True, auto_now=True, editable=False)
 
        def __unicode__(self):
                return u'%s' % (self.title)
        class Meta:
                verbose_name_plural = "posts"
                ordering = ['date_added']