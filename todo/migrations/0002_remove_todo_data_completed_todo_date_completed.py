# Generated by Django 4.0.3 on 2022-07-17 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='data_completed',
        ),
        migrations.AddField(
            model_name='todo',
            name='date_completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]