# Generated by Django 2.2.2 on 2019-08-03 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_poll_num_of_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='choices',
            name='full_votes',
            field=models.IntegerField(default=0),
        ),
    ]
