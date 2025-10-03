from django.contrib import admin
from .models import Country, Department, City, User

# Customización del admin para Country
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'abrev', 'get_status')  # columnas visibles en el admin

    def get_status(self, obj):
        return "Activo ✅" if obj.status else "Inactivo ❌"
    get_status.short_description = 'Estado'  # Nombre de la columna en la tabla

# Registro de modelos en el admin
admin.site.register(Country, CountryAdmin)
admin.site.register(Department)
admin.site.register(City)
admin.site.register(User)
