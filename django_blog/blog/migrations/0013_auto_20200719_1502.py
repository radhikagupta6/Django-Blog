# Generated by Django 3.0.3 on 2020-07-19 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200718_1739'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='github_url',
            new_name='instagram_url',
        ),
    ]
