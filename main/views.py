from django.shortcuts import render


def chat(request):
    return render(request, 'chat.html', {})


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })


def index(request):
    return render(request, 'index.html')


def lesson(request):
    return render(request, 'lesson.html')


def personal(request):
    return render(request, 'personal.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def subject(request):
    return render(request, 'subject.html')


def timetable(request):
    return render(request, 'timetable.html')
