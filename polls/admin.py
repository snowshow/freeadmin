__author__ = 'mikhailkheyfets'
from polls.models import    Modem
from django.contrib import admin
from polls.models import Choice
from polls.models import TvRecord
# admin.site.register(Poll)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3



    
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),

    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date')
    list_filter = ['pub_date', 'question']
    search_fields = ['question']
    date_hierarchy = 'pub_date'
    actions = ['make_published']

    def make_published(self, request, queryset):
        rows_updated = queryset.update(question='A')
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published   ura." % message_bit)

def export_selected_objects(modeladmin,request, queryset):
        modeladmin.message_user(request, 'jhgkajhdgkjashgdkajshdgkjashg')

        
admin.site.add_action(export_selected_objects, 'export_selected')

#list_display = ('question', 'pub_date')
#admin.site.register(Poll, PollAdmin)
#admin.site.register(Poll, PollAdmin)

#admin.site.register(TvRecord)
#admin.site.register(Choices)

#class ArticleAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None,               {'fields': ['username']}),
#        ('Date information', {'fields': ['password'], 'classes': ['collapse']}),
#
#    ]
  #  actions = [make_published]

#admin.site.register(ArticleAdmin)

from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from polls.models import Genre
from polls.models import Choices

#class MyMPTT(MPTTModelAdmin):
#    fieldsets = [
#
#        ('Date information', {'fields': ['name'], }),
#        ('Parent', {'fields': ['parent'], 'classes': ['collapse']})
#    ]
#    list_display = ('name','parent')

admin.site.register(Genre,MPTTModelAdmin)
admin.site.register(Choices)
admin.site.register(TvRecord)
admin.site.register(Modem)
#class CategoryAdmin(editor.TreeEditor):
#    list_display = ('__unicode__', 'active_toggle')
#    active_toggle = editor.ajax_editable_boolean('active', _('active'))
#admin.site.register(Genre,CategoryAdmin)