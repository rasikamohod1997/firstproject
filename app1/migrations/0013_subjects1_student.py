# Generated by Django 3.0 on 2022-06-26 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_department1_college'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects1',
            name='student',
            field=models.ManyToManyField(to='app1.Students1'),
        ),
    ]