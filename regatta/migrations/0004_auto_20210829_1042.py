# Generated by Django 3.2.6 on 2021-08-29 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regatta', '0003_regatta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regatta',
            name='organizer',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='regatta',
            name='place',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
