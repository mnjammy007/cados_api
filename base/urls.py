from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import Endpoint, AdvocateList, AdvocateDetails, CompanyList

urlpatterns = [
    path("", Endpoint.as_view(), name="endpoints"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("advocates/", AdvocateList.as_view(), name="advocate_list"),
    path(
        "advocates/<str:username>/", AdvocateDetails.as_view(), name="advocate_details"
    ),
    path("companies/", CompanyList.as_view(), name="company_list"),
]
