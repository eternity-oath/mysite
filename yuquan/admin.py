from django.contrib import admin
from yuquan.models import Message, Category, Enterprise ,Article, Cases, Customer,ServiceFlow, Links, IndexImage, Users
# Register your models here.
from django.utils.html import format_html


class MessageAdmin(admin.ModelAdmin):
    actions_on_top = True
    # search_fields = ['name', 'phone', 'email']
    list_display = ('id', 'name', 'phone', 'email', 'content', 'created_time', 'last_mod_time')
    actions_on_bottom = True


class CategoryAdmin(admin.ModelAdmin):
    actions_on_top = True
    # search_fields = ['name', 'parent_category', 'slug']
    list_display = ('id', 'name', 'parent_category', 'slug', 'icon', 'created_time', 'last_mod_time')
    actions_on_bottom = True


class EnterpriseAdmin(admin.ModelAdmin):
    actions_on_top = True
    # search_fields = ['name', 'parent_category', 'slug']
    list_display = ('id', 'name', 'short_name', 'phone', 'email', 'address', 'beiancode', 'gongan_beiancode',
                    'created_time', 'last_mod_time')
    actions_on_bottom = True


class ArticleAdmin(admin.ModelAdmin):
    actions_on_top = True
    # search_fields = ['name', 'parent_category', 'slug']
    list_display = ('id', 'title', 'subtitle', 'body', 'pub_time', 'article_category', 'created_time', 'last_mod_time')
    actions_on_bottom = True


class CasesAdmin(admin.ModelAdmin):
    actions_on_top = True
    # search_fields = ['name', 'parent_category', 'slug']
    list_display = ('id', 'name', 'image', 'views', 'case_category', 'created_time', 'last_mod_time')
    actions_on_bottom = True


class CustomerAdmin(admin.ModelAdmin):
    actions_on_top = True
    # search_fields = ['name', 'parent_category', 'slug']
    list_display = ('id', 'title', 'photo_url', 'created_time', 'last_mod_time')
    actions_on_bottom = True

class ServiceFlowAdmin(admin.ModelAdmin):
    actions_on_top = True
    # search_fields = ['name', 'parent_category', 'slug']
    list_display = ('id', 'title', 'describe', 'created_time', 'last_mod_time')
    actions_on_bottom = True


class LinksAdmin(admin.ModelAdmin):
    actions_on_top = True
    # search_fields = ['name', 'parent_category', 'slug']
    list_display = ('id', 'name', 'link_url', 'created_time', 'last_mod_time')
    actions_on_bottom = True


class IndexImageAdmin(admin.ModelAdmin):
    actions_on_top = True
    # search_fields = ['name', 'parent_category', 'slug']
    list_display = ('id', 'name', 'image_url', 'created_time', 'last_mod_time')
    actions_on_bottom = True


class UsersAdmin(admin.ModelAdmin):
    actions_on_top = True
    # search_fields = ['name', 'parent_category', 'slug']
    list_display = ('id', 'name', 'wechat_url', 'qq_url', 'describe')
    actions_on_bottom = True

admin.site.register(Message, MessageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Enterprise, EnterpriseAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Cases, CasesAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(ServiceFlow, ServiceFlowAdmin)
admin.site.register(Links, LinksAdmin)
admin.site.register(IndexImage, IndexImageAdmin)


admin.site.register(Users, UsersAdmin)

