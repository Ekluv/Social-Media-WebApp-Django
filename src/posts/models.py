from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.TextField(max_length=1000, blank=False,null=False)
    submitted_by = models.ForeignKey(User)
    submitted_on = models.DateTimeField(auto_now_add=True,auto_now=False)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={"pk":self.pk})
