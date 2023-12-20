
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('co-api/',include('contact.urls')),
    path('pu-api/',include('purchase.urls')),
    path('se-api/',include('sell.urls')),
    path('re-api/',include('reports.urls')),
    path('pa-api/',include('payment_account.urls')),
    path('st-api/',include('stock_transfer.urls')),
    path('sad-api/',include('stock_adjustment.urls')),
    path('dr-api/',include('detailed_report.urls')),
    path('usr-api/',include('user_management.urls')),
    path('sms-api/',include('smss.urls')),
    #path('api/',include('contact.urls')),
    #path('api/product/',include('product.urls')),
    #path('api/expense/',include('expense.urls')),
    #path('api/user/', include('user_management.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

