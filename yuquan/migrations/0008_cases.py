# Generated by Django 3.2 on 2021-07-06 08:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('yuquan', '0007_article_article_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间')),
                ('name', models.CharField(help_text='名称', max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/%Y%m%d/', verbose_name='案例')),
            ],
            options={
                'verbose_name': '案例',
                'db_table': 'cases',
            },
        ),
    ]
