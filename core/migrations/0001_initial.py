# Generated by Django 3.0.7 on 2020-06-13 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Silabas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('silaba', models.CharField(max_length=3)),
                ('palavra1', models.CharField(max_length=10)),
                ('palavra2', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ('silaba',),
            },
        ),
    ]
