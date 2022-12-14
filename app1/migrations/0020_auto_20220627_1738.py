# Generated by Django 3.0 on 2022-06-27 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_auto_20220627_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'fueltype',
            },
        ),
        migrations.AddField(
            model_name='carmodel',
            name='fueltype',
            field=models.ManyToManyField(to='app1.FuelType'),
        ),
    ]
