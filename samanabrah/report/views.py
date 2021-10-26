from django.shortcuts import render


def add_report(request):
    # require add report form.
    return render(request, "report/add_report.html")
