import django
from django.db import models
from cms import settings
from django import forms
from django.utils.text import capfirst

class NamedFlagsFormField(forms.fields.MultipleChoiceField):
    hidden_widget = forms.MultipleHiddenInput
    widget = forms.CheckboxSelectMultiple
    def __init__(self, *args, **kwargs):
        self.coerce = kwargs.pop('coerce', lambda val: val)
        self.empty_value = kwargs.pop('empty_value', '')
        return super(NamedFlagsFormField, self).__init__(*args, **kwargs)
    def clean(self, value):
        """
        Validate that the value is in self.choices and can be coerced to the
        right type.
        """
        value = super(NamedFlagsFormField, self).clean(value)
        if value == self.empty_value or value in forms.fields.EMPTY_VALUES:
            return self.empty_value

        # Hack alert: This field is purpose-made to use with Field.to_python as
        # a coercion function so that ModelForms with choices work. However,
        # Django's Field.to_python raises
        # django.core.exceptions.ValidationError, which is a *different*
        # exception than django.forms.util.ValidationError. So we need to catch
        # both.
        try:
            value = self.coerce(value)
        except (ValueError, TypeError, django.core.exceptions.ValidationError):
            raise forms.ValidationError(self.error_messages['invalid_choice'] % {'value': value})
        return value
    

class NamedFlagsField(models.Field):
    __metaclass__ = models.SubfieldBase
    def __init__(self, *args, **kwargs):
        null, blank = kwargs.pop('null',True), kwargs.pop('blank', True)
        choices = kwargs.pop('choices', settings.CMS_PAGE_FLAGS)
        super(NamedFlagsField, self).__init__(null=True, blank=True, choices=choices, *args, **kwargs)
    def get_internal_type(self):
        return 'TextField'
    def south_field_triple(self):
        "Returns a suitable description of this field for South."
        # We'll just introspect ourselves, since we inherit.
        from south.modelsinspector import introspector
        field_class = "django.db.models.fields.TextField"
        args, kwargs = introspector(self)
        kwargs['null'] = True
        kwargs['blank'] = True
        return (field_class, args, kwargs)
    def to_python(self, value):
        if isinstance(value, list):
            return value
        if value:
            active_flags = value.split(',')
        else:
            active_flags = []
        return active_flags
    def get_db_prep_value(self, value):
        if isinstance(value, list):
            active_flags = value
        else:
            active_flags = []
        return ','.join(active_flags)
    def formfield(self, **kwargs):
        "Returns a django.forms.Field instance for this database Field."
        defaults = {'required': not self.blank, 'label': capfirst(self.verbose_name), 'help_text': self.help_text}
        if self.has_default():
            defaults['initial'] = self.get_default()
            if callable(self.default):
                defaults['show_hidden_initial'] = True
        if self.choices:
            # Fields with choices get special treatment.
            #include_blank = self.blank or not (self.has_default() or 'initial' in kwargs)
            include_blank=False
            defaults['choices'] = self.get_choices(include_blank=include_blank)
            defaults['coerce'] = self.to_python
            if self.null:
                defaults['empty_value'] = None
            form_class = NamedFlagsFormField
            # Many of the subclass-specific formfield arguments (min_value,
            # max_value) don't apply for choice fields, so be sure to only pass
            # the values that TypedChoiceField will understand.
            for k in kwargs.keys():
                if k not in ('coerce', 'empty_value', 'choices', 'required',
                             'widget', 'label', 'initial', 'help_text',
                             'error_messages'):
                    del kwargs[k]
        defaults.update(kwargs)
        return form_class(**defaults)