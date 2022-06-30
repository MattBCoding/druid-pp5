from django.shortcuts import render, redirect
from .forms import ContactMessageForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home/home.html', context)

def contact(request):
    '''
    View to provide contact page
    '''
    form = ContactMessageForm()

    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            new_message = form.save()
            contact_email = new_message.email
            contact_subject = new_message.subject
            contact_message = new_message.message
            # email to internal address
            internal_subject = render_to_string(
                'home/emails/contact_email_subject.txt',
                {'subject': contact_subject}
            )
            internal_body = render_to_string(
                'home/emails/contact_email_body.txt',
                {
                    'message': contact_message,
                    'subject': contact_subject,
                    'customer': contact_email,
                    }
            )
            send_mail(
                internal_subject,
                internal_body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL]
            )
            # email to customer contacting us confirming receipt
            external_subject = render_to_string(
                'home/emails/customer_contact_email_subject.txt',
                {'subject': contact_subject}
            )
            external_body = render_to_string(
                'home/emails/customer_contact_email_body.txt',
                {
                    'subject': contact_subject,
                    'message': contact_message,
                    }
            )
            send_mail(
                external_subject,
                external_body,
                settings.DEFAULT_FROM_EMAIL,
                [contact_email]
            )
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('contact')
        else:
            messages.error(request, 'All fields are required in the form.\
                                    please double check and try again.')
    
    context = {
        'form': form,
    }
    return render(request, 'home/contact.html', context)
