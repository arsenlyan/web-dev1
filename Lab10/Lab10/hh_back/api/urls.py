from django.urls import path
from .views import (
    CompanyList, CompanyDetail, CompanyVacancies,
    VacancyList, VacancyDetail, TopTenVacancies
)
from .views import company_list, company_detail
from .views import VacancyListCreate, VacancyRUD

urlpatterns = [
    path('companies/', company_list),
    path('companies/<int:id>/', company_detail),
    
    path('vacancies/', VacancyListCreate.as_view()),
    path('vacancies/<int:pk>/', VacancyRUD.as_view()),

    path('companies/<int:id>/vacancies/', CompanyVacancies.as_view()),

    path('vacancies/top_ten/', TopTenVacancies.as_view()),
]

#Former

'''
urlpatterns = [
    path('companies/', CompanyList.as_view()),
    path('companies/<int:pk>/', CompanyDetail.as_view()),
    path('companies/<int:id>/vacancies/', CompanyVacancies.as_view()),

    path('vacancies/', VacancyList.as_view()),
    path('vacancies/<int:pk>/', VacancyDetail.as_view()),
    path('vacancies/top_ten/', TopTenVacancies.as_view()),
]
'''