# Generated by Django 3.1.3 on 2020-12-10 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.CharField(max_length=200)),
                ('creation_Time', models.DateTimeField(auto_now_add=True)),
                ('completion_Status', models.BooleanField(default=False)),
            ],
        ),
    ]
