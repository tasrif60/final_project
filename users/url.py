from django.urls import path, include
from users.views import login, home_page, reset_pass, create_profile
#
# from final_project import views


urlpatterns = [

    path('', login),
    path('dashboard.html', home_page),
    path('recovery_pass.html', reset_pass),
    path('Profile_form.html', create_profile),
]

