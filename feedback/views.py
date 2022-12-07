from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.views.generic import FormView

from feedback import forms


class Feedback(FormView):
    template_name = 'feedback/question.html'
    form = forms.FormFeedback

    def form_valid(self, form):
        form.save()
        send_mail(
            'Theme of letter',
            form.cleaned_data.get('text'),
            'from@example.com',
            ['to_1@example.com', 'to_2@example.com'],
            fail_silently=False
        )
        return super().form_valid(form)

    def get(self, request):
        form = forms.FormFeedback(request.POST or None)
        context = {
            'form': form
        }
        return render(request, 'feedback/question.html', context)

    def post(self, request):
        form = forms.FormFeedback(request.POST or None)
        form.save()
        send_mail(
            'Theme of letter',
            form.cleaned_data.get('text'),
            'from@example.com',
            ['to_1@example.com', 'to_2@example.com'],
            fail_silently=False
        )
        return redirect('feedback:feedback')
