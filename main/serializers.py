from rest_framework import serializers


class MatchListSerializer(serializers.Serializer):
    index = serializers.IntegerField()
    date_cet = serializers.DateTimeField()
    date_msc = serializers.DateTimeField()
    team_a = serializers.CharField()
    team_b = serializers.CharField()
    event = serializers.CharField()
    match_type = serializers.CharField()
