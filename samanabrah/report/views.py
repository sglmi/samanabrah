from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import ReportForm
from .models import Report


# class ReportListView(ListView):
#     model = Report
#     template_name = "report/reports.html"
#     context_object_name = "reports"
#     ordering = ["-date"]


# class ReportDetailView(DetailView):
#     model = Report


class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
    form_class = ReportForm
    template_name = "report/create.html"

    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)


# class ReportUpdateView(LoginRequiredMixin, UpdateView):
#     model = Report
#     form_class = ReportForm
#     template_name = "report/update.html"

#     def form_valid(self, form):
#         form.instance.employee = self.request.user
#         return super().form_valid(form)


# class ReportDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Report
#     success_url = "/report"

#     def test_func(self):
#         Report = self.get_object()
#         if self.request.user == Report.employee:
#             return True
#         return False
