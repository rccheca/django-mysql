# Generated by Django 3.2.6 on 2021-08-04 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='votes',
            new_name='votes2',
        ),
    ]
