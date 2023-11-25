from rest_framework.viewsets import ModelViewSet
from .models import AuthorModel, BookModel
from .serailizer import AuthorSerializer, BookSerializer
from rest_framework.response import Response


# Create your views here.

class AuthorViewSet(ModelViewSet):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"detail": "Successfully created"}, status=201)
        else:
            return Response(serializer.errors, status=400)

    def list(self, request, *args, **kwargs):
        data = self.serializer_class(self.queryset, many=True).data
        return Response(data, 200)


class BookViewSet(ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"detail": "Successfully created"}, status=201)
        else:
            return Response(serializer.errors, status=400)

    def list(self, request, *args, **kwargs):
        data = self.serializer_class(BookModel.objects.all(), many=True).data
        return Response(data, 200)
