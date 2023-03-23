from django.contrib import admin
from . models import Logo,Home,About,Entries,Work,Contact
# Register your models here.

admin.site.register(Logo)
admin.site.register(Home)
admin.site.register(About)
admin.site.register(Work)


@admin.register(Entries)
class EnteriesAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ['id','name']
    search_fields = ['name']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email']
    list_display_links = ['id','name']
    search_fields = ['name']


