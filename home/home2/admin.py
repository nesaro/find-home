from django.contrib import admin
from django.utils.html import format_html
from django.db.models import OuterRef, Subquery, F
from .models import House, HousePrice, HouseOffer
from .forms import HouseForm

class HPInline(admin.StackedInline):
    model = HousePrice
    can_delete=False
    extra=0

class HOInline(admin.StackedInline):
    model = HouseOffer
    can_delete=False
    extra=0

class HouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'clickurl', 'asking_price', 'description', 'log', 'n_bedrooms', 'reception', 'distance_to_station_km',
                    'carpet', 'lease', 'valuation', 'first_call_on', 'first_visit_on', 'postcode', 'land_registry_price_sold', 'deactivated', 'last_offer')
    inlines = [HPInline, HOInline]
    list_filter = ['deactivated', 'first_call_on']
    
    
    def asking_price(self, obj):
        return obj.current_price
    asking_price.admin_order_field = 'current_price'

    def valuation(self, obj):
        return obj.average_valuation
    valuation.admin_order_field = 'average_valuation'

    def last_offer(self, obj):
        return obj.last_offer
    last_offer.admin_order_field = 'last_offer'

    def clickurl(self, obj):
        return format_html('<a href="{0}">{0}</a>', obj.url)

    def get_queryset(self, request):
        result = super().get_queryset(request)
        prices = HousePrice.objects.filter(house=OuterRef('id')).order_by('-date')
        result = result.annotate(current_price=Subquery(prices.values('price')[:1]))
        offers = HouseOffer.objects.filter(house=OuterRef('id')).order_by('-date')
        result = result.annotate(last_offer=Subquery(offers.values('amount')[:1]))
        result = result.annotate(average_valuation=(F('ne_valuation')+F('ng_valuation'))/2)
        return result

class HousePriceAdmin(admin.ModelAdmin):
    list_display = ('house', 'date', 'price')


admin.site.register(House, HouseAdmin)
admin.site.register(HousePrice, HousePriceAdmin)
admin.site.register(HouseOffer)
