# Generated by Django 3.0.3 on 2020-07-15 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200715_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='pic',
        ),
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Clink link above to read the blog post', max_length=255),
        ),
    ]
