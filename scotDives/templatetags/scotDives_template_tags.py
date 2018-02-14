from django import template
from scotDives.models import DiveSiteList

register = template.Library()


@register.inclusion_tag('scotDives/divesitelist.html')
def get_divesite_list(page=None):
    return {'pages': Pages.objects.all(),
            'act_page': page}

