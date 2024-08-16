# forms.py
from django import forms
from django.forms import formset_factory


class NoteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        note_options = kwargs.pop('note_options')
        duration_options = kwargs.pop('duration_options')
        flat_sharp_options = kwargs.pop('flat_sharp_options')
        octave_options = kwargs.pop('octave_options')
        n = kwargs.pop('n')
        super(NoteForm, self).__init__(*args, **kwargs)

        for i in range(n):
            self.fields[f'note_{i+1}'] = forms.ChoiceField(choices=[(opt, opt) for opt in note_options], label=f'Note {i+1}')
            self.fields[f'octave_{i+1}'] = forms.ChoiceField(choices=[(opt, opt) for opt in octave_options], label=f'Octave {i+1}')
            self.fields[f'flat_sharp_{i+1}'] = forms.ChoiceField(choices=[(opt, opt) for opt in flat_sharp_options], label=f'Flat/Sharp {i+1}')
            self.fields[f'duration_{i+1}'] = forms.ChoiceField(choices=[(opt, opt) for opt in duration_options], label=f'Duration {i+1}')

NoteFormSet = formset_factory(NoteForm, extra=4)

# forms.py
# forms.py

class DynamicForm(forms.Form):
    def __init__(self, *args, **kwargs):
        n = kwargs.pop('n', 1)
        default_values = kwargs.pop('default_values', {})

        super(DynamicForm, self).__init__(*args, **kwargs)

        for i in range(1, n + 1):
            defaults = default_values.get(f'{i}', ['None', 'None', 'None', 'None'])
            self.fields[f'Note{i}'] = forms.ChoiceField(choices=[(opt, opt) for opt in ['None', 'd', 'r', 'm', 'f', 's', 'l', 't', 'd']], initial=defaults[0])
            self.fields[f'flat_sharp{i}'] = forms.ChoiceField(choices=[(opt, opt) for opt in ['None', 'flat', 'sharp']], initial=defaults[1])
            self.fields[f'Octave{i}'] = forms.ChoiceField(choices=[(opt, opt) for opt in ['None', 'low', 'high']], initial=defaults[2])
            self.fields[f'Duration{i}'] = forms.ChoiceField(choices=[(opt, opt) for opt in ['None', '0.25', '1', '2', '3']], initial=defaults[3])
