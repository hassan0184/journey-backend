from django.urls import path
from .views import FormatChoicesView

urlpatterns = [
    path("format_choices/", FormatChoicesView.as_view(), name="format_choices"),
]
