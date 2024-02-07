from django.contrib import admin
from rango.models import Category, Page

# admin.site.register(Page)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

    # def __init__(self):
    #     super.__init__()

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
