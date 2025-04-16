from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# DRF용 router 설정
from rest_framework import routers
from demos import views  # 너의 앱 이름이 demos라고 가정할게

# 라우터 객체 생성
router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'orders', views.OrderViewSet)
# 필요한 다른 모델도 추가 가능
# router.register(r'product-images', views.ProductImageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # 모든 API 경로는 /api/ 로 시작
]

# MEDIA 설정: 개발 환경에서만 작동
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)