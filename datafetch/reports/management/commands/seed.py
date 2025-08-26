from django.core.management.base import BaseCommand
from reports.models import Report,Product
from datetime import date, timedelta
import random

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Report.objects.all().delete()
        Product.objects.all().delete()
        base_date = date(2025, 1, 1)
        
        
        
        for i in range(30):
            Report.objects.create(
                name=f"Item {i+1}",
                date=base_date + timedelta(days=i),
                value=random.randint(10, 100),
                price=random.randint(10,100),
            )


        for i in range(30):
            Product.objects.create(
                product=f"Product {i+1}",
                date2=base_date + timedelta(days=i),
                value2=random.randint(10,100),
                rate=random.randint(10,100),
            )
        self.stdout.write(self.style.SUCCESS("Dummy data created!"))