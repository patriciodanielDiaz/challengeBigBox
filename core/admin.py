from django.contrib import admin
from  .models import Category, Reason, Box, Activity,BoxImage,ActivityImage
from django.contrib import admin


class ReasonInLine(admin.TabularInline):
    model = Reason
    extra = 1

class BoxImageInLine(admin.TabularInline):
    model = BoxImage
    extra = 1

class BoxAdmin(admin.ModelAdmin):
    inlines =[ BoxImageInLine]
    list_display = ('name','category')
    list_editable =('category',)


class ActivityAdmin(admin.ModelAdmin):
    
    list_display = ('name','category')
    list_editable =('category',)

admin.site.register(Category)
admin.site.register(Reason)
admin.site.register(Box,BoxAdmin)
admin.site.register(Activity,ActivityAdmin)
admin.site.register(BoxImage)
admin.site.register(ActivityImage)










'''
class ReasonAdmin(admin.ModelAdmin):
     inlines = [ActivityInline, ]
     exclude = ('reasons',)


    def get_queryset(self, request):
        qs = super(BoxAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs

        box_ct = ContentType.objects.get_for_model(Box)
        log_entries = LogEntry.objects.filter(
            content_type=box_ct, 
            user=request.user,
            action_flag=ADDITION
        )
        user_box_ids = [a.object_id for a in log_entries]
        return qs.filter(id__in=user_box_ids)
'''