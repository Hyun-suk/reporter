from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse

from django.db.models import Count

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.models import User
from .models import Reporter, Article
from .forms import NewReporterForm


class ReporterListView(ListView):
    model = Reporter
    context_object_name = 'reporters'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        kwargs['sports_reporters'] = Reporter.objects.filter(categories__name='스포츠')
        return super().get_context_data(**kwargs)


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'articles.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        kwargs['reporter'] = self.reporter
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.reporter = get_object_or_404(Reporter, id=self.kwargs.get('reporter_id'))
        queryset = Article.objects.filter(published_by=self.reporter).order_by('-published_at')
        return queryset


@login_required
def new_reporter(request):

    if request.method == 'POST':
        form = NewReporterForm(request.POST)
        if form.is_valid():
            reporter = form.save(commit=False)
            reporter.save()
            return redirect('reporters:reporters_list')  # TODO: redirect to the created topic page
    else:
        form = NewReporterForm()
    return render(request, 'new_reporter.html', {'form': form})


# class TopicListView(ListView):
#     model = Topic
#     context_object_name = 'topics'
#     template_name = 'topics.html'
#     paginate_by = 20
#
#     def get_context_data(self, **kwargs):
#         kwargs['board'] = self.board
#         return super().get_context_data(**kwargs)
#
#     def get_queryset(self):
#         self.board = get_object_or_404(Board, id=self.kwargs.get('board_id'))
#         queryset = self.board.topics.order_by('-updated_at').annotate(replies=Count('posts') - 1)
#         return queryset

# def board_topics(request, board_id):
#     board = get_object_or_404(Board, id=board_id)
#     queryset = board.topics.order_by('-updated_at').annotate(replies=Count('posts') - 1)
#     page = request.GET.get('page', 1)
#
#     paginator = Paginator(queryset, 20)
#
#     try:
#         topics = paginator.page(page)
#     except PageNotAnInteger:
#         # fallback to the first page
#         topics = paginator.page(1)
#     except EmptyPage:
#         # probably the user tried to add a page number
#         # in the url, so we fallback to the last page
#         topics = paginator.page(paginator.num_pages)
#
#     return render(request, 'topics.html', {'board': board, 'topics': topics})
