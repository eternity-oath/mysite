# Generated by Django 3.2 on 2021-07-15 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yuquan', '0026_auto_20210715_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='cases',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name='浏览量'),
        ),
    ]
