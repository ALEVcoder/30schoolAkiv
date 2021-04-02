from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    if request.method == 'POST':
        ism = request.POST['user']
        famm = request.POST['fam']
        nomer = request.POST['nomer']
        xabar = request.POST['xabar']
        
        title = ism
        msg='Sizga '+ism+'dan xabar bor '+'\nFamilyasi:'+famm+'\nNomeri: '+nomer + '\nXabari:'+xabar

        print(ism, xabar, nomer)
        send_mail(
            ism,
            msg,
            nomer,
            ['alevcoder1@gmail.com'],
            fail_silently=False,
        )
        
        print('Xabaringiz ketti')
    return render(request, 'index.html')

def blog_detail(request):
    return render(request, 'blog-detail.html')