from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from product.models import Product, subscription
from product.serializers import ProductSerializer, SubscriptionSerializer
from datetime import datetime, timedelta

class ProductView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        products = Product.objects.filter(active=True)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, product_id):
        user = request.user
        sub = subscription.objects.filter(user=user.id, product=product_id, end_date__lte=datetime.now() + timedelta(days=365))
        if sub.exists():
            return Response({"detail": "이미 구독중 입니다."}, status=status.HTTP_400_BAD_REQUEST)
        request.data['user'] = user.id
        request.data['product'] = product_id
        request.data['start_date'] = datetime.now()
        request.data['end_date'] = datetime.now() + timedelta(days=365)
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)