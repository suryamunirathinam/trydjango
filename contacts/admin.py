from django.contrib import admin

# Register your models here.
from .models import Contact

class ContactAdmin (admin.ModelAdmin):
                    # customization here 
    list_display = ('id','name','listing','email','contact_date')
    list_display_links = ('id','name')
    search_fields = ('name','email','listing')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)
                    # model  # name of class