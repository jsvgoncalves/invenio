from wtforms import TextAreaField

__all__ = ['AbstractField']


class AbstractField(TextAreaField):

    def __init__(self, **kwargs):
        self._icon_html = '<i class="icon-pencil"></i>'
        super(AbstractField, self).__init__(**kwargs)

    def pre_validate(self):
        return dict(error=0, error_message='')

    def autocomplete(self):
        return []