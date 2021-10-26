from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import reverse


class Report(models.Model):
    date = models.DateField(default=timezone.now)
    text = models.TextField()
    employee = models.ForeignKey(User, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse("users:report_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"Report of {self.employee.username.upper()} in date {self.date}"
