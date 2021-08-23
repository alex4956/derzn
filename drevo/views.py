from django.db.models import Count, Q
from django.views.generic import ListView, TemplateView, DetailView
from .models import Category, Znanie, Relation, Tr, Author, Label, GlossaryTerm


class DrevoListView(ListView):
    """
    выводит сущности Знание для заданной рубрики
    """
    template_name = 'drevo/type.html'
    model = Znanie
    context_object_name = 'znanie'

    def get_queryset(self):
        """
        формирует выборку из сущностей Знание для вывода
        """
        category_pk = self.kwargs['pk']
        qs = Znanie.published.filter(category__pk=category_pk)
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Передает данные в шаблон
        """
        context = super().get_context_data(**kwargs)
        # текущая категория
        category = Category.published.get(pk=self.kwargs['pk'])
        context['category'] = category
        return context


class DrevoView(TemplateView):
    """
    Выводит древо с иерархией категорий
    """
    template_name = 'drevo/drevo.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Передает данные в шаблон
        """
        context = super().get_context_data(**kwargs)
        # формирует список категорий
        categories = Category.tree_objects.exclude(is_published=False)
        context['ztypes'] = categories

        # формирование списка Знаний по категориям
        zn = Znanie.published.all()
        zn_dict = {}
        for category in categories:
            zn_in_this_category = zn.filter(category=category)
            zn_dict[category.name] = zn_in_this_category
        context['zn_dict'] = zn_dict

        return context


class ZnanieDetailView(DetailView):
    """
    Выводит подробную информацию о сущности Знание
    """
    model = Znanie
    context_object_name = 'znanie'
    template_name = 'drevo/znanie_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Передает в шаблон данные через контекст
        """
        context = super().get_context_data(**kwargs)

        # первичный ключ текущей записи
        pk = self.object.pk

        # получаем список связей, в который базовым знанием является текущее знание
        qs = Relation.objects.filter(bz__pk=pk)

        # получаем список всех видов связей
        ts = Tr.objects.all()

        context['rels'] = [[item.name, qs.filter(tr=item, rz__is_published=True)]
                           for item in ts if qs.filter(tr=item, rz__is_published=True).count() > 0]

        return context


class LabelsListView(ListView):
    """
    выводит список меток
    """
    template_name = 'drevo/labels.html'
    model = Label
    context_object_name = 'labels'
    queryset = Label.objects.annotate(zn_num=Count('znanie',
                                                   filter=Q(znanie__is_published=True))).\
        all().order_by('name')


class ZnanieByLabelView(ListView):
    """
    выводит сущности Знание для заданной метки
    """
    template_name = 'drevo/zlabel.html'
    model = Znanie
    context_object_name = 'znanie'

    def get_queryset(self):
        """
        формирует выборку из сущностей Знание для вывода
        """
        # получаем из запроса порядковый номер текущей метки
        label_pk = self.kwargs['pk']

        # получаем query set Знание, имеющих такую же метку
        qs = Znanie.published.filter(labels__id__in=[label_pk, ])
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Передает в шаблон данные через контекст
        """
        context = super().get_context_data(**kwargs)

        context['label'] = Label.objects.get(pk=self.kwargs['pk'])

        return context


class AuthorsListView(ListView):
    """
    выводит список авторов
    """
    template_name = 'drevo/authors_list.html'
    model = Author
    context_object_name = 'authors'
    queryset = Author.objects.annotate(zn_num=Count('znanie', filter=Q(znanie__is_published=True))).all()


class AuthorDetailView(DetailView):
    """
    Выводит подробную информацию об Авторе
    """
    model = Author
    context_object_name = 'author'
    template_name = 'drevo/author_details.html'


class GlossaryListView(ListView):
    """
    выводит список терминов глоссария
    """
    template_name = 'drevo/glossary.html'
    model = GlossaryTerm
    context_object_name = 'glossary_terms'
    queryset = GlossaryTerm.objects.filter(is_published=True)
