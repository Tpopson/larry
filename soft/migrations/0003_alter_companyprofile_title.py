# Generated by Django 4.0.6 on 2022-08-02 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soft', '0002_companyprofile_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]