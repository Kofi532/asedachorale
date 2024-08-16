from django.shortcuts import render



# Create your views here
from django.shortcuts import render

def ret_(request):
    # You can set a default value for number_of_columns if not provided
    number_of_columns = int(request.GET.get('columns', 7))
    
    notes = ['d', 'r', 'm', 'f', 's', 'l', 't', 'Rest']
    durations = [0.25, 0.5, 0.75, 1, 2, 3, 4]
    
    voice_parts = {
        'Soprano': notes[:number_of_columns],
        'Alto': notes[:number_of_columns],
        'Tenor': notes[:number_of_columns],
        'Bass': notes[:number_of_columns],
    }
    
    notes_range = range(1, number_of_columns + 1)  # Generate a range based on the number of columns

    context = {
        'voice_parts': voice_parts,
        'notes_range': notes_range,
        'note_options': notes,
        'duration_options': durations,
    }
    return render(request, 'home.html', context)


from django.shortcuts import render
from django.http import JsonResponse
import json


def ret_(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            data = body.get('data', [])
            # Process the data as needed
            print(data)  # Debugging: Check the data structure
            return JsonResponse({'status': 'success', 'data': data})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'})

    number_of_columns = int(request.GET.get('columns', 7))

    notes = ['d', 'r', 'm', 'f', 's', 'l', 't', 'Rest']
    durations = [0.25, 0.5, 0.75, 1, 2, 3, 4]
    
    # Extend notes list to match number_of_columns
    extended_notes = notes * ((number_of_columns // len(notes)) + 1)
    
    voice_parts = {
        'Soprano': extended_notes[:number_of_columns],
        'Alto': extended_notes[:number_of_columns],
        'Tenor': extended_notes[:number_of_columns],
        'Bass': extended_notes[:number_of_columns],
    }
    
    notes_range = range(1, number_of_columns + 1)  # Generate a range based on the number of columns

    context = {
        'voice_parts': voice_parts,
        'notes_range': notes_range,
        'note_options': notes,
        'duration_options': durations,
    }
    return render(request, 'home.html', context)


from django.shortcuts import render
from django.http import JsonResponse
import json

def ret(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            data = body.get('data', [])
            # Process the data as needed
            print(data)  # Debugging: Check the data structure
            return JsonResponse({'status': 'success', 'data': data})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'})

    number_of_columns = int(request.GET.get('columns', 7))

    notes = ['d', 'r', 'm', 'f', 's', 'l', 't', 'Rest']
    durations = [0.25, 0.5, 0.75, 1, 2, 3, 4]

    # Extend notes list to match number_of_columns
    extended_notes = notes * ((number_of_columns // len(notes)) + 1)

    voice_parts = {
        'Soprano': extended_notes[:number_of_columns],
        'Alto': extended_notes[:number_of_columns],
        'Tenor': extended_notes[:number_of_columns],
        'Bass': extended_notes[:number_of_columns],
    }

    notes_range = range(1, number_of_columns + 1)  # Generate a range based on the number of columns

    # Default values for specific columns and rows
    default_values = {
        ('Soprano', 1): ['r', 'high', 3]
    }

    context = {
        'voice_parts': voice_parts,
        'notes_range': notes_range,
        'note_options': notes,
        'duration_options': durations,
        'default_values': default_values,
    }
    return render(request, 'home.html', context)


from django.shortcuts import render
from django.http import JsonResponse
import json
from django.shortcuts import render
import json

def rett_(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            data = body.get('data', [])
            # Process the data as needed
            print(data)  # Debugging: Check the data structure
            return JsonResponse({'status': 'success', 'data': data})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'})

    number_of_columns = 7  # Assuming a fixed number of columns

    # Define default values for each voice part
    soprano_default = ['d', 'None', 'None', 'None', 'None', 'None', 'None']
    alto_default = ['r', 'None', 'None', 'None', 'None', 'None', 'None']
    tenor_default = ['m', 'None', 'None', 'None', 'None', 'None', 'None']
    bass_default = ['f', 'None', 'None', 'None', 'None', 'None', 'None']

    notes = ['d', 'r', 'm', 'f', 's', 'l', 't', 'Rest']
    durations = [0.25, 0.5, 0.75, 1, 2, 3, 4]

    # Extend notes list to match number_of_columns
    extended_notes = notes * ((number_of_columns // len(notes)) + 1)

    voice_parts = {
        'Soprano': soprano_default[:number_of_columns],
        'Alto': alto_default[:number_of_columns],
        'Tenor': tenor_default[:number_of_columns],
        'Bass': bass_default[:number_of_columns],
    }

    notes_range = range(1, number_of_columns + 1)  # Generate a range based on the number of columns

    context = {
        'voice_parts': voice_parts,
        'notes_range': notes_range,
        'note_options': notes,
        'duration_options': durations,
    }
    return render(request, 'noteform.html', context)

from .forms import NoteFormSet


from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def note_form_view(request):
    note_options = ['None', 'd', 'r', 'm', 'f', 's', 'l', 't', 'd']
    duration_options = ['None', 0.25, 1, 2, 3]
    flat_sharp_options = ['None', 'flat', 'sharp']
    octave_options = ['None', 'low', 'high']
    n = 3  # Example value, this can be dynamically set

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received data:", data)  # Debug: print received data
            # You can process the data here, e.g., save to database

            return JsonResponse({'message': 'Data submitted successfully!'})
        except Exception as e:
            print("Error processing data:", e)  # Debug: print error
            return JsonResponse({'error': 'Error submitting data.'}, status=500)

    formset = NoteFormSet(form_kwargs={
        'note_options': note_options,
        'duration_options': duration_options,
        'flat_sharp_options': flat_sharp_options,
        'octave_options': octave_options,
        'n': n,
    })

    context = {
        'formset': formset,
        'n': n,
    }

    return render(request, 'noteform_.html', context)

from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd

# Example data (replace with your actual data source)
data = {
    'Soprano': ['m', 'low', 'None', '2', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
    'Alto': ['None', 'None', 'None', 'None', 'm', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],
    'Tenor': ['None', 'None', 'None', 'None', 'None', 'low', 'None', 'None', 'None', 'None', 'None', 'None'],
    'Bass': ['None', 'None', 'None', 'None', 'None', 'high', 'flat', 'None', 'None', 'None', 'None', 'None']
}

# Create DataFrame
df = pd.DataFrame(data)

def table_view(request):
    # Use DataFrame index as column headers
    headers = df.columns.tolist()  # This will give you ['Soprano', 'Alto', 'Tenor', 'Bass']

    # Prepare data for template
    rows = df.values.tolist()

    context = {
        'headers': headers,
        'rows': rows,
    }
    return render(request, 'jot.html', context)

def update_cell(request):
    if request.method == 'POST' and request.is_ajax():
        row = int(request.POST.get('row'))
        col = int(request.POST.get('col'))
        value = request.POST.get('value')
        
        # Update DataFrame cell
        df.iloc[row, col] = value
        
        # Optionally, you can save the updated DataFrame to a file or database
        
        return JsonResponse({'message': 'Cell updated successfully.'})
    else:
        return JsonResponse({'error': 'Invalid request.'}, status=400)
