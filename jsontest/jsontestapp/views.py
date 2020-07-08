from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from jsontestapp.models import Users, ActivityPeriod

# Create your views here.

class DelData(APIView):

    def get(self, request):
        Users.objects.all().delete()
        ActivityPeriod.objects.all().delete()
        responseContent = {
            'server_name': 'Suyash Ghuge'
        }
        return Response(responseContent, status=status.HTTP_200_OK)

class FillData(APIView):

    def get(self, request):
        u = Users(idp = '12345', real_name = 'User1', tz = 'America/Los_Angeles')
        u.save()
        u1 = Users(idp = '23456', real_name = 'User2', tz = 'Asia/Kolkata')
        u1.save()
        a1 = ActivityPeriod(idp = u, activity_periods = 'start_time: Feb 1 2020 1:33PM, end_time: Feb 1 2020 1:54PM')
        a1.save()
        a2 = ActivityPeriod(idp = u, activity_periods = 'start_time: Mar 1 2020 11:11AM, end_time: Mar 1 2020 2:00PM')
        a2.save()
        a3 = ActivityPeriod(idp = u, activity_periods = 'start_time: Mar 16 2020 5:33PM, end_time: Mar 16 2020 8:02PM')
        a3.save()
        a4 = ActivityPeriod(idp = u1, activity_periods = 'start_time: Feb 1 2020 1:33PM, end_time: Feb 1 2020 1:54PM')
        a4.save()
        a5 = ActivityPeriod(idp = u1, activity_periods = 'start_time: Mar 1 2020 11:11AM, end_time: Mar 1 2020 2:00PM')
        a5.save()
        a6 = ActivityPeriod(idp = u1, activity_periods = 'start_time: Mar 16 2020 5:33PM, end_time: Mar 16 2020 8:02PM')
        a6.save()
        responseContent = {
            'server_name': 'Suyash Ghuge'
        }
        return Response(responseContent, status=status.HTTP_200_OK)
        
        


class GetJson(APIView):

    def get(self, request):
        # res = {'a'}
        responseContent = {
            'server_name': 'Suyash Ghuge'
        }
        records = Users.objects.all()
        members = []
        for record in records:
            p = []
            periods = ActivityPeriod.objects.filter(idp = record)
            for per in periods:
                p.append(per.activity_periods)
            resp = {"id" : record.idp, "real_name" : record.real_name, "tz" : record.tz, "activity_periods" : p}
            members.append(resp)
        res = {"ok" : "true", "members" : members}
        return Response(res, status=status.HTTP_200_OK)