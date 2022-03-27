from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from .serializers import CasesSerializer
from .models import *
from rest_framework.response import Response
from rest_framework import status


class CovidAPIView(APIView):
    def get(self, request, slug):

        try:
            query = Cases.objects.get(country=slug)
            serializer = CasesSerializer(query)
            data = serializer.data
            data["status"] = "successful"
            data["message"] = "case_created_successfully"
            return Response(data, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            url = 'https://covid-api.mmediagroup.fr/v1/cases?country=' + slug
            data = requests.get(url)
            data = data.json()

            for i in data:
                res = data[i]

                if res.get('country') is None:
                    data = {
                        "status": "failed",
                        "message": "invalid_country"
                    }
                    return Response(data)
                else:
                    serializer = CasesSerializer(data=res)
                    if serializer.is_valid():
                        serializer.save()
                        data = serializer.data
                        data["status"] = "successful"
                        data["message"] = "case_created_successfully"
                        return Response(data, status=status.HTTP_200_OK)

                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



















































        '''

        for i in data.keys():
            for j in data[i].keys():
                confirmed = j.confirmed
                return Response(confirmed)
                
        '''

