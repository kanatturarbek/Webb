from django.urls import path
from api.views import company_list,company_detail,company_vacancies,vacancy_detail,vacancy_list,topten
urlpatterns = [
    path('companies/',company_list),
    path('companies/<int:company_id>',company_detail),
    path('vacancies/',vacancy_list),
    path('vacancies/<int:vacancy_id>',vacancy_detail),
    path('companies/<int:company_id>/vacancies/',company_vacancies),
    path('vacancies/top_ten',topten)
]   