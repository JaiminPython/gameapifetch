import requests
from django.conf import settings

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView




class APIForGame(APIView):
    '''
    I have created the API view to get data from API using requests method
    '''
    def get(self, request):
        params = {"api_key": settings.APIKEY_GAME_BOMB,
                  "format": "json",
                  "query": request.GET.get("query"),
                  "resources": "game"}
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
        response = requests.get("https://www.giantbomb.com/api/search/", params=params, headers=headers)
        print(response.text)
        print("Demooo............................................")
        if response.status_code == 200:
            return Response(response.json())
        return Response({"message": "Sorry we have some issue with server."}, status=status.HTTP_404_NOT_FOUND)
