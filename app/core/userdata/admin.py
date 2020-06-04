from django.contrib import admin
from .models import DatosUser, Roles, HabilUser, Rates, DetaRoles

# Register your models here.
class DatosUserAdmin(admin.ModelAdmin):
    list_display = "nombuser"
    list_display_links = ["nombuser",]
    search_fields = ["nombuser",]

    class Meta:
        model = DatosUser

admin.site.register(DatosUser)

class RolesAdmin(admin.ModelAdmin):
    list_display = "roleName"
    list_display_links = ["roleName",]
    search_fields = ["roleName",]

    class Meta:
        model = Roles

admin.site.register(Roles)

class HabilUserAdmin(admin.ModelAdmin):
    list_display = "nombhabil"
    list_display_links = ["nombhabil",]
    search_fields = ["nombhabil",]

    class Meta:
        model = HabilUser

admin.site.register(HabilUser)

class RatesAdmin(admin.ModelAdmin):
    list_display = "rate"
    list_display_links = ["rate",]
    search_fields = ["rate",]

    class Meta:
        model = Rates

admin.site.register(Rates)

class DetaRolesAdmin(admin.ModelAdmin):
    list_display = "estarol"
    list_display_links = ["estarol",]
    search_fields = ["estarol",]

    class Meta:
        model = DetaRoles

admin.site.register(DetaRoles)