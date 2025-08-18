from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import DummyReport
from .serializers import DummyReportSerializer



def home(request):
    return render(request, "index.html")



@api_view(['GET'])
def get_reports(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    queryset = DummyReport.objects.all()
    if start_date and end_date:
        queryset = queryset.filter(date__range=[start_date, end_date])
    
    serializer = DummyReportSerializer(queryset, many=True)
    return Response(serializer.data)
