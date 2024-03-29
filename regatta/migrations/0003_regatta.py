# Generated by Django 3.2.6 on 2021-08-29 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regatta', '0002_auto_20210829_0957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regatta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('place', models.CharField(max_length=30)),
                ('organizer', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('club', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='regatta.club')),
            ],
        ),
    ]
