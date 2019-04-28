from django.db import models

class ElecModel(models.Model):
    vid = models.CharField('voterid', max_length=10, default='', blank=False)
    name = models.CharField('name', max_length=50, default='')
    Address = models.TextField('address', default='')
    number = models.BigIntegerField('number', default='')
    gender = models.BooleanField('gender')

    @property
    def testproperty(self):
        return '{} testprop'.format(self.name)
    

