from django.contrib import admin
from yuquan.models import Message, Category, Enterprise ,Article, Cases, Customer,ServiceFlow, Links
# Register your models here.
from django.utils.html import format_html





admin.site.register(Message)
admin.site.register(Category)
admin.site.register(Enterprise)
admin.site.register(Article)
admin.site.register(Cases)
admin.site.register(Customer)
admin.site.register(ServiceFlow)
admin.site.register(Links)





