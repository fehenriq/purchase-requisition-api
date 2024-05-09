from rest_framework import serializers
from apps.services.models import Service, ServiceType
from utils.validators.valid_date import retroactive_date


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

    def validate(self, data):
        if data.get("request_date") and not retroactive_date(data["request_date"]):
            raise serializers.ValidationError({"request_date": "Não é permitido data retroativa."})

        if data.get("quotation_date") and not data.get("quotation_emails"):
            raise serializers.ValidationError({"emails": "Deve ter no mínimo um fornecedor."})

        return data


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = "__all__"
