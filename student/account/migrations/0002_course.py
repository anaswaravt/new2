# Generated by Django 4.1.3 on 2022-12-01 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('semester', models.CharField(max_length=100)),
                ('fee', models.IntegerField(max_length=100)),
            ],
        ),
    ]