# Generated by Django 3.2.6 on 2021-08-04 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_rename_votes_choice_votes2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='votes2',
            new_name='votes',
        ),
    ]
