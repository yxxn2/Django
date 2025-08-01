from django.shortcuts import render

# 메인 페이지 뷰

def home(request):
    return render(request, "core/home.html")
