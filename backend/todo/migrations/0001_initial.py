# Generated by Django 3.1.3 on 2020-11-19 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarefa', models.CharField(max_length=60)),
                ('enable', models.BooleanField(default=True)),
            ],
        ),
    ]
