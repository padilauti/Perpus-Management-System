from import_export import resources
from perpustakaan.models import Buku
from import_export.fields import Field


class BukuResource(resources.ModelResource):
    kelompok_id__nama = Field(attribute='kelompok_id', column_name='kelompok') # custom nama 

    class Meta:
        model = Buku
        fields = ['judul', 'kelompok_id__nama', 'penerbit', 'jumlah'] # buat nampilin yang mana aja 
        # export_ order = [''] buat costum posisi tema 