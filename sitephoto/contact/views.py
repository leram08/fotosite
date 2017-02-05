from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from contact.forms import *
from contact.models import Orders
from django.shortcuts import render_to_response


def contact(request):
        all_is_right=''
        if request.method == 'POST':
                form = ContactForm(request.POST)
                if form.is_valid():
                        #import pdb; pdb.set_trace()
                        orders = Orders(name=form.cleaned_data['name'], email=form.cleaned_data['email'], message=form.cleaned_data['message'])
                        orders.save()
                        all_is_right ="Ваше сообщение успешно отправлено"
                        form = ContactForm()
        else:
                form = ContactForm()

        return render(request, 'contact.html', {'form':form, 'all_is_right': all_is_right,})

