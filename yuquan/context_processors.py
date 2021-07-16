#!/usr/bin/env python
# encoding: utf-8
from yuquan.models import Category, Enterprise, Cases, Customer, ServiceFlow, Links, Article, IndexImage, Users


def category(requests):
    categorys = Category.objects.all().order_by('id')
    enterprise = Enterprise.objects.all().order_by('id')[0]
    cases_list = Cases.objects.all().order_by('id').values(
        'id', 'name', 'image', 'views', 'case_category', 'case_category__slug','case_category_id__parent_category__slug'
    )
    customer_list = Customer.objects.all().order_by('id')[0:4]
    service_flow_list = ServiceFlow.objects.all().order_by('id')
    link_list = Links.objects.all().order_by('id')
    index_image_list = IndexImage.objects.all().order_by('id')
    xwzx_son_list = Category.objects.filter(parent_category__slug="xwzx").order_by('id')
    index_user_image = Users.objects.all().order_by('id')[0]
    print(index_user_image.qq_url)
    xwzx_son_article = {}
    for xwzx_son in xwzx_son_list:

        xwzx_son_article[xwzx_son.slug] = Article.objects.filter(article_category=xwzx_son.id).order_by('-pub_time')[0:4]


    return {
        "categorys": categorys,
        "enterprise": enterprise,
        "cases_list": cases_list,
        "customer_list": customer_list,
        "service_flow_list": service_flow_list,
        "link_list": link_list,
        "index_image_list": index_image_list,
        "xwzx_son_list": xwzx_son_list,
        "index_user_image": index_user_image,
        "xwzx_son_article": xwzx_son_article
    }

