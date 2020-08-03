from .models import Product
from .models import VM
from .serializers import ProductSerializer
from .serializers import VMSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination

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


class VM_class(APIView):
    def get(self, request):
        queryset = VM.objects.all()
        id = request.GET.get('id')
        name = request.GET.get('name')
        status = request.GET.get('status')
        if id is not None:
            queryset = queryset.filter(id=id)
        if name is not None:
            queryset = queryset.filter(name=name)
        if status is not None:
            queryset= queryset.filter(status=status)
        pg = LimitOffsetPagination()
        page_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
        serializer = VMSerializer(instance=page_roles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VMSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
