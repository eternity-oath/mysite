# Generated by Django 3.2 on 2021-07-15 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yuquan', '0031_enterprise_gongan_beiancode'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprise',
            name='beian_image_url',
            field=models.ImageField(blank=True, null=True, upload_to='enterprise_image/%Y%m%d/', verbose_name='备案图片'),
        ),
    ]
