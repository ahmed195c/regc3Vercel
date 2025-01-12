from django.core.management.base import BaseCommand
from logsApp.models import RegistredCars, EmployesInfo
from logsApp.cars import carsList
from logsApp.empinfo import empInfo

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        # Seed RegistredCars
        for car in carsList:
            RegistredCars.objects.create(
                carYear=car["Myear"],
                                        cownerName=car["empName"],
                                         cownerPhone=car["tel"],
                                        section=car["section"],
                                        carNumber=car["vnumber"],
                                        vType=car["vType"],
                carIsInparking=True
            )
        
        # Seed EmployesInfo
        for emp in empInfo:
            EmployesInfo.objects.create(ceoNumber=emp["empId"],
                                    ceoName=emp["empName"],
                                   phoneNumber=emp["tel"],
                                   section=emp["Sections"],
                                  position=emp["job"]
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))
