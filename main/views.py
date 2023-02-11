from django.views.generic import TemplateView
from .mixins import BaseMixin


class MainPage(BaseMixin):
    pass


class NewestView(BaseMixin, TemplateView):
    pass


class FrontView(BaseMixin, TemplateView):
    pass


class NewCommentsView(BaseMixin, TemplateView):
    pass


class AskView(BaseMixin, TemplateView):
    pass


class ShowView(BaseMixin, TemplateView):
    pass


class JobsView(BaseMixin, TemplateView):
    pass


class SubmitView(BaseMixin, TemplateView):
    pass


class LoginView(BaseMixin, TemplateView):
    pass


class ItemView(BaseMixin, TemplateView):
    pass


class UserView(BaseMixin, TemplateView):
    pass


class ContextView(BaseMixin, TemplateView):
    pass


class HideView(BaseMixin, TemplateView):
    pass


class FromView(BaseMixin, TemplateView):
    pass


class FaveView(BaseMixin, TemplateView):
    pass


class ShowNewView(BaseMixin, TemplateView):
    pass