from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from .serializers import CasesSerializer
from .models import *
from rest_framework.response import Response
from rest_framework import status


class DictionaryAPIView(APIView):
    def get(self, request, slug):
        # url = 'https://api.dictionaryapi.dev/api/v2/entries/en/hello'
        # url = 'https://coronavirus.m.pipedream.net/'
        # url = 'https://dog.ceo/api/breeds/list/all'
        # url = 'https://ulvis.net/api.php?url=www.asuquo.com/'

        try:
            query = Cases.objects.get(country=slug)
            serializer = CasesSerializer(query)
            return Response(data=serializer.data)

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
                        return Response(data, status=status.HTTP_201_CREATED)

                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



















































        '''

        for i in data.keys():
            for j in data[i].keys():
                confirmed = j.confirmed
                return Response(confirmed)
                
        '''
