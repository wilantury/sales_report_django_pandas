# Django
from django.urls import path
# Views
from .views import (
    create_report_view, 
    ReportDetailView, 
    ReportListView
)

app_name = 'reports'

urlpatterns = [
    path('save/', create_report_view, name='create-reports'),
    path('', ReportListView.as_view(), name='main'),
    path('<pk>/', ReportDetailView.as_view(), name='detail'),
]
