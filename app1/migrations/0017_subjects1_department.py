# Generated by Django 3.0 on 2022-06-27 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_students1_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects1',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subjs', to='app1.Department1'),
        ),
    ]
