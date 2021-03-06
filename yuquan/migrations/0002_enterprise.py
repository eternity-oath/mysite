# Generated by Django 3.2 on 2021-07-01 10:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('yuquan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='公司名称', max_length=30)),
                ('phone', models.CharField(help_text='电话', max_length=225)),
                ('email', models.EmailField(help_text='邮箱', max_length=254)),
                ('content', models.CharField(help_text='地址', max_length=225)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '公司',
                'db_table': 'enterprise',
            },
        ),
    ]
