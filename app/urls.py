from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet
router = DefaultRouter()
router.register('author', AuthorViewSet)
router.register('book', BookViewSet)


urlpatterns = []
urlpatterns += router.urls