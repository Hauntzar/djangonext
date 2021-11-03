from django.shortcuts import render
from rest_framework import generics,response,status
from .models import Campaign, Subscriber
from .serializers import SubscriberSerializer,CampaignSerializer


# Create your views here.
class CampaignListAPIView(generics.ListAPIView):
    serializer_class = CampaignSerializer

    def get_queryset(self):
        return Campaign.objects.all()

class CampaignDetailAPIView(generics.GenericAPIView):
    serializer_class = CampaignSerializer

    def get(self,request,slug):# generic can handle put,patch,post,get,etc
        query_set = Campaign.objects.filter(slug=slug).first()
        # print('query_set: ',query_set)
        # print('Campaign.objects.filter(slug=slug): ',Campaign.objects.filter(slug=slug))
        # print('query_set: ',query_set)

        if query_set:
            print('found')
            return response.Response(self.serializer_class(query_set).data)

        print('nothing')
        return response.Response('Not found', status=status.HTTP_404_NOT_FOUND)

class SubscribeToCampaignAPIView(generics.CreateAPIView):
    serializer_class = SubscriberSerializer

    def get_queryset(self):
        return Subscriber.objects.all()