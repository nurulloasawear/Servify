from django.urls import path, include

urlpatterns = [
    path('users/', include('api.user.urls')),
    # path('address/', include('api.address.urls')),
    # path('admin-logs/', include('api.admin_logs.urls')),
    # path('booking/', include('api.booking_m.urls')),
    # path('cart/', include('api.cart.urls')),
    # path('category/', include('api.category.urls')),
    # path('chat/', include('api.chat_messages.urls')),
    # path('liked/', include('api.liked.urls')),
    # path('location/', include('api.location.urls')),
    # path('notifications/', include('api.notifications.urls')),
    # path('payment/', include('api.payment.urls')),
    # path('proffessions/', include('api.proffessions.urls')),
    # path('reports/', include('api.reports.urls')),
    # path('review/', include('api.review.urls')),
    # path('schedules/', include('api.schedules.urls')),
    # path('services/', include('api.services.urls')),
]