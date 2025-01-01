from django.contrib import admin
from .models import RegistredCars,EmployesInfo,InUseCars,LogsC,FinesAccidents,FinesAccidentsImage,LicenseFile
models_list = [LogsC,RegistredCars,EmployesInfo,InUseCars,FinesAccidents,FinesAccidentsImage,LicenseFile]


class EmployesInfoAdmin(admin.ModelAdmin):
    list_display = ('ceoName','ceoNumber','section','EmpHaveCar')
    search_fields = ('ceoName','ceoNumber')
    list_filter = ('section',)


class LogsCAdmin(admin.ModelAdmin):
    list_display = ('id','Logs_employee_ins', 'taken_date','taken_time','return_date', 'return_time','Logs_car_ins')
    search_fields = ('taken_date', 'return_time')
    list_filter = ('taken_date',)
    # readonly_fields = ('Logs_car_ins','Logs_employee_ins')

class RegCarsAdmin(admin.ModelAdmin):
    list_display = ('carNumber','vType','section','cownerName','cownerEmpNumber')
    search_fields = ('vType','id',"carNumber")
    list_filter = ('vType',)

class FinesAccidentsAdmin(admin.ModelAdmin):
    # list_display = ('car','text','report_date')
    search_fields = ('text','car')
    list_filter = ()

admin.site.register(LicenseFile)
admin.site.register(LogsC, LogsCAdmin)
admin.site.register(RegistredCars, RegCarsAdmin)
admin.site.register(EmployesInfo,EmployesInfoAdmin)
admin.site.register(InUseCars)
admin.site.register(FinesAccidents)
admin.site.register(FinesAccidentsImage)