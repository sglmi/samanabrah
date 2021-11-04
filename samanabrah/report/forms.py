from django import forms

from .models import Report
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["date", "text"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date"] = JalaliDateField(
            label="تاریخ",  # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget(
                attrs={
                    "placeholder": "تاریخ گزارش را انتخاب کنید",
                    "autocomplete": "off",
                }
            ),
        )
        self.fields["text"] = forms.CharField(
            label="متن گزارش",
            max_length=255,
            widget=forms.Textarea(
                attrs={
                    "placeholder": "متن گزارش را به صورت خلاصه و مفید بنویسید",
                    "rows": 5,
                    "class": "countdown",
                }
            ),
        )
