# Generated by Django 3.0.7 on 2020-06-23 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200622_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('tipo', models.CharField(choices=[('E', 'Elogio'), ('D', 'Dúvida'), ('R', 'Reclamação'), ('S', 'Sugestão'), ('X', 'Outros')], max_length=1)),
                ('mensagem', models.TextField()),
                ('publicado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-publicado',),
            },
        ),
    ]
