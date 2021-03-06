# Generated by Django 2.2 on 2020-05-05 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0013_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='short_note_about_yourself',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='current_year',
            field=models.CharField(choices=[('1st year', '1st year'), ('2nrd year', '2nd year'), ('3rd year', '3rd year'), ('4th year', '4th year')], max_length=500, null=True),
        ),
    ]
