from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from product.models import CommentForm, Comment, Images, ImagesForm, Category


def index(request):
    return HttpResponse("Product Page")

@login_required(login_url='/login')
def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user = request.user

            data = Comment()
            data.user_id = current_user.id
            data.product_id = id
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Yorumunuz başarı ile gönderilmiştir. Teşekkür ederiz..")
            return HttpResponseRedirect(url)
    messages.warning(request, "Yorumunuz kaydedilmedi")
    return HttpResponseRedirect(url)


@login_required(login_url='/login')
def gallery(request, id):
    category = Category.objects.all()
    images = Images.objects.filter(product_id=id)
    form = ImagesForm()
    context = {
        'images': images,
        'id': id,
        'form': form,
        'category': category,
    }

    return render(request, 'gallery.html', context)


@login_required(login_url='/login')
def addgallery(request, id):
    if request.method == 'POST':  # form post edildiyse
        form = ImagesForm(request.POST, request.FILES)
        if form.is_valid():
            data = Images()
            data.title = form.cleaned_data['title']
            data.image = form.cleaned_data['image']
            data.product_id = id
            data.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/login')
def deletegallery(request, id):
    Images.objects.get(pk=id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))