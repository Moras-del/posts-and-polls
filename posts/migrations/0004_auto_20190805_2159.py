# Generated by Django 2.2.2 on 2019-08-05 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_pluses'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': (('can_plus_post', 'can_plus_post'),)},
        ),
    ]
