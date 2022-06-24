from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin) :
    list_display = ('title', 'tag_list', 'cdate')
    search_fields = ['title'],
    # prepopulated_fields = {'slug': ('title',)} # title 필드를 사용해 미리 채워지도록
    
    # Post 레코드 리스트를 가져오는 메소드 오버라이딩
    # N:N 관계에서 쿼리 횟수를 줄여 성능 높일때 : prefetch_related
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tag')
    
    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tag.all())

# Register your models here.
admin.site.register(Project, ProjectAdmin)