# Generated by Django 3.0.7 on 2020-06-22 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200619_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metrica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.IntegerField()),
                ('ano', models.IntegerField()),
                ('sorteios', models.IntegerField(default=0)),
                ('facebook', models.IntegerField(default=0)),
                ('twitter', models.IntegerField(default=0)),
                ('whatsapp', models.IntegerField(default=0)),
                ('telegram', models.IntegerField(default=0)),
                ('email', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('mes', 'ano'),
                'unique_together': {('mes', 'ano')},
            },
        ),
        migrations.DeleteModel(
            name='Compartilhamento',
        ),
    ]
