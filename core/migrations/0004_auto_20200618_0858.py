# Generated by Django 3.0.7 on 2020-06-18 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200613_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='silaba',
            name='imagem1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='silaba',
            name='imagem2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
