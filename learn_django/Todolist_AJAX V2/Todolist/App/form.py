from django import forms
from App.models import Things


class ThingsForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(ThingsForm, self).clean()
        value = cleaned_data.get('things')
        try:
            Things.objects.get(things=value)
            self._errors['things'] = self.error_class(["这件事已经有啦"])
        except Things.DoesNotExist:
            pass
        print(cleaned_data)
        return cleaned_data

    class Meta:
        model = Things
        exclude = ("id",)


