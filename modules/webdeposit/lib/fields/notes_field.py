from wtforms import TextAreaField

__all__ = ['NotesField']


class NotesField(TextAreaField):

    def __init__(self, **kwargs):
        self._icon_html = '<i class="icon-list"></i>'
        super(NotesField, self).__init__(**kwargs)

    def pre_validate(self):
        return dict(error=0, error_message='')

    def autocomplete(self):
        return []