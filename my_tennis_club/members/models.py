from django.db import models

# Create your models here.
class Member(models.Model):
    '''Model definition for Member.'''
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    class Meta:
        '''Meta definition for Member.'''

        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def __str__(self):
        pass