from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post,Project,Aboutme,Quote


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','published_date','author','image')
    list_filter = ('published_date','author')


class QuoteAdmin(admin.ModelAdmin):
    exclude = ('published_date',)
    list_display= ('qauthor','qdate')
    list_filter = ('qauthor','qdate')

class AboutmeAdmin(admin.ModelAdmin):
    list_display = ('atitle','published_date')
    exclude = ('published_date',)
    list_filter = ('published_date',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('ptitile','location','startdate','enddate','designation')
    exclude = ('published_date',)
    list_filter = ('ptitile','location','startdate')

admin.site.register(Post,PostAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Aboutme,AboutmeAdmin)
admin.site.register(Quote,QuoteAdmin)
admin.site.unregister(Group)

admin.site.site_header = "Vivek's Dashboard"
