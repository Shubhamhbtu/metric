from rest_framework import viewsets
from .serializers import MyDataSerializer
from .models import MyData
from datetime import datetime, timedelta
from django.utils.timezone import now


class MyDataViewSet(viewsets.ModelViewSet):
    today = datetime.today()
    queryset = MyData.objects.filter(
        create_date__year=today.year,
        create_date__month=today.month,
        create_date__day=today.day
    )
    five_minutes_ago = now() + timedelta(
        minutes=-5)
    queryset = queryset.filter(create_date__gte=five_minutes_ago)
    serializer_class = MyDataSerializer

    # def get_queryset(self):
    #     minute = self.request.query_params.get("minute")
    #     today = datetime.today()
    #     five_minutes_ago = now() + timedelta(
    #         minutes=-minute)
    #     queryset = MyData.objects.filter(create_date__gte=five_minutes_ago)
    #     serializer_class = MyDataSerializer
