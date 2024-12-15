from django.contrib import admin
from .models import TestScore
from .models import CustomUser


@admin.register(TestScore)
class TestScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'school_name', 'is_studying', 'study_level', 'current_activity')
    search_fields = ('school_name', 'user__username')  # Foydalanuvchi username va maktab nomi bo'yicha qidirish
    list_filter = ('study_level', 'is_studying')  # Filtrlar
    ordering = ('-user',)  # Tartib
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('date_of_birth', 'phone_number', 'address', 'bio', 'profile_picture', 'updated_at')
    search_fields = ('phone_number', 'address')  # Qidiruv uchun
    list_filter = ('updated_at',)
admin.site.register(CustomUser, MyModelAdmin)
