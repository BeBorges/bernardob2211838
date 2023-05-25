from django.contrib import admin
from .models import Curiosity, TopScorer

class CuriosityAdmin(admin.ModelAdmin):
    # Define quais campos serão exibidos na lista de exibição do admin
    list_display = ('title', 'info_1', 'info_2', 'info_3')
    # Define os campos pelos quais é possível filtrar os registros na lista do admin
    list_filter = ('title',)
    # Define os campos pelos quais é possível realizar buscas na lista do admin
    search_fields = ('title',)

class TopScorerAdmin(admin.ModelAdmin):
    # Define quais campos serão exibidos na lista de exibição do admin
    list_display = ('title', 'info_1', 'info_2', 'info_3')
    # Define os campos pelos quais é possível filtrar os registros na lista do admin
    list_filter = ('title',)
    # Define os campos pelos quais é possível realizar buscas na lista do admin
    search_fields = ('title',)

admin.site.register(Curiosity, CuriosityAdmin)
admin.site.register(TopScorer, TopScorerAdmin)
