# Generated by Django 3.2.6 on 2021-08-29 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regatta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('abbreviation', models.CharField(max_length=10)),
            ],
        ),
        migrations.RenameField(
            model_name='boat',
            old_name='type',
            new_name='model',
        ),
        migrations.AddField(
            model_name='boat',
            name='finrating',
            field=models.DecimalField(decimal_places=4, default=1.0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='boat',
            name='club',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='regatta.club'),
        ),
    ]