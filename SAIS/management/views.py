from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from management.models import *

def forgetPassword(request):
	if request.POST:
		user = User()
		email = request.POST['email']
		u = User.objects.all().filter(email=email)

		use = u[0]
		use.set_password('12345678')
		use.save()
		

	return render(request, 'management/forget-password.html')

def index(request):
	return render(request, 'management/home.html')

def logoutUser(request):
	logout(request)
	return render(request, 'management/log-in.html')

def loginUser(request):
	if request.user.is_authenticated():
		return render(request, 'management/home.html')
	else:
		if request.POST:
			user = User()
			username = request.POST['username']
			password = request.POST['password']
			try:
				print username
				username = Student.objects.get(StdNum=username)
				print username
			except Exception, e:
				return render(request, 'management/log-in.html')
			
			username = username.SUser
			user = authenticate(username=username, password=password)

			if user is not None:
				login(request,user)
				return render(request, 'management/home.html')

			return render(request, 'management/log-in.html')
		else:
			return render(request, 'management/log-in.html')


def studentprofile(request):
	print request.user.id
	sNumber = Student.objects.get(SUser=request.user.id).StdNum
	fName = User.objects.get(id=request.user.id).first_name
	lName = User.objects.get(id=request.user.id).last_name
	sex = Student.objects.get(SUser=request.user.id).Sex
	cStat = Student.objects.get(SUser=request.user.id).CivilStatus
	degree = Student.objects.get(SUser=request.user.id).Degree
	email = User.objects.get(id=request.user.id).email
	print fName
	return render(request, 'management/profile.html', {'number':sNumber, 'fName':fName, 'lName':lName, 'sex':sex, 'cStat':cStat,'degree':degree, 'email':email}) #, {'getUser' : getUser}

def workflow(request):
	user = request.user
	return render(request, 'management/approval-workflow.html')

def addresses(request):
	userID = request.user.id
	studentID = Student.objects.get(SUser=userID).id
	HousingType = Address.objects.get(StudentID=studentID, AddressType=1).HousingType
	print HousingType
	HouseNumber = Address.objects.get(StudentID=studentID, AddressType=1).HouseNumber
	Brgy = Address.objects.get(StudentID=studentID, AddressType=1).Brgy
	City = Address.objects.get(StudentID=studentID, AddressType=1).City
	Landline = Address.objects.get(StudentID=studentID, AddressType=1).Landline

	HousingType2 = Address.objects.get(StudentID=studentID, AddressType=2).HousingType
	HouseNumber2 = Address.objects.get(StudentID=studentID, AddressType=2).HouseNumber
	Brgy2 = Address.objects.get(StudentID=studentID, AddressType=2).Brgy
	City2 = Address.objects.get(StudentID=studentID, AddressType=2).City
	Landline2 = Address.objects.get(StudentID=studentID, AddressType=2).Landline
	return render(request, 'management/profile/addresses.html', {'HousingType':HousingType,'HouseNumber':HouseNumber, 'Brgy':Brgy, 'City':City, 'Landline':Landline, 'HousingType2':HousingType2,'HouseNumber2':HouseNumber2, 'Brgy2':Brgy2, 'City2':City2, 'Landline2':Landline2})


# def demographicinfo(request):
# 	return render(request, 'management/profile/demographic-info.html')

# def personalinfo(request):
# 	return render(request, 'management/profile/personal-info.html')

def emergencycontacts(request):
	userID = request.user.id
	studentID = Student.objects.get(SUser=userID).id
	father = Parents.objects.get(StudentID=studentID).FatherName
	fatherOccu = Parents.objects.get(StudentID=studentID).FatherOccu
	mother = Parents.objects.get(StudentID=studentID).MotherName
	motherOccu = Parents.objects.get(StudentID=studentID).MotherOccu
	gName = Guardian.objects.get(StudentID=studentID).Name	
	gOccu = Guardian.objects.get(StudentID=studentID).Occupation
	gHouseNumber = Guardian.objects.get(StudentID=studentID).HouseNumber
	gBrgy = Guardian.objects.get(StudentID=studentID).Barangay
	gCity =Guardian.objects.get(StudentID=studentID).City
	gLandline = Guardian.objects.get(StudentID=studentID).Landline
	sName = SendDocs.objects.get(StudentID=studentID).Name	
	sOccu = SendDocs.objects.get(StudentID=studentID).Occupation
	sHouseNumber = SendDocs.objects.get(StudentID=studentID).HouseNumber
	sBrgy = SendDocs.objects.get(StudentID=studentID).Barangay
	sCity =SendDocs.objects.get(StudentID=studentID).City
	sLandline = SendDocs.objects.get(StudentID=studentID).Landline
	return render(request, 'management/profile/emergency-contacts.html', {'father':father, 'fatherOccu':fatherOccu, 'mother':mother, 'motherOccu': motherOccu, 'gName':gName, 'gOccu':gOccu, 'gHouseNumber':gHouseNumber, 'gBrgy':gBrgy, 'gCity':gCity, 'gLandline':gLandline, 'sName':sName, 'sOccu':sOccu, 'sHouseNumber':sHouseNumber, 'sBrgy':sBrgy, 'sCity':sCity, 'sLandline':sLandline})

def internetaddresses(request):
	return render(request, 'management/profile/internet-addresses.html')

# def studentinfo(request):
# 	return render(request, 'management/profile/student-info.html')

def otherinfo(request):
	return render(request, 'management/profile/other-info.html')

def studentcenter(request):
	return render(request, 'management/student-center.html')

def studyplan(request):
	return render(request, 'management/student_center/study-plan.html')

def classsched(request):
	return render(request, 'management/student_center/class-sched.html')

def examsched(request):
	return render(request, 'management/student_center/exam-sched.html')

def viewgrades(request):
	return render(request, 'management/student_center/view-grades.html')

def htds(request):
	return render(request, 'management/student_center/holds-and-todos.html')

def termstats(request):
	return render(request, 'management/student_center/term-stats.html')

def transcript(request):
	return render(request, 'management/student_center/transcript.html')

def coursehist(request):
	return render(request, 'management/student_center/course-history.html')

def search(request):
	return render(request, 'management/search-or-browse.html')

def classsearch(request):
	return render(request, 'management/search_browse/class-search.html')

def browsecourse(request):
	return render(request, 'management/search_browse/browse-catalog.html')

def enrollment(request):
	return render(request, 'management/enrollment.html')

def enrollmentsched(request):
	return render(request, 'management/enrollment/enrollment-sched.html')

def addclass(request):
	return render(request, 'management/enrollment/add-class.html')

def dropclass(request):
	return render(request, 'management/enrollment/drop-class.html')

def finances(request):
	return render(request, 'management/finances.html')

def acctinquiry(request):
	return render(request, 'management/campus-finances/acct-inquiry.html')

def financialaids(request):
	return render(request, 'management/campus-finances/financial-aids.html')

def paymentplan(request):
	return render(request, 'management/campus-finances/payment-plan.html')

# def acadrecords(request):
# 	return render(request, 'management/acad-records.html')


