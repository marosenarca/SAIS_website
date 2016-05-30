from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ('StdNum', 'SUser','Sex')
# admin.site.register.Student)

@admin.register(models.Citizenship)
class CitizenshipAdmin(admin.ModelAdmin): 
	list_display = ('id','Desc')

@admin.register(models.Sex)
class SexAdmin(admin.ModelAdmin):
	list_display = ('id','Desc')

@admin.register(models.CivilStatus)
class CivilStatusAdmin(admin.ModelAdmin):
	list_display = ('id','Desc')



'''--------'''

@admin.register(models.StudentType)
class StudentType(admin.ModelAdmin):
	list_display = ('id','Desc')


@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
	list_display = ('id','Code','Desc')

@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
	list_display =  ('id','Subject','CourseNum', 'Desc','Title','Units')

@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
	list_display = ('id','Name')

@admin.register(models.CourseComponents)
class CourseComponentAdmin(admin.ModelAdmin):
	list_display = ('CourseID','ComponentID','isRequired')

@admin.register(models.CoursePreReq)
class CPRAdmin(admin.ModelAdmin):
	list_display = ('CourseID','PreReqID')

@admin.register(models.Class)
class ClassAdmin(admin.ModelAdmin):
	list_display = ('TeacherID','CourseID','Section','StartTime','EndTime','DaysOffered','Room','Status','ClassCapacity')

@admin.register(models.StudentSchedule)
class StudentScheduleAdmin(admin.ModelAdmin):
	list_display = ('ScheduleID','StudentID','Status')

@admin.register(models.CourseOffered)
class CourseOfferedAdmin(admin.ModelAdmin):
	list_display = ('CourseID','Semester','Year')

@admin.register(models.SubjectStatus)
class SubjectStatusAdmin(admin.ModelAdmin):
	list_display = ('id','Desc')

@admin.register(models.ScheduleStatus)
class ScheduleStatusAdmin(admin.ModelAdmin):
	list_display = ('id','Desc')


@admin.register(models.STS)
class STSAdmin(admin.ModelAdmin):
	list_display = ('id','BracketName','BracketDesc','PercentDiscount','Stipend')

@admin.register(models.StudentFinance)
class StudentFinanceAdmin(admin.ModelAdmin):
	list_display = ('StudentID','STSID','ScholarshipID')


@admin.register(models.ScholarshipStatus)
class ScholarshipStatusAdmin(admin.ModelAdmin):
	list_display = ('id','Desc')

@admin.register(models.Scholarship)
class ScholarshipAdmin(admin.ModelAdmin):
	list_display = ('id','Desc','isGovernment','Amount')

@admin.register(models.Syllabus)
class SyllabusAdmin(admin.ModelAdmin):
	list_display = ('id', 'Degree', 'Course', 'Year', 'Semester')

@admin.register(models.Degree)
class DegreeAdmin(admin.ModelAdmin):
	list_display = ('id', 'Name')

@admin.register(models.AddressType)
class AddressTypeAdmin(admin.ModelAdmin):
	list_display = ('id', 'Desc')

@admin.register(models.HousingType)
class HousingTypeAdmin(admin.ModelAdmin):
	list_display = ('id', 'Desc')

@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
	list_display = ('id', 'AddressType', 'HouseNumber', 'Brgy', 'City')

@admin.register(models.Parents)
class ParentsAdmin(admin.ModelAdmin):
	list_display = ('id', 'FatherName', 'FatherOccu', 'MotherName', 'MotherOccu')

@admin.register(models.Guardian)
class GuardianAdmin(admin.ModelAdmin):
	list_display = ('id', 'Name', 'Occupation', 'HouseNumber', 'Barangay', 'City')

#

@admin.register(models.SendDocs)
class SendDocsAdmin(admin.ModelAdmin):
	list_display = ('id', 'Name', 'Occupation', 'HouseNumber', 'Barangay', 'City')