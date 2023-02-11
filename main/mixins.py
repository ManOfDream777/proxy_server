from typing import Any
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse
from .services.utils import parse_html
import requests


class BaseMixin(TemplateView):
    template_name = 'main/index.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        request_uri = request.path[:-1]
        query_params = ''
        if request.GET:
            last_value = tuple(request.GET)[-1]
            request_uri += '?'
            for query_param in request.GET.keys():
                if query_param == last_value:
                    query_params += f'{query_param}={request.GET.get(query_param)}'
                else:
                    query_params += f'{query_param}={request.GET.get(query_param)}&'

        reqq = requests.get(f'https://news.ycombinator.com{request_uri}{query_params}', headers={
                            'Content-type': 'text', 'SomeHeader': 'exists'})
        body, title = parse_html(reqq.text)
        context = super().get_context_data(**kwargs)
        context['body'] = body
        context['title'] = title
        return super().get(request, *args, **context)
