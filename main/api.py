from rest_framework.views import APIView
from rest_framework.response import Response


from django_filters.rest_framework import DjangoFilterBackend


from .pd_parse_html import *


from .serializers import MatchListSerializer


parser = MatchParser()

parser.format_data()

parser_output = parser.get_dict()


class MatchApi(APIView):
    def get(self, request):
        result = MatchListSerializer(parser_output, many=True).data
        return Response(result)
