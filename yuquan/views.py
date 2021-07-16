from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from yuquan.models import Category, Article, Message, Cases, Users
from yuquan import models

def index(request):
    return render(request, 'yuquan/index.html',  locals())


def users(request, category_name):
    if category_name == "weixin":
        title = "微信"
    else:
        title = "QQ"
    user_list = Users.objects.all().order_by('id')
    context = {"user_list": user_list, "category_name": category_name, 'title': title}
    return render(request, 'yuquan/users_contact.html', context)


def services(request):
    return render(request, 'yuquan/services.html')


def contact(request):
    return render(request, 'yuquan/contact.html')


def about(request):
    return render(request, 'yuquan/about.html')


def work(request):
    return render(request, 'yuquan/work.html')


def message(request):
    post = request.POST
    name = str(post.get("name"))
    phone = str(post.get("phone"))
    email = str(post.get("email"))
    content = str(post.get("content"))
    try:

        if not (name and phone and email and content):
            error = '姓名、电话或邮箱不能为空'
            return HttpResponse(error)
        else:
            Message.objects.create(name=name, phone=phone, email=email, content=content)
    except Exception as e:
        print('error', e)
    return render(request, 'yuquan/about.html')


def blog_detail(request):
    return render(request, 'yuquan/blog-single.html')


def paginator(request, data_list, number):
    after_range_num = 3  # 当前页前显示5页
    befor_range_num = 3  # 当前页后显示4页
    try:  # 如果请求的页码少于1或者类型错误，则跳转到第1页
        page = int(request.GET.get("page", 1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    paginator = Paginator(data_list, number)  # 设置在每页显示的数量，这里为50
    try:  # 跳转到请求页面，如果该页不存在或者超过则跳转到尾页
        page_list = paginator.page(page)
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        page_list = paginator.page(paginator.num_pages)
    if page >= after_range_num:
        page_range = paginator.page_range[page - after_range_num:page + befor_range_num]
    else:
        page_range = paginator.page_range[0:int(page) + befor_range_num]
    return page_list, page_range


def category_name(request, category_name):
    categorys = Category.objects.filter(slug=category_name)
    master_category = Category.objects.get(slug=category_name)
    son_category = Category.objects.filter(parent_category=master_category.id)
    if not categorys:
        return render(request, '404.html')
    else:
        if category_name == 'khal':
            # 处理
            data_list = Cases.objects.filter(case_category_id__parent_category=master_category.id).values('id', 'name',
                'image', 'case_category', 'case_category__slug')
            # 分页
            page_list, page_range = paginator(request, data_list, 6)
        else:
            data_list = Article.objects.filter(article_category_id__parent_category=master_category.id).values('id',
                'title', 'subtitle', 'body', 'pub_time', 'article_category__slug')
            # 分页
            page_list, page_range = paginator(request, data_list, 5)
        count = data_list.count()
        context = {"master_category": master_category, "son_category": son_category, "data_list": data_list,
                   'count': count, 'page_list': page_list, 'page_range': page_range, "title": master_category.name}
        return render(request, 'yuquan/blog.html',context)


def son_category(request, category_name, son_category):
    check_master_category = Category.objects.filter(slug=category_name)
    check_son_category = Category.objects.filter(slug=son_category)
    if not (check_master_category and check_son_category):
        return render(request, '404.html')
    master_category = Category.objects.get(slug=category_name)
    son_category_list = Category.objects.filter(parent_category=master_category.id)
    category = Category.objects.get(slug=son_category)
    if category.parent_category_id != master_category.id:
        return render(request, '404.html'),
    else:
        if category_name == 'khal':
            # 处理
            data_list = Cases.objects.filter(case_category=category.id).values('id', 'name',
                'image', 'case_category', 'case_category__slug')
            # 分页
            page_list, page_range = paginator(request, data_list, 6)
        else:
            data_list = Article.objects.filter(article_category=category.id).values('id', 'title',
                  'subtitle', 'body', 'pub_time', 'article_category__slug')
            # 分页
            page_list, page_range = paginator(request, data_list, 5)

        count = data_list.count()
        context = {"master_category": master_category, "son_category": son_category_list, "data_list": data_list,
                   'count': count, 'page_list': page_list, 'page_range': page_range, "title": category.name}
        return render(request, 'yuquan/blog.html', context,)


def get_category_tree(category_name):
    url_dict = {}
    master_categorys = Category.objects.filter(parent_category=None)
    for master_category in master_categorys:
        son_url = []
        son_categorys = Category.objects.filter(parent_category=master_category.id)
        for son_category in son_categorys:
            son_url.append(f'{master_category.slug}/{son_category.slug}')
        url_dict[master_category.slug] = son_url

    return url_dict


def article(request, category_slug, son_category_slug, id):
    master_category = Category.objects.get(slug=category_slug)
    current_category = Category.objects.get(slug=son_category_slug)
    son_category = Category.objects.filter(parent_category=master_category.id)

    if category_slug == 'khal':
        data_list = Cases.objects.filter(case_category__slug=son_category_slug).values('id', 'name', 'image', 'views',
                   'case_category', 'case_category__slug')
        # 浏览量 + 1
        case = models.Cases.objects.get(id=id)
        case.views += 1
        case.save()
    else:
        data_list = Article.objects.filter(article_category__slug=son_category_slug).values('id', 'title',
                  'subtitle', 'body', 'pub_time', 'article_category', 'article_category__slug')
    previous_article_index = 0

    next_article_index = 0
    previous_article_title = None
    nex_article_title = None
    previous_index = 0
    next_index = 0
    current_index = 0
    current_data = None
    if len(data_list) > 1:
        for index, article in enumerate(data_list):
            if index == 0:
                previous_index = 0
                next_index = index + 1
            elif index == len(data_list) - 1:
                previous_index = index - 1
                next_index = index
            else:
                previous_index = index - 1
                next_index = index + 1
            # 通过id判断当前记录;
            if article.get("id") == id:
                current_index = index
                current_data = article
                if current_index == 0:
                    next_article_index = data_list[next_index].get("id")
                    if category_slug == 'khal':
                        nex_article_title = data_list[next_index].get("name")
                    else:
                        nex_article_title = data_list[next_index].get("title")
                elif current_index == next_index:
                    previous_article_index = data_list[previous_index].get("id")
                    if category_slug == 'khal':
                        previous_article_title = data_list[previous_index].get("name")
                    else:
                        previous_article_title = data_list[previous_index].get("title")
                else:
                    previous_article_index = data_list[previous_index].get("id")
                    next_article_index = data_list[next_index].get("id")
                    if category_slug == 'khal':
                        previous_article_title = data_list[previous_index].get("name")
                        nex_article_title = data_list[next_index].get("name")
                    else:
                        previous_article_title = data_list[previous_index].get("title")
                        nex_article_title = data_list[next_index].get("title")


                break
    else:
        current_data = data_list[0]

    context = {"master_category": master_category, "son_category": son_category, "current_data": current_data,
               'previous_article_index': previous_article_index, 'next_article_index': next_article_index,
               'title': current_category.name, "previous_article_title": previous_article_title, "nex_article_title":
               nex_article_title}
    return render(request, 'yuquan/blog-single.html', context)
