from django.contrib import admin
from taxonomy.models import Taxonomy, TaxonomyTerm, TaxonomyMap

class TaxonomyAdmin(admin.ModelAdmin):
   pass

class TaxonomyTermAdmin(admin.ModelAdmin):
   pass

class TaxonomyMapAdmin(admin.ModelAdmin):
   pass


admin.site.register(Taxonomy, TaxonomyAdmin)
admin.site.register(TaxonomyTerm, TaxonomyTermAdmin)
admin.site.register(TaxonomyMap, TaxonomyMapAdmin)
