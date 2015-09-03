from django.contrib import admin

# import your model
from brassica1.models import Tweets

# and register it
class TweetsAdmin(admin.ModelAdmin):
    model = Tweets
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Tweets, TweetsAdmin)
