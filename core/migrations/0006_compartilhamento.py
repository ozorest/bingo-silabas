# Generated by Django 3.0.7 on 2020-06-19 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200618_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compartilhamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.IntegerField()),
                ('ano', models.IntegerField()),
                ('facebook', models.IntegerField(default=0)),
                ('twitter', models.IntegerField(default=0)),
                ('whatsapp', models.IntegerField(default=0)),
                ('telegram', models.IntegerField(default=0)),
                ('email', models.IntegerField(default=0)),
            ],
        ),
    ]
