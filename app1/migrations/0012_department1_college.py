# Generated by Django 3.0 on 2022-06-26 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_auto_20220626_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='department1',
            name='college',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.College1'),
        ),
    ]
