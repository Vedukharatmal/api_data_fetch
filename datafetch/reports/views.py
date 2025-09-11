from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Report, Product
from .serializers import ReportSerializer, ProductSerializer
import random
from django.http import JsonResponse
import requests
from reports.utils.config_loader import get_url_from_excel


#home function
def home(request):
    return render(request, "index.html")

#function to take api-endpoint from config.xlsx
def get_api_endpoint(request):
    try:
        # Read the endpoint for "reports_api" from config.xlsx
        url = get_url_from_excel("reports_api")  
        return JsonResponse({"endpoint": url})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

#local database api function
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

    choice = random.choice([0, 1, 2, 3])

    tables = []

    if choice == 1:
        tables.append({
            "name": "table1",
            "columns": list(report_serializer.data[0].keys()) if report_serializer.data else [],
            "rows": [list(item.values()) for item in report_serializer.data]
        })
    elif choice == 2:
        tables.append({
            "name": "table2",
            "columns": list(product_serializer.data[0].keys()) if product_serializer.data else [],
            "rows": [list(item.values()) for item in product_serializer.data]
        })
    elif choice == 3:
        if report_serializer.data:
            tables.append({
                "name": "table1",
                "columns": list(report_serializer.data[0].keys()),
                "rows": [list(item.values()) for item in report_serializer.data]
            })
        if product_serializer.data:
            tables.append({
                "name": "table2",
                "columns": list(product_serializer.data[0].keys()),
                "rows": [list(item.values()) for item in product_serializer.data]
            })


    if not tables:
        return Response({"tables": [], "message": "No data found"}, status=200)

    return Response({"tables": tables}, status=200)



#External api function
@api_view(["GET"])
def reports_api(request):
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")

    try:
        external_api_url = get_url_from_excel("reports_api")
    except Exception as e:
        return Response({"error": f"Config error: {str(e)}"}, status=500)

    try:
        response = requests.get(
            external_api_url,
            params={"start_date": start_date, "end_date": end_date},
            timeout=10
        )

        if response.status_code != 200:
            return Response({"error": "Failed to fetch data from provider"}, status=502)

        external_data = response.json()

        normalized_tables = [
            {
                "name": table.get("name", "Unknown Table"),
                "columns": table.get("columns", []),
                "rows": table.get("rows", []),
            }
            for table in external_data.get("tables", [])
        ]

        if not normalized_tables:
            return Response({"tables": [], "message": "No data found"}, status=200)
        

        return Response({"tables": normalized_tables}, status=200)

    except Exception as e:
        return Response({"error": str(e)}, status=500)
