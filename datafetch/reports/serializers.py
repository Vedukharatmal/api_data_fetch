from rest_framework import serializers
from .models import DummyReport

class DummyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DummyReport
        fields = '__all__'