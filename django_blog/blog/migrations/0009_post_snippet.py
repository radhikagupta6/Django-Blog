# Generated by Django 3.0.3 on 2020-07-16 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200716_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='click link above to read full blog post', max_length=255),
        ),
    ]
