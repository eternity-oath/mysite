#!/usr/bin/env python
# encoding: utf-8
from yuquan.models import Category, Enterprise, Cases, Customer, ServiceFlow, Links, Article



def category(requests):
    categorys = Category.objects.all().order_by('id')
    enterprise = Enterprise.objects.all().order_by('id')[0]
    cases_list = Cases.objects.all().order_by('id')
    customer_list = Customer.objects.all().order_by('id')[0:4]
    service_flow_list = ServiceFlow.objects.all().order_by('id')
    link_list = Links.objects.all().order_by('id')
    xwzx_son_list = Category.objects.filter(parent_category__slug="xwzx").order_by('id')
    xwzx_son_article = {}
    for xwzx_son in xwzx_son_list:
        print(xwzx_son.slug)
        xwzx_son_article[xwzx_son.slug] = Article.objects.filter(article_category=xwzx_son.id).order_by('-pub_time')[0:4]


    return {
        "categorys": categorys,
        "enterprise": enterprise,
        "cases_list": cases_list,
        "customer_list": customer_list,
        "service_flow_list": service_flow_list,
        "link_list": link_list,
        "xwzx_son_list": xwzx_son_list,
        "xwzx_son_article": xwzx_son_article
    }

