# Generated by Django 4.0.4 on 2022-05-09 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(default=0, max_length=254)),
                ('cpf', models.CharField(max_length=11)),
                ('data_criacao', models.DateField()),
            ],
        ),
    ]
