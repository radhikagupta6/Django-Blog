# Generated by Django 3.0.3 on 2020-07-15 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200715_2223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='snippet',
        ),
        migrations.AddField(
            model_name='post',
            name='pic',
            field=models.ImageField(default='e.png', upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(default='Click to read the blog post', max_length=255),
        ),
    ]
