from django.db import models

# Create your models here.

class Logo(models.Model):

    img = models.ImageField('page image',upload_to='images')

    def __str__(self):
        return self.img
    
    class Meta:
        verbose_name = 'Logos'
        verbose_name_plural = 'Logo'
    
class Home(models.Model):

    name = models.CharField('Home name',max_length=30)
    text = models.TextField('Home text')
    img = models.ImageField('Home image',upload_to='images')
    button = models.CharField('Button name',max_length=30)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Homes'
        verbose_name_plural = 'Home'
    

class About(models.Model):

    name = models.CharField('About page name',max_length=50)
    text = models.TextField('About page text')
    img = models.ImageField('About page image',upload_to='images')
    button = models.CharField('Button name',max_length=30)

    def __str__(self):
        return self.name
    
class Entries(models.Model):

    name = models.CharField('Entries name',max_length=50)
    text = models.TextField('Entries text')
    img = models.ImageField('Entries image',upload_to='images')
    button = models.CharField('Button name',max_length=30)

    def __str__(self):
        return self.name
    

class Work(models.Model):

    name = models.CharField('Image name',max_length=50)
    text = models.TextField('Image text')
    img = models.ImageField('Work image',upload_to='images')
    
    def __str__(self):
        return self.name
    
class Contact(models.Model):

    name = models.CharField('Contact name',max_length=50)
    email = models.EmailField('User email')
    subject = models.CharField('Contact subject',max_length=200)
    message = models.TextField('User message')

    def __str__(self):
        return self.name