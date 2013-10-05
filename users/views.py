# Create your views here.

from django.views.generic import TemplateView, DetailView
from models import Category, Genre, Fiction
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class FunficsView(TemplateView):
    template_name = "funfics.html"

    def get_context_data(self, **kwargs):
        data = super(FunficsView, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        genres = Genre.objects.all()
        data['categories'] = categories
        data['genres'] = genres
        return data

# lines = []
#     for i in range(10000):
#         lines.append(u'Line %s' % (i + 1))
#     paginator = Paginator(lines, 10)
#     page = request.GET.get('page')
#     try:
#         show_lines = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         show_lines = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range (e.g. 9999), deliver last page of results.
#         show_lines = paginator.page(paginator.num_pages)
#     return render_to_response('pagination.html', RequestContext(request, {
#         'lines': show_lines,
#     }))


class CategoryView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = "category.html"

    def get_object(self):
        object = super(CategoryView, self).get_object()
        return object

    def get_context_data(self, **kwargs):
        data = super(CategoryView, self).get_context_data(**kwargs)

        lines = Fiction.objects.all().filter(category=self.object)

        paginator = Paginator(lines, 20)
        page = self.request.GET.get('page')
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            show_lines = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            show_lines = paginator.page(paginator.num_pages)
        data['lines'] = show_lines
        data['paginator'] = paginator

        return data


class GenreView(DetailView):
    model = Genre
    context_object_name = 'genre'
    template_name = "genre.html"

    def get_object(self):
        object = super(GenreView, self).get_object()
        return object

    def get_context_data(self, **kwargs):
        data = super(GenreView, self).get_context_data(**kwargs)

        lines = Fiction.objects.all().filter(genre=self.object)

        paginator = Paginator(lines, 20)
        page = self.request.GET.get('page')
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            show_lines = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            show_lines = paginator.page(paginator.num_pages)
        data['lines'] = show_lines
        data['paginator'] = paginator

        return data


class FictionView(DetailView):
    model = Fiction
    context_object_name = 'fiction'
    template_name = "fiction_detail.html"

    def get_object(self):
        object = super(FictionView, self).get_object()
        return object

    def get_context_data(self, **kwargs):
        data = super(GenreView, self).get_context_data(**kwargs)
        return data
