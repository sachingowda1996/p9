from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
    path('trail/',views.trail,name="Trail"),
    path('profile/',views.profile,name="profile"),
    path('fact/<n>',views.fact,name='fact'),
    path('second/',views.second,name="second"),
    path('third/',views.second,name="third"),
    path('fourth/',views.second,name="fourth"),
    path('fifth/',views.second,name="fifth"),
    path('url_data/<name>',views.urls_data,name="urls_data"),
    path("ab/<a>/<b>",views.ab,name="ab"),
    path("great_2_number/<a>/<b>",views.great_2_number,name="great_2_number"),
    path("reverse/<a>",views.reverse,name="reverse"),
]
