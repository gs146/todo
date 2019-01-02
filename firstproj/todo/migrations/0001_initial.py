# Generated by Django 2.1.4 on 2018-12-29 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='user_todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(verbose_name='date published')),
                ('flag', models.BooleanField(default=False)),
                ('user', models.CharField(max_length=200)),
            ],
        ),
    ]
