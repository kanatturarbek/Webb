
from rest_framework import serializers

from models import Vacancy

class VacancySerializer(serializers.Serializers):
    id=serializers.IntegerField()
    name=serializers.CharField()
