from django.shortcuts import render, redirect, reverse
from .models import VideoAnime, Usuario
from .forms import CriarContaForm, FormHomepage
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# bloqueia as paginas que nao abre sem login

class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHomepage

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('filmes:homefilmes')
        else:
            return super().get(request, *args, **kwargs) # redireciona para a homepage

    def get_success_url(self):
        email = self.request.POST.get("email")
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('filmes:login')
        else:
            return reverse('filmes:criarconta')

        return

class Homefilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = VideoAnime

class Detalhesfilme(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilme.html"
    model = VideoAnime

    def get(self, request, *args, **kwargs):# contador de visualizacoes
        #descobrir qual o filme ele ta acessando
        filmes = self.get_object()
        #contabilizar
        filmes.visualizacoes += 1
        filmes.save()
        usuario = request.user
        usuario.filmes_vistos.add(filmes)
        return super().get(request, *args, **kwargs) # redireciona o usuario para a url final

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        filmes_relacionados = VideoAnime.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["filmes_relacionados"] = filmes_relacionados
        return context

class PesquisaFilme(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = VideoAnime

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = VideoAnime.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None

class PaginaPerfil(LoginRequiredMixin, UpdateView):
    template_name = "editarperfil.html"
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse ('filmes:homefilmes')

class Criarconta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse ('filmes:login')

    #object list e o nome da lista
# listview voce importa a url a ser exibida e a lista do banco de dados do models



# FUNCTION BASE VIEW

#def homepage(request):
#    return render(request, "homepage.html")


# def homefilmes(request):
#    context = {}
#    lista_filmes = VideoSurebet.objects.all()
#    context['lista_filmes'] = lista_filmes
#    return render(request, "homefilmes.html", context)


