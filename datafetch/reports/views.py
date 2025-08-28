from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Report, Product
from .serializers import ReportSerializer, ProductSerializer
import random



def home(request):
    return render(request, "index.html")



@api_view(['GET'])
def reports(request):

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    reports = Report.objects.all()
    if start_date and end_date:
        reports = reports.filter(date__range=[start_date, end_date])
    report_serializer = ReportSerializer(reports, many=True)

    products = Product.objects.all()
    if start_date and end_date:
        products = products.filter(date2__range=[start_date, end_date])
    product_serializer = ProductSerializer(products, many=True)


    choice = random.choice([0,1,2,3])

    response_data = {}

    if choice == 1:
        response_data["table1"] = report_serializer.data
    elif choice == 2:
        response_data["table2"] = product_serializer.data
    elif choice == 3:
        response_data["table1"] = report_serializer.data
        response_data["table2"] = product_serializer.data



    return Response(response_data)
