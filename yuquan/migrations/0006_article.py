# Generated by Django 3.2 on 2021-07-06 08:00

from django.db import migrations, models
import django.utils.timezone
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('yuquan', '0005_alter_category_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='标题')),
                ('body', mdeditor.fields.MDTextField(verbose_name='正文')),
                ('pub_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '文章',
                'db_table': 'article',
            },
        ),
    ]
