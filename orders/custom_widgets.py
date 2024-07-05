# widgets.py

from django.forms import RadioSelect
from django.utils.safestring import mark_safe

class ImageRadioSelect(RadioSelect):
    template_name = 'widgets/image_radio_select.html'

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)
        if value.instance:
            option['image_url'] = value.instance.image.url
        return option
