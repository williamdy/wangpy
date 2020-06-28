from .models import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination


class product_class(APIView):

    def get(self, request):
        queryset = Product.objects.all()
        pg = PageNumberPagination()
        page_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
        serializer = ProductSerializer(instance=page_roles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
