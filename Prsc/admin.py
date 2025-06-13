from django.contrib import admin
from .models import Player



#@admin.register(Player)
# usr- prsc, pass- 070809010
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'status']   
    list_filter = ['status'] 
    search_fields=['name'] 
    list_editable =['status']                          
    actions = ['approve_players']

    def approve_players(self, request, queryset):
        updated = queryset.update(status='approved')
        self.message_user(request, f"{updated} player(s) approved.")
    approve_players.short_description = "Approve selected players"

admin.site.register(Player, PlayerAdmin)