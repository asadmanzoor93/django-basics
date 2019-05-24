from django.contrib import admin

from users.models import CustomUser, BlogPost, DateConversion
from users.forms import BlogForm


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'last_login')
    search_fields = ('username', 'first_name', 'last_name')
    list_filter = ('last_login',)
    fields = ('first_name', 'last_name', 'username', 'email', 'location','birth_date', 'is_admin',
              'is_staff', 'bio')
    date_hierarchy = 'last_login'
    ordering = ('-last_login',)


class BlogPostAdmin(admin.ModelAdmin):
    actions = ['delete_selected', 'publish_selected']
    list_display = ('title', 'content', 'status')

    def publish_selected(self, request, queryset):
        queryset.update(status='published')

    publish_selected.short_description = "Publish the selected posts"

    def get_actions(self, request):
        actions = super(BlogPostAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    form = BlogForm
    change_form_template = 'custom_create.html'
    fields = ('title', 'content', 'status')


class DateConversionAdmin(admin.ModelAdmin):
    list_display = ('timezone', 'status', 'date')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(DateConversion, DateConversionAdmin)
