from django.contrib.admin import AdminSite

class ChukyTIAdminSite(AdminSite):
    site_header = "Escuela Chucky TI - Panel Administrativo"
    site_title = "Escuela Chucky TI"
    index_title = "Bienvenido al Panel de Administración"
    
    class Media:
        css = {
            'all': ()
        }
        js = ()