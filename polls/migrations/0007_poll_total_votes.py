# Generated by Django 2.2.2 on 2019-08-05 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20190803_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='total_votes',
            field=models.PositiveIntegerField(null=True),
        ),
    ]