from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306209870',
        'name': 'Meisya Najla Aqilah',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)