# Generated by Django 3.0 on 2022-06-27 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_subjects1_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.Car')),
            ],
        ),
    ]
