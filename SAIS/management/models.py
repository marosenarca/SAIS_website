from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

stdNumValidator = RegexValidator('^\d{9}$','Invalid input!')

# Create your models here.

class Citizenship(models.Model):
	Desc = models.CharField(max_length=100)

	def __str__(self):
		return self.Desc

class CivilStatus(models.Model):
	Desc = models.CharField(max_length=10)

	def __str__(self):
		return self.Desc

class Sex(models.Model):
	Desc = models.CharField(max_length=10)

	def __str__(self):
		return self.Desc

class StudentType(models.Model):
	Desc = models.CharField(max_length=40)

	def __str__(self):
		return self.Desc

class Degree(models.Model):
	Name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.Name


class Student(models.Model):	
	SUser = models.OneToOneField(User)
	StdNum = models.CharField(max_length=9, blank=False, validators=[stdNumValidator])
	MiddleName = models.CharField(max_length=50)
	BirthDate = models.DateField()
	StudentType = models.ForeignKey(StudentType)
	Sex = models.ForeignKey(Sex)
	CivilStatus = models.ForeignKey(CivilStatus)
	Citizenship = models.ForeignKey(Citizenship)
	Degree = models.ForeignKey(Degree)

	def __unicode__(self):
		return self.SUser.get_full_name()

	def lastName(self):
		return self.SUser.last_name

	def firstName(self):
		return self.SUser.first_name
		

class Subject(models.Model):
	Code = models.CharField(max_length=6)
	Desc = models.CharField(max_length=60)

	def __unicode__(self):
		return self.Desc

class Course(models.Model):
	Subject = models.ForeignKey(Subject)
	CourseNum = models.FloatField()
	Desc = models.CharField(max_length=100)
	Title = models.CharField(max_length=60)
	Units = models.FloatField()

	def __unicode__(self):
		return self.Title


class Syllabus(models.Model):
	Degree = models.ForeignKey(Degree)
	Course = models.ForeignKey(Course)
	Year = models.IntegerField()
	Semester = models.IntegerField()

class Teacher(models.Model):
	Name = models.CharField(max_length=100)

class CourseComponents(models.Model):
	CourseID = models.ForeignKey(Course)
	ComponentID = models.IntegerField()
	isRequired = models.BooleanField()

class CoursePreReq(models.Model):
	CourseID = models.ForeignKey(Course)
	PreReqID = models.IntegerField()

class SubjectStatus(models.Model):
	Desc = models.CharField(max_length=20) # waitlist, drop, enrolled, enlisted



class ScheduleStatus(models.Model):
	Desc = models.CharField(max_length=10) # open, close

class Class(models.Model):
	TeacherID = models.ForeignKey(Teacher)
	CourseID = models.ForeignKey(Course)
	Section = models.CharField(max_length=3)
	StartTime = models.TimeField()
	EndTime = models.TimeField()
	DaysOffered = models.CharField(max_length=100)
	Room = models.CharField(max_length=50)
	Status = models.ForeignKey(ScheduleStatus)
	ClassCapacity = models.IntegerField()

class StudentSchedule(models.Model):
	ScheduleID = models.ForeignKey(Class)
	StudentID = models.ForeignKey(Student)
	Status = models.ForeignKey(SubjectStatus)

class CourseOffered(models.Model):
	CourseID = models.ForeignKey(Course)
	Semester = models.IntegerField()
	Year = models.CharField(max_length=10)



class Scholarship(models.Model):
	Desc = models.CharField(max_length=100)
	isGovernment = models.BooleanField()
	Amount = models.FloatField()


class STS(models.Model):
	BracketName = models.CharField(max_length=10)
	BracketDesc = models.CharField(max_length=100)
	PercentDiscount = models.FloatField()
	Stipend = models.BooleanField()

class StudentFinance(models.Model):
	StudentID = models.ForeignKey(Student)
	STSID = models.ForeignKey(STS)
	ScholarshipID = models.ForeignKey(Scholarship)

class ScholarshipStatus(models.Model):
	Desc = models.CharField(max_length=50) #active, suspended, terminated

class AddressType(models.Model):
	Desc = models.CharField(max_length=100)

class Address(models.Model):
	StudentID = models.ForeignKey(Student)
	AddressType = models.ForeignKey(AddressType)
	HouseNumber = models.CharField(max_length=10)
	Brgy = models.CharField(max_length=100)
	City = models.CharField(max_length=100)
	Landline = models.CharField(max_length=100)


# class UserProfile(models.Model):  
#     user = models.ForeignKey(User, unique=True)
# 	StdNum = models.CharField(max_length=9, blank=False, validators=[stdNumValidator])
# 	MiddleName = models.CharField(max_length=50)
# 	BirthDate = models.DateField()
# 	StudentType = models.ForeignKey(StudentType)
# 	Sex = models.ForeignKey(Sex)
# 	CivilStatus = models.ForeignKey(CivilStatus)
# 	Citizenship = models.ForeignKey(Citizenship)

#     def __unicode__(self):
#         return u'Profile of user: %s' % self.user.username


