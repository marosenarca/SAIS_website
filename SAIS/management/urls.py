from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$',views.loginUser, name='log-in'),
	url(r'^logout/$',views.logoutUser, name='log-out'),
	url(r'^home/$',views.index, name='index'),
	url(r'^profile/$',views.studentprofile, name='profile'),
	url(r'^student-center/$',views.studentcenter, name='student-center'),
	url(r'^enrollment/$',views.enrollment, name='enrollment'),
	url(r'^search-or-browse/$',views.search, name='search-or-browse'),
	url(r'^campus-finances/$',views.finances, name='campus-finances'),
	url(r'^approval-workflow/$',views.workflow, name='approval-workflow'),
	# url(r'^academic-records/$',views.acadrecords, name='acad-records'),
	url(r'^profile/addresses$',views.addresses, name='addresses'),
	# url(r'^profile/demographic-info$',views.demographicinfo, name='demographic-info'),
	# url(r'^profile/personal-info$',views.personalinfo, name='personal-info'),
	url(r'^profile/emergency-contacts$',views.emergencycontacts, name='emergency-contacts'),
	url(r'^profile/internet-addresses$',views.internetaddresses, name='internet-addresses'),
	# url(r'^profile/sudent-info$',views.studentinfo, name='student-info'),
	url(r'^profile/other-info$',views.otherinfo, name='other-info'),
	url(r'^student-center/study-plan$',views.studyplan, name='study-plan'),
	url(r'^student-center/class-schedule$',views.classsched, name='class-schedule'),
	url(r'^student-center/exam-schedule$',views.examsched, name='exam-schedule'),
	url(r'^student-center/view-grades$',views.viewgrades, name='view-grades'),
	url(r'^student-center/holds-and-todos$',views.htds, name='holds-and-todos'),
	url(r'^student-center/term-statistics$',views.termstats, name='term-statistics'),
	url(r'^student-center/view-transcript$',views.transcript, name='view-transcript'),
	url(r'^student-center/course-history$',views.coursehist, name='course-history'),
	url(r'^search-or-browse/class-search$',views.classsearch, name='class-search'),
	url(r'^search-or-browse/browse-courses$',views.browsecourse, name='browse-courses'),
	url(r'^enrollment/enrollment-schedule$',views.enrollmentsched, name='enrollment-schedule'),
	url(r'^enrollment/add-class$',views.addclass, name='add-class'),
	url(r'^enrollment/add-class/step-two$',views.steptwo, name='add-class-two'),
	url(r'^enrollment/add-class/step-three$',views.stepthree, name='add-class-three'),
	url(r'^enrollment/drop-class$',views.dropclass, name='drop-class'),
	url(r'^campus-finances/account$',views.acctinquiry, name='acct-inquiry'),
	url(r'^campus-finances/financial-aids$',views.financialaids, name='financial-aids'),
	url(r'^campus-finances/payment-plan$',views.paymentplan, name='payment-plan'),

	]