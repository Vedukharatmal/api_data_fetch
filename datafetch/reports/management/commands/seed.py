from django.core.management.base import BaseCommand
from reports.models import DummyReport
from datetime import date, timedelta
import random

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        DummyReport.objects.all().delete()
        base_date = date(2025, 1, 1)
        for i in range(30):
            DummyReport.objects.create(
                name=f"Item {i+1}",
                date=base_date + timedelta(days=i),
                value=random.randint(10, 100)
            )
        self.stdout.write(self.style.SUCCESS("Dummy data created!"))