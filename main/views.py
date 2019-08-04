from django.shortcuts import render
from emoji import emojize
from django.views.generic import TemplateView
from services.emoji import predict
# Create your views here.

class Index(TemplateView):
    template_name='index.html'

    def post(self,request):
        content= request.POST['content']
        
        sentences= content.split('.')
        emojis= list(map(predict, sentences))
        emojized_content=''
        for sentence, emoji in zip(sentences,emojis):
            emojized_content += sentence+emojize(emoji)+"."


        context={
            "emojized_content": emojized_content
        } 
        return render(request,self.template_name,context)
