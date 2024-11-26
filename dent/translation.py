from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Team)
class TeamTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

@register(Prices)
class PricesTranslationOptions(TranslationOptions):
    fields = ('description', 'services', 'prices')


@register(Descriptions)
class DescriptionsTranslationOptions(TranslationOptions):
    fields = ('home_page_description',)

