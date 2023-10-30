from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "./base.html")

def account(request):
    return render(request, "./account/account.html")

def abuse(request):
    return render(request, "./abuse/abuse.html")

def account(request):
    return render(request, "./account/account.html")

def activities(request):
    return render(request, "./activities/activities.html")

def adverts(request):
    return render(request, "./adverts/adverts.html")

def emails(request):
    return render(request, "./emails/emails.html")

def features(request):
    return render(request, "./features/features.html")

def info_pages(request):
    return render(request, "./info_pages/info_pages.html")

def languages(request):
    return render(request, "./languages/languages.html")

def media(request):
    return render(request, "./media/media.html")

def messenger(request):
    return render(request, "./messenger/messenger.html")

def modals(request):
    return render(request, "./modals/modals.html")

def payments(request):
    return render(request, "./payments/payments.html")

def payouts(request):
    return render(request, "./payouts/payouts.html")

def post(request):
    return render(request, "./post/post.html")

def reels(request):
    return render(request, "./reels/reels.html")

def timeline(request):
    return render(request, "./timeline/timeline.html")

def user(request):
    return render(request, "./user/user.html")