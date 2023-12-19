from django.contrib import admin

from .models import Produto, Cliente


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')
    # list_editable = ('preco', 'estoque')
    # search_fields = ('nome',)
    # list_per_page = 10

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)

