from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('facilities_location', views.fac_loc, name="fac_loc"),
    path('request_librarians', views.req_lib, name="req_lib"),
    path('FAQ', views.faq, name="faq"),
    path('Booking_facilities', views.book_fac, name="book_fac"),
    path("Search_Results", views.search_results, name="search_results"),
]