from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Advocate, Company


class CompanySerializer(ModelSerializer):
    employee_count = serializers.SerializerMethodField(read_only=True)

    def get_employee_count(self, obj):
        return obj.advocate_set.count()

    class Meta:
        model = Company
        exclude = ("id",)


class AdvocateSerializer(ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Advocate
        exclude = ("id",)
