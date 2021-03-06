# Generated by Django 2.1.4 on 2018-12-17 19:45

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_post_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='page_click',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_pic',
            field=models.ImageField(upload_to=blog.models.user_directory_path),
        ),
    ]
