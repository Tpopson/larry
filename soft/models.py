from django.db import models

# Create your models here.


class CompanyProfile(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=250)
    keyword = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='logo', blank=True, null=True)
    favicon = models.ImageField(upload_to='logo', blank=True, null=True, default='/favicon-96x96.png')
    banner = models.ImageField(upload_to='banner', blank=True, null=True)
    mobile = models.CharField(max_length=20)
    mobile2 = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField()
    copyright_year = models.CharField(max_length=4)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'companyprofile'
        managed = True
        verbose_name = 'CompanyProfile'
        verbose_name_plural = 'CompanyProfile'




STATUS = [
    ('New', 'New'),
    ('Processing', 'Processing'),
    ('Cleared', 'Cleared'),
]

class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    message = models.TextField()
    email = models.EmailField()
    created = models.DateField(auto_now_add=True)
    cleared = models.DateField(auto_now=True)
    admin_note = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS, default='New')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'contact'
        managed = True 
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'
    

class Service(models.Model):
    type = models.CharField(max_length=250)
    img = models.ImageField(upload_to='services', blank=True, null=True)

    def __str__(self):
        return self.type

    class Meta:
        db_table = 'service'
        managed = True 
        verbose_name = 'Service'
        verbose_name_plural = 'Service'