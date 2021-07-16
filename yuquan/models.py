import os
from abc import ABCMeta, abstractmethod, abstractproperty
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.timezone import now
from mdeditor.fields import MDTextField
from pypinyin import Style, lazy_pinyin


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_time = models.DateTimeField('创建时间', default=now)
    last_mod_time = models.DateTimeField('修改时间', default=now)

    def save(self, *args, **kwargs):
        if 'slug' in self.__dict__:
            slug = getattr(
                self, 'title') if 'title' in self.__dict__ else getattr(
                self, 'name')
            initial = ''.join(lazy_pinyin(slug, style=Style.FIRST_LETTER))
            setattr(self, 'slug', initial)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True

    @abstractmethod
    def get_absolute_url(self):
        pass


class Category(BaseModel):
    """分类"""
    name = models.CharField('分类名', max_length=30, unique=True)
    parent_category = models.ForeignKey(
        'self',
        verbose_name="父级分类",
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    slug = models.SlugField(default='no-slug', max_length=60, blank=True)
    icon = models.CharField(verbose_name='菜单图标', max_length=32)
    class Meta:
        ordering = ['name']
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse(
            'blog:category_detail', kwargs={
                'category_name': self.slug})

    def __str__(self):
        return self.name


class Enterprise(BaseModel):
    #9、公司
    name = models.CharField(max_length=30, help_text="公司名称")
    short_name = models.CharField(max_length=30, help_text="简称")
    english_name = models.CharField(max_length=30, help_text="英文名称")
    phone = models.CharField(max_length=225, help_text="电话")
    email = models.EmailField(help_text="邮箱")
    address = models.CharField(max_length=225, help_text="地址")
    describe = models.CharField(max_length=225, help_text="企业描述")
    vision = MDTextField('企业愿景')
    image_url = models.ImageField('企业图片', upload_to='enterprise_image/%Y%m%d/', blank=True, null=True)
    video_url= models.FileField('企业视频', upload_to='enterprise_video/%Y%m%d/', blank=True, null=True)
    video_describe = models.CharField('视频描述', max_length=225, help_text="视频描述")
    video_image_url = models.ImageField('企业视频图片', upload_to='enterprise_image/%Y%m%d/', blank=True, null=True)
    recruit_image_url = models.ImageField('招聘图片', upload_to='enterprise_image/%Y%m%d/', blank=True, null=True)
    recruit = MDTextField('招聘')
    beian_image_url = models.ImageField('备案图片', upload_to='enterprise_image/%Y%m%d/', blank=True, null=True)
    beiancode = models.CharField(
        '备案号',
        max_length=2000,
        null=True,
        blank=True)
    gongan_beiancode = models.TextField(
        '公安备案号',
        max_length=2000,
        null=True,
        blank=True)
    class Meta:
        db_table='enterprise'
        verbose_name = "公司"

    def __str__(self):
        return self.name


class Message(BaseModel):
    #9、留言
    name = models.CharField(max_length=30, help_text="姓名")
    phone = models.CharField(max_length=225, help_text="电话")
    email = models.EmailField(help_text="邮箱")
    content = models.CharField(max_length=225, help_text="留言")
    class Meta:
        db_table='message'
        verbose_name = "留言"


class Article(BaseModel):
    """文章"""
    title = models.CharField('标题', max_length=200, unique=True)
    subtitle = models.CharField('副标题', max_length=200)
    body = MDTextField('正文')
    pub_time = models.DateTimeField(
        '发布时间', blank=False, null=False, default=now)
    article_category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    class Meta:
        db_table = 'article'
        verbose_name = "文章"

    def __str__(self):
        return self.title


class Cases(BaseModel):
    name = models.CharField(max_length=30, help_text="名称")
    image = models.ImageField('案例', upload_to='cases_image/%Y%m%d/', blank=True, null=True)
    views = models.PositiveIntegerField('浏览量', default=0)
    case_category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    # 这里定义一个方法，作用是当用户注册时没有上传照片，模板中调用 [ModelName].[ImageFieldName].url 时赋予一个默认路径

    def photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/media/default/user.jpg'

    class Meta:
        db_table = 'cases'
        verbose_name = "案例"

    def __str__(self):
        return self.name


class Customer(BaseModel):
    title = models.CharField(max_length=40, help_text="名称")
    comment = models.CharField(max_length=200, help_text="评价")
    photo_url = models.ImageField('客户url', upload_to='photo_image/%Y%m%d/', blank=True, null=True)

    class Meta:
        db_table = 'customer'
        verbose_name = "客户点评"

    def __str__(self):
        return self.title


class ServiceFlow(BaseModel):
    title = models.CharField(max_length=40, help_text="名称")
    describe = models.CharField(max_length=200, help_text="描述")
    class Meta:
        db_table = 'service_flow'
        verbose_name = "服务流程"

    def __str__(self):
        return self.title


class Links(BaseModel):
    name = models.CharField(max_length=40, help_text="名称")
    link_url = models.URLField(help_text="网址")

    class Meta:
        db_table = 'links'
        verbose_name = "友情链接"

    def __str__(self):
        return self.name


class IndexImage(BaseModel):
    """主页图片"""
    name = models.CharField(max_length=40, help_text="名称")
    image_url = models.ImageField('主页图片', upload_to='index_image/%Y%m%d/', blank=True, null=True)
    class Meta:
        db_table = 'index_image'
        verbose_name = "主页滚动图片"

    def __str__(self):
        return self.name


class Users(BaseModel):
    """主页图片"""
    name = models.CharField(max_length=40, help_text="名称")
    wechat_url = models.ImageField('微信图片', upload_to='user_image/%Y%m%d/', blank=True, null=True)
    qq_url = models.ImageField('qq图片', upload_to='user_image/%Y%m%d/', blank=True, null=True)
    describe = models.CharField(max_length=225, help_text="描述")
    class Meta:
        db_table = 'users'
        verbose_name = "员工"

    def __str__(self):
        return self.name