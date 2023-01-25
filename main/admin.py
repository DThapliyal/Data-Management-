from django.contrib import admin
from .models import Users
# Register your models here.
@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','Name','Email','City','Department','Password')