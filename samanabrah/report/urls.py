from django.urls import path

from . import views


app_name = "report"

urlpatterns = [
    path("create/", views.ReportCreateView.as_view(), name="create"),
    # path("<int:pk>/", views.ReportDetailView.as_view(), name="detail"),
    # path(
    #     "<int:pk>/update/",
    #     views.ReportUpdateView.as_view(),
    #     name="update",
    # ),
    # path(
    #     "<int:pk>/delete/",
    #     views.ReportDeleteView.as_view(),
    #     name="delete",
    # ),
]
