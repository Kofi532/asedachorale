from django.shortcuts import render
from music21 import note, stream, tempo, configure, chord
import re
import music21
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import redirect
from django.http import HttpResponse
import os
<<<<<<< HEAD
# from fuzzywuzzy import fuzz
# import fluidsynth
from IPython.display import display, Audio
=======
from fuzzywuzzy import fuzz

import fluidsynth
# from IPython.display import display, Audio
>>>>>>> d64141e793585eba81673de8af9f37b259e7a589
from midi2audio import FluidSynth
from django.http import FileResponse
from django.views import View
from pydub import AudioSegment
import random
import string
<<<<<<< HEAD
from django.shortcuts import render
import mido
import base64
=======
from django.conf import settings

>>>>>>> d64141e793585eba81673de8af9f37b259e7a589
# from .models import NoteList
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
import time
# "C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\lyrics"
# "C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a"
# "C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a"
# "C:\Users\Asamoah\Desktop\kofi\aseda_a"
# "C:\Users\Asamoah\Desktop\kofi\aseda_a"

@csrf_exempt  # Only for demonstration purposes, not recommended for production
def handle_click_presby(request):
    lists = list(range(1, 1001))
    directory = r"adom\templates\lyrics_presby"
    kpo = []

    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                kpo.append(entry.name)
    file_list = kpo

    # Remove '.html' from each element in the list
    file_list = [file_name.replace('.html', '') for file_name in file_list]
    def rearrange_list(input_list):
        def extract_integer(s):
            # Extracts the integer part from the string
            num = ''
            for char in s:
                if char.isdigit():
                    num += char
                else:
                    break
            return int(num) if num else None

        # Custom sorting function based on extracted integers
        def sort_key(elem):
            return extract_integer(elem)

        # Sort the list based on extracted integers
        sorted_list = sorted(input_list, key=sort_key)
        return sorted_list

    # Example list
    original_list = file_list

    # Rearrange the list
    rearranged_list = rearrange_list(original_list)
    lists = rearranged_list
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                kpo.append(entry.name)

    value_to_retrieve = request.GET.get('value_to_pass', None)
    print('hard')
    print(value_to_retrieve)
    if value_to_retrieve is not None:
        clicked_value = value_to_retrieve
        request.session['clicked_value'] = clicked_value
        # return JsonResponse({'status': 'success'})
        def generate_random_word():
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(4))

        random_word = generate_random_word()
        midi_file_path = f'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\media\\{random_word}.mid'
        # score.write('midi', fp=midi_file_path)
        request.session['random_word'] = random_word
        midi_messages = 1
        path = f"C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\tunes_ang\\{clicked_value}.xml"
        score = music21.converter.parse(path)
        score.write('midi', fp=midi_file_path)

        return render(request, 'lyrics_presby/'+str(clicked_value)+'.html', {'lists': lists, 'clicked_value':clicked_value})

<<<<<<< HEAD
    if request.method == 'POST':
        clicked_value = request.POST.get('num')
        request.session['clicked_value'] = clicked_value
        print(clicked_value)  # For demonstration, you can use this value as needed


        # return JsonResponse({'status': 'success'})
        def generate_random_word():
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(4))

        random_word = generate_random_word()
        midi_file_path = f'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\media\\{random_word}.mid'
        # score.write('midi', fp=midi_file_path)
        request.session['random_word'] = random_word
        midi_messages = 1 
        # try:
        path = f"C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\tunes_ang\\{clicked_value}.xml"
        
        score = music21.converter.parse(path)
        score.write('midi', fp=midi_file_path)

        # except:
        #     return render(request, 'sorry.html', {'lists': lists})
        return render(request, 'lyrics_presby/'+str(clicked_value)+'.html', {'lists': lists, 'clicked_value':clicked_value, 'midi_messages':midi_messages})
        # return render(request, 'lyricshtml', {'lists': lists})
        # return redirect('landing_page', value_one=first_value)
    return render(request, 'base_presby.html', {'lists': lists})

    # return redirect('landing_page') + f'?value_one={first_value}'





@csrf_exempt  # Only for demonstration purposes, not recommended for production
def handle_click_ang(request):
    lists = list(range(1, 1001))
    directory = r"adom\templates\lyrics_ang"
    kpo = []

    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                kpo.append(entry.name)
    file_list = kpo

    # Remove '.html' from each element in the list
    file_list = [file_name.replace('.html', '') for file_name in file_list]
    def rearrange_list(input_list):
        def extract_integer(s):
            # Extracts the integer part from the string
            num = ''
            for char in s:
                if char.isdigit():
                    num += char
                else:
                    break
            return int(num) if num else None

        # Custom sorting function based on extracted integers
        def sort_key(elem):
            return extract_integer(elem)

        # Sort the list based on extracted integers
        sorted_list = sorted(input_list, key=sort_key)
        return sorted_list

    # Example list
    original_list = file_list

    # Rearrange the list
    rearranged_list = rearrange_list(original_list)
    lists = rearranged_list
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                kpo.append(entry.name)

    value_to_retrieve = request.GET.get('value_to_pass', None)
    print('hard')
    print(value_to_retrieve)
    if value_to_retrieve is not None:
        clicked_value = value_to_retrieve
        request.session['clicked_value'] = clicked_value
        # return JsonResponse({'status': 'success'})
        def generate_random_word():
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(4))

        random_word = generate_random_word()
        midi_file_path = f'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\media\\{random_word}.mid'
        # score.write('midi', fp=midi_file_path)
        request.session['random_word'] = random_word
        midi_messages = 1
        path = f"C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\tunes_ang\\{clicked_value}.xml"
        score = music21.converter.parse(path)
        score.write('midi', fp=midi_file_path)

        return render(request, 'lyrics_ang/'+str(clicked_value)+'.html', {'lists': lists, 'clicked_value':clicked_value})

    if request.method == 'POST':
        clicked_value = request.POST.get('num')
        request.session['clicked_value'] = clicked_value
        print(clicked_value)  # For demonstration, you can use this value as needed


        # return JsonResponse({'status': 'success'})
        def generate_random_word():
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(4))

        random_word = generate_random_word()
        midi_file_path = f'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\media\\{random_word}.mid'
        # score.write('midi', fp=midi_file_path)
        request.session['random_word'] = random_word
        midi_messages = 1 
        # try:
        path = f"C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\tunes_ang\\{clicked_value}.xml"
        
        score = music21.converter.parse(path)
        score.write('midi', fp=midi_file_path)

        # except:
        #     return render(request, 'sorry.html', {'lists': lists})
        return render(request, 'lyrics_ang/'+str(clicked_value)+'.html', {'lists': lists, 'clicked_value':clicked_value, 'midi_messages':midi_messages})
        # return render(request, 'lyricshtml', {'lists': lists})
        # return redirect('landing_page', value_one=first_value)
    return render(request, 'base_ang.html', {'lists': lists})

    # return redirect('landing_page') + f'?value_one={first_value}'

def handle_click(request):
    lists = list(range(1, 1001))
    directory = r"adom\templates\lyrics_try"
    kpo = []

    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                kpo.append(entry.name)
    file_list = kpo

    # Remove '.html' from each element in the list
    file_list = [file_name.replace('.html', '') for file_name in file_list]
    def rearrange_list(input_list):
        def extract_integer(s):
            # Extracts the integer part from the string
            num = ''
            for char in s:
                if char.isdigit():
                    num += char
                else:
                    break
            return int(num) if num else None
        # Custom sorting function based on extracted integers
        def sort_key(elem):
            return extract_integer(elem)

        # Sort the list based on extracted integers
        sorted_list = sorted(input_list, key=sort_key)
        return sorted_list

    # Example list
    original_list = file_list

    # Rearrange the list
    rearranged_list = rearrange_list(original_list)
    lists = rearranged_list
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                kpo.append(entry.name)

    value_to_retrieve = request.GET.get('value_to_pass', None)
    print('hard')
    print(value_to_retrieve)
    if value_to_retrieve is not None:
        clicked_value = value_to_retrieve
        request.session['clicked_value'] = clicked_value
        # return JsonResponse({'status': 'success'})
        def generate_random_word():
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(4))

        random_word = generate_random_word()
        midi_file_path = f'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\media\\{random_word}.mid'
        # score.write('midi', fp=midi_file_path)
        request.session['random_word'] = random_word
        midi_messages = 1
        path = f"C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\tunes\\{clicked_value}.xml"
        score = music21.converter.parse(path)
        score.write('midi', fp=midi_file_path)

        return render(request, 'lyrics/'+str(clicked_value)+'.html', {'lists': lists, 'clicked_value':clicked_value})

    if request.method == 'POST':
        clicked_value = request.POST.get('num')
        request.session['clicked_value'] = clicked_value
        print(clicked_value)  # For demonstration, you can use this value as needed


        # return JsonResponse({'status': 'success'})
        def generate_random_word():
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(4))

        random_word = generate_random_word()
        midi_file_path = f'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\media\\{random_word}.mid'
        # score.write('midi', fp=midi_file_path)
        request.session['random_word'] = random_word
        midi_messages = 1 
        # try:
        path = f"C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\tunes\\{clicked_value}.xml"
        
        score = music21.converter.parse(path)
        score.write('midi', fp=midi_file_path)

        # except:
        #     return render(request, 'sorry.html', {'lists': lists})
        return render(request, 'lyrics_try/'+str(clicked_value)+'.html', {'lists': lists, 'clicked_value':clicked_value, 'midi_messages':midi_messages})
        # return render(request, 'lyricshtml', {'lists': lists})
        # return redirect('landing_page', value_one=first_value)
    return render(request, 'base.html', {'lists': lists})



def display_hymn(request):
    def extract_html_file_names(directory):
        # List all files ending with .html
        html_files = [file for file in os.listdir(directory) if file.endswith('.html')]

        # Extract base names without extension
        base_names = [re.match(r'(.+?)\.html', file).group(1) for file in html_files]

        # Sort using a custom key
        def custom_sort_key(name):
            # Split into parts: numbers and non-numbers
            parts = re.split(r'(\d+)', name)
            # Convert numeric parts to integers for correct sorting
            parts = [int(part) if part.isdigit() else part for part in parts]
            return parts

        sorted_base_names = sorted(base_names, key=custom_sort_key)
        return sorted_base_names

    # Example usage:
    directory_path = 'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\lyrics' # Replace with your directory path
    html_files_list = extract_html_file_names(directory_path)
    hymn_numbers = html_files_list  # Define the list of hymn numbers
    hymn_number = request.GET.get('hymn_number')


##
    if hymn_number is not None:
        print('there is the')
        print(type(hymn_number))
        print((hymn_number))
        # hymn_number = hymn_number.replace('mhb', '')
        # hymn_number = str(hymn_number)
        def generate_random_word():
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(4))

        random_word = generate_random_word()
        midi_file_path = f'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\media\\{random_word}.mid'
        # score.write('midi', fp=midi_file_path)
        request.session['random_word'] = random_word
        request.session['number_ofhymn'] = 'mhb'+hymn_number

        midi_messages = 1
        path = f"C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\tunes\\{hymn_number}.xml"
        score = music21.converter.parse(path)
        score.write('midi', fp=midi_file_path)
        hymn_data = fetch_hymn_from_file(hymn_number)
        # Initialize a list to store notes and rests at each point in time
        notes_and_rests_by_time = []
        notes_and_rests_by_time_ = []

        # Get all the notes, chords, and rests from the score
        all_notes = score.flat.getElementsByClass(music21.note.GeneralNote)

        # Create a dictionary to group elements by their starting offset
        elements_by_offset = {}

        # Iterate through the notes, chords, and rests and group them by offset
        for element in all_notes:
            offset = element.offset
            if offset not in elements_by_offset:
                elements_by_offset[offset] = []
            elements_by_offset[offset].append(element)

        # Sort the offsets in ascending order
        sorted_offsets = sorted(elements_by_offset.keys())

        notss = []

        # Iterate through the sorted offsets and collect notes and rests at each point in time
        for offset in sorted_offsets:
            elements = elements_by_offset[offset]
            notes_and_rests = []
            nots=[]

            for element in elements:
                if isinstance(element, music21.note.Note):
                    pitch = element.pitch
                    parts = re.split(r'(\d+)', str(pitch))
                    modified_item = ''.join(parts)
                    pitch = modified_item
                    notes_and_rests.append(f"{pitch}") # {element.duration.quarterLength}
                    nots.append(f"{pitch} {element.duration.quarterLength}")

                elif isinstance(element, music21.chord.Chord):
                    for chord_note in element:
                        chord_pitch = chord_note.pitch
                        parts = re.split(r'(\d+)', str(chord_pitch))
                        modified_item = ''.join(parts)
                        chord_pitch = modified_item
                        notes_and_rests.append(f"{chord_pitch}") # {chord_note.duration.quarterLength}
                        nots.append(f"{chord_pitch} {chord_note.duration.quarterLength}")

                elif isinstance(element, music21.note.Rest):
                    pass
                    # notes_and_rests.append(f"Rest Duration: {element.duration.quarterLength}")

            notes_and_rests_by_time.append(notes_and_rests)
            notes_and_rests_by_time_.append(nots)
            notes = notes_and_rests_by_time_
#
            data = notes
            # Function to extract note and octave
            def get_note_octave(note):
                parts = note.split()
                note_part = parts[0][:-1]
                octave = int(parts[0][-1])
                return note_part, octave

            # Sort each sublist by octave and then by note alphabetically
            sorted_data = [
                sorted(sublist, key=lambda x: (get_note_octave(x)[1], get_note_octave(x)[0]), reverse=True)
                for sublist in data
            ]

            sorted_data
#
            data = sorted_data
            data = notes_and_rests_by_time_
            # Function to remove duplicates if sublist has more than 4 members
            def remove_excess_duplicates(data):
                new_data = []
                for sublist in data:
                    if len(sublist) > 4:
                        seen = set()
                        filtered = []
                        for item in sublist:
                            if item not in seen:
                                seen.add(item)
                                filtered.append(item)
                            elif len(filtered) < 4:
                                filtered.append(item)
                        new_data.append(filtered[:4])
                    else:
                        new_data.append(sublist)
                return new_data

            result = remove_excess_duplicates(data)
            # print(result)
            notes_and_rests_by_time_ = result
            notes_and_rests_by_time_ = result
        # print('fir the check')
        # print(notes_and_rests_by_time_)
        for sublist in notes:
            if len(sublist) < 4:
                # print("A sublist has fewer than 4 items:", sublist)
                # Create DataFrame
                df = pd.DataFrame(notes, columns=['Note1', 'Note2', 'Note3', 'Note4'])

                # Function to extract duration from note string
                def extract_duration(note):
                    if isinstance(note, str):
                        parts = note.split()
                        if len(parts) == 2 and parts[1].replace('.', '').isdigit():
                            return float(parts[1])
                    return 0.0

                # Add cumulative duration columns
                for col in df.columns:
                    df[col + '_Cumulative'] = df[col].apply(extract_duration).cumsum()

                # Display the updated DataFrame
                # print(df)
                # Get the index of the first sublist with less than 4 members
                index = next((i for i, sublist in enumerate(notes) if len(sublist) < 4), None)
                index = index -1
                # print("Index of the first sublist with less than 4 members:", index)
                # Function to check the next sublist after the given index
                def check_next_sublist_length(notes, index):
                    if index + 1 < len(notes):
                        next_sublist = notes[index + 1]
                        return len(next_sublist) < 4
                    return False

                # Check the next sublist
                has_less_than_4_items = check_next_sublist_length(notes, index)
                # print(f"The next sublist after index {index} has less than 4 items: {has_less_than_4_items}")
                # Retrieve the highest cumulative duration and corresponding column names
                def get_highest_cumulative_info(df, index):
                    if index >= 0:
                        # Get the cumulative duration values for the specified row
                        cumulative_values = df.iloc[index, df.columns.str.endswith('_Cumulative')]
                        # Find the maximum value
                        max_duration = cumulative_values.max()
                        # Get the column names with the maximum value
                        columns_with_max_duration = cumulative_values[cumulative_values == max_duration].index.tolist()
                        return max_duration, columns_with_max_duration
                    return None, []

                # Execute the function
                max_duration, columns_with_max_duration = get_highest_cumulative_info(df, index)

                # print(f"Highest cumulative duration at index {index}: {max_duration}")
                # print("Column names with this highest cumulative duration:", columns_with_max_duration)
                # Define the lists
                list1 = ['Note1_Cumulative', 'Note2_Cumulative', 'Note3_Cumulative', 'Note4_Cumulative']
                list2 = columns_with_max_duration

                # Retrieve members in list1 that are not in list2
                result = [item for item in list1 if item not in list2]

                # print(result)  # Output: ['Note2_Cumulative']

                def replace_cumulative_notes(lst):
                    replacements = {
                        'Note1_Cumulative': 0,
                        'Note2_Cumulative': 1,
                        'Note3_Cumulative': 2,
                        'Note4_Cumulative': 3
                    }
                    
                    return [replacements.get(item, item) for item in lst]

                # Example usage
                input_list = ['Note1_Cumulative', 'Note2_Cumulative', 'Other', 'Note3_Cumulative', 'Note4_Cumulative']
                input_list = result
                output_list = replace_cumulative_notes(input_list)
                original_list =notes[index + 1]
                desired_length = 4

                # Create a new list with '-' as placeholders
                modified_list = ['-'] * desired_length

                # Insert the original list elements at their respective indexes
                indices = output_list

                # Ensure the indices length matches the original_list length
                for i, item in enumerate(original_list):
                    if i < len(indices):
                        modified_list[indices[i]] = item


                # New value to replace notes[6]
                new_value = modified_list
                # Replace the element at index 6
                notes[index+1] = new_value
                
                # Print the updated list
                aaa = notes.copy()
            else:
                aaa = notes_and_rests_by_time_.copy()
            
        def note_to_solfa(note, key):
            solfa_mappings = {
            'C major': {
                'C': 'd', 'D': 'r', 'E': 'm', 'F': 'f', 'G': 's',
                'A': 'l', 'B': 't', 'C#': 'di', 'D#': 'ri', 'F#': 'fi',
                'G#': 'si', 'A#': 'li'
            },
            'C# major': {
                'C#': 'd', 'D#': 'r', 'E#': 'm', 'F#': 'f', 'G#': 's',
                'A#': 'l', 'B#': 't', 'D': 'ra', 'F': 'fa', 'A': 'la'
            },
            'B minor': {
                'B': 'd', 'C#': 'r', 'D': 'm', 'E': 'f', 'F#': 's',
                'G': 'l', 'A': 't', 'E#': 'fi', 'A#': 'ti', 'C': 'ma'
            },
            'A minor': {
                'A': 'd', 'B': 'r', 'C': 'm', 'D': 'f', 'E': 's',
                'F': 'l', 'G': 't', 'C#': 'mi', 'D#': 'fi', 'G#': 'te'
            },
            'A major': {
                'A': 'd', 'B': 'r', 'C#': 'm', 'D': 'f', 'E': 's',
                'F#': 'l', 'G#': 't', 'D#': 'fi', 'G': 'le'
            },
            'D minor': {
                'D': 'd', 'E': 'r', 'F': 'm', 'G': 'f', 'A': 's',
                'B-': 'l', 'C': 't', 'E-': 'ri', 'A-': 'se'
            },
            'G minor': {
                'G': 'd', 'A': 'r', 'B-': 'm', 'C': 'f', 'D': 's',
                'E-': 'l', 'F': 't', 'A-': 'fi', 'D#': 'si'
            },
            'G major': {
                'G': 'd', 'A': 'r', 'B': 'm', 'C': 'f', 'D': 's',
                'E': 'l', 'F#': 't', 'F': 'fi', 'C#': 'fi'
            },
            'E- major': {
                'E-': 'd', 'F': 'r', 'G': 'm', 'A-': 'f', 'B-': 's',
                'C': 'l', 'D': 't', 'A': 'se', 'B': 'ma'
            },
            'C minor': {
                'C': 'd', 'D': 'r', 'E-': 'm', 'F': 'f', 'G': 's',
                'A-': 'l', 'B-': 't', 'E': 'mi', 'A': 'li'
            },
            'B- major': {
                'B-': 'd', 'C': 'r', 'D': 'm', 'E-': 'f', 'F': 's',
                'G': 'l', 'A': 't', 'D#': 'ra', 'F#': 'si'
            },
            'A- major': {
                'A-': 'd', 'B-': 'r', 'C': 'm', 'D-': 'f', 'E-': 's',
                'F': 'l', 'G': 't', 'D': 'ma', 'E': 'li'
            },
            'D major': {
                'D': 'd', 'E': 'r', 'F#': 'm', 'G': 'f', 'A': 's',
                'B': 'l', 'C#': 't', 'G#': 'ma', 'E#': 'ri'
            },
            'B- minor': {
                'B-': 'd', 'C': 'r', 'D-': 'm', 'E-': 'f', 'F': 's',
                'G-': 'l', 'A-': 't', 'E': 'mi', 'G': 'fi'
            },
            'F minor': {
                'F': 'd', 'G': 'r', 'A-': 'm', 'B-': 'f', 'C': 's',
                'D-': 'l', 'E-': 't', 'B': 'si', 'G-': 'fi'
            },
            'E minor': {
                'E': 'd', 'F#': 'r', 'G': 'm', 'A': 'f', 'B': 's',
                'C': 'l', 'D': 't', 'A#': 'li', 'G#': 'si'
            },
            'F major': {
                'F': 'd', 'G': 'r', 'A': 'm', 'B-': 'f', 'C': 's',
                'D': 'l', 'E': 't', 'C#': 'fi', 'G#': 'le'
            },
            'E major': {
                'E': 'd', 'F#': 'r', 'G#': 'm', 'A': 'f', 'B': 's',
                'C#': 'l', 'D#': 't', 'A#': 'li', 'B#': 'si'
            }
        }
            
            mapping = solfa_mappings[key]
            if note == '-':
                return '-'
            note_name, duration = note.split()
            note_name = note_name[:-1]  # Remove the octave number
            solfa = mapping.get(note_name, note_name)
            return f"{solfa} {duration}"

        notes_ = notes
        # Get the key signature
        key_signature = score.analyze('key')

    #
        def capitalize_first_letter(s):
            if s and s[0].islower():
                return s[0].upper() + s[1:]
            return s

        # Example usage
        strin = str(key_signature)
        capitalized_string = capitalize_first_letter(strin)
        music_key = capitalized_string
#
        print(f"The key of the piece is: {key_signature}")
        solfa_notes = [[note_to_solfa(note, key=capitalized_string) for note in chord] for chord in notes_]
        chords = []
        for chord in solfa_notes:
            chords.append(chord)
        notes = chords

        # Remove sublists with all members being '-'
        filtered_notes = [sublist for sublist in notes if sublist.count('-') < 4]

        filtered_notes
        new_data = filtered_notes.copy()
        data = [(index + 1, *row) for index, row in enumerate(new_data)]
        tempo = request.GET.get('tempo','1x')

        selected_voice_part = request.GET.get('voice_part')
        if selected_voice_part:
            if selected_voice_part == 'All':
                pass
            else:
                if tempo:
                    tempo_map = {   
                        '1x':1,
                        '3x': 0.60,
                        '2x': 0.85,
                        '-2x': 1.30,
                        '-3x': 1.50,
                    }

                    tempo_num = tempo_map.get(tempo)
                    request.session['tempo_num'] = tempo_num
                else:
                    tempo_num = 1
                voice_map = {
                    'Soprano': 0,
                    'Alto': 1,
                    'Tenor': 2,
                    'Bass': 3
                }

                kogi = selected_voice_part
                voice_num = voice_map.get(kogi)


                # Given music notes
                try:
                    music_notes = notes_
                    # print(music_notes)
                except NameError:
                    music_notes = notes_.copy()
                    print(f'music notes are except {music_notes}')
                note_a = music_notes
                # Remove empty sublists
                filtered_notes = [sublist for sublist in note_a if sublist]

                music_notes = filtered_notes.copy()
                print('Ongoing')
                print(music_notes)
                # Create a stream
                melody = stream.Stream()

                # Extract and add the first note from each sublist
                for sublist in music_notes:
                    note_str = sublist[voice_num]  # First member of each sublist
                    if note_str == '-':
                        pass
                    else:

                        pitch, duration = note_str.split()  # Split into pitch and duration
                        duration = float(duration)  # Convert duration to float
                        # Create a note object and add it to the stream
                        n = note.Note(pitch)
                        n.quarterLength = duration*tempo_num
                        melody.append(n)

                # Show (and play) the stream
                # melody.show('midi')

                def generate_random_word():
                    letters = string.ascii_lowercase
                    return ''.join(random.choice(letters) for _ in range(4))

                random_word = generate_random_word()
                midi_file_path = f'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\media\\{random_word}.mid'
                # score.write('midi', fp=midi_file_path)
                request.session['random_word'] = random_word
                midi_messages = 1
                path = f"C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\tunes\\{hymn_number}.xml"
                # score = music21.converter.parse(path)
                melody.write('midi', fp=midi_file_path)
                # hymn_data = fetch_hymn_from_file_ang(hymn_number)


        if hymn_data:
            hymn_data = re.sub(r'(?<!HYMN\s)(\d+)(?=\s)', r'<br><br> \1', hymn_data)
            aa = type(hymn_data)
            # Retrieve the AudioRecord for the given hymn_number and logged-in user, if it exists
            random_letters = None
            # print(f"1this is the randomess {hymn_number}")
            if request.user.is_authenticated:
                # print('hemmy')
                try:
                    audio_record = AudioRecord.objects.get(user=request.user, hymn_number='mhb'+hymn_number)
                    random_letters = audio_record.random_letters
                    request.session['hymn_number'] = 'mhb'+hymn_number
                    request.session['random_letters'] = random_letters
                    # print(f"this is the randomess {random_letters}")
                except AudioRecord.DoesNotExist:
                    random_letters = None
                return render(request, 'hymn_display.html', {'hymn_number':hymn_number, 'hymn_data': hymn_data, 'random_letters':random_letters, 'data':data, 'music_key': music_key, 'selected_voice_part': selected_voice_part, 'hymn_numbers': hymn_numbers})
            return render(request, 'hymn_display.html', {'hymn_number':hymn_number, 'hymn_data': hymn_data, 'data':data, 'music_key': music_key, 'selected_voice_part': selected_voice_part, 'hymn_numbers': hymn_numbers})
        else:
            return render(request, 'hymn_display.html', {'error_message': 'Hymn not found.', 'hymn_numbers': hymn_numbers})
    else:
        return render(request, 'hymn_display.html', {'error_message': 'Please select or enter a hymn number.', 'hymn_numbers': hymn_numbers})


def fetch_hymn_from_file(hymn_number):
    file_path = "C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\mbh.txt"  # Adjust this path as per your file location
    with open(file_path, 'r') as f: 
        hymn_found = False
        hymn_lines = []
        current_stanza = []
        for line in f:
            stripped_line = line.strip()
            if stripped_line == f'HYMN {hymn_number}':
                hymn_found = True
                hymn_lines.append(f'HYMN {hymn_number}')
            elif hymn_found and stripped_line.startswith('HYMN'):
                break
            elif hymn_found:
                if stripped_line and stripped_line[0].isdigit() and stripped_line[1] == ' ':
                    if current_stanza:
                        hymn_lines.append(' '.join(current_stanza).strip())
                        current_stanza = [stripped_line]
                    else:
                        current_stanza.append(stripped_line)
                else:
                    current_stanza.append(stripped_line)
        if current_stanza:
            hymn_lines.append(' '.join(current_stanza).strip())
        
        if hymn_lines:
            formatted_hymn = '\n\n'.join([f'<p>{line}</p>' for line in hymn_lines])
            return formatted_hymn
        else:
            return None


def display_hymn_angg(request):
    def extract_html_file_names(directory):
        # List all files ending with .html
        html_files = [file for file in os.listdir(directory) if file.endswith('.html')]

        # Extract base names without extension
        base_names = [re.match(r'(.+?)\.html', file).group(1) for file in html_files]

        # Sort using a custom key
        def custom_sort_key(name):
            # Split into parts: numbers and non-numbers
            parts = re.split(r'(\d+)', name)
            # Convert numeric parts to integers for correct sorting
            parts = [int(part) if part.isdigit() else part for part in parts]
            return parts

        sorted_base_names = sorted(base_names, key=custom_sort_key)
        return sorted_base_names

    # Example usage:
    directory_path = "C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\lyrics_ang" # Replace with your directory path
    html_files_list = extract_html_file_names(directory_path)
    hymn_numbers = html_files_list  # Define the list of hymn numbers
    hymn_number = request.GET.get('hymn_number')
    
    if hymn_number:
        def generate_random_word():
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(4))

        random_word = generate_random_word()
        midi_file_path = f'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\media\\{random_word}.mid'
        # score.write('midi', fp=midi_file_path)
        request.session['random_word'] = random_word
        midi_messages = 1
        path = f"C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\anglican_tunes\\{hymn_number}.xml"
        score = music21.converter.parse(path)
        score.write('midi', fp=midi_file_path)
        hymn_data = fetch_hymn_from_file_ang(hymn_number)

#

#
        # Initialize a list to store notes and rests at each point in time
        notes_and_rests_by_time = []
        notes_and_rests_by_time_ = []

        # Get all the notes, chords, and rests from the score
        all_notes = score.flat.getElementsByClass(music21.note.GeneralNote)

        # Create a dictionary to group elements by their starting offset
        elements_by_offset = {}

        # Iterate through the notes, chords, and rests and group them by offset
        for element in all_notes:
            offset = element.offset
            if offset not in elements_by_offset:
                elements_by_offset[offset] = []
            elements_by_offset[offset].append(element)

        # Sort the offsets in ascending order
        sorted_offsets = sorted(elements_by_offset.keys())

        notss = []

        # Iterate through the sorted offsets and collect notes and rests at each point in time
        for offset in sorted_offsets:
            elements = elements_by_offset[offset]
            notes_and_rests = []
            nots=[]

            for element in elements:
                if isinstance(element, music21.note.Note):
                    pitch = element.pitch
                    parts = re.split(r'(\d+)', str(pitch))
                    modified_item = ''.join(parts)
                    pitch = modified_item
                    notes_and_rests.append(f"{pitch}") # {element.duration.quarterLength}
                    nots.append(f"{pitch} {element.duration.quarterLength}")

                elif isinstance(element, music21.chord.Chord):
                    for chord_note in element:
                        chord_pitch = chord_note.pitch
                        parts = re.split(r'(\d+)', str(chord_pitch))
                        modified_item = ''.join(parts)
                        chord_pitch = modified_item
                        notes_and_rests.append(f"{chord_pitch}") # {chord_note.duration.quarterLength}
                        nots.append(f"{chord_pitch} {chord_note.duration.quarterLength}")

                elif isinstance(element, music21.note.Rest):
                    pass
                    # notes_and_rests.append(f"Rest Duration: {element.duration.quarterLength}")

            notes_and_rests_by_time.append(notes_and_rests)
            notes_and_rests_by_time_.append(nots)
            notes = notes_and_rests_by_time_

            data = notes_and_rests_by_time_
            copy_notes = notes_and_rests_by_time_.copy()
            data = notes
            # Function to extract note and octave
            def get_note_octave(note):
                parts = note.split()
                note_part = parts[0][:-1]
                octave = int(parts[0][-1])
                return note_part, octave

            # Sort each sublist by octave and then by note alphabetically
            sorted_data = [
                sorted(sublist, key=lambda x: (get_note_octave(x)[1], get_note_octave(x)[0]), reverse=True)
                for sublist in data
            ]

            sorted_data
#
            data = sorted_data
            data = notes_and_rests_by_time_
            # Function to remove duplicates if sublist has more than 4 members
            def remove_excess_duplicates(data):
                new_data = []
                for sublist in data:
                    if len(sublist) > 4:
                        seen = set()
                        filtered = []
                        for item in sublist:
                            if item not in seen:
                                seen.add(item)
                                filtered.append(item)
                            elif len(filtered) < 4:
                                filtered.append(item)
                        new_data.append(filtered[:4])
                    else:
                        new_data.append(sublist)
                return new_data

            result = remove_excess_duplicates(data)
            notes_and_rests_by_time_ = result



        for sublist in notes:
            if len(sublist) < 4:
                # print("A sublist has fewer than 4 items:", sublist)
                # Create DataFrame
                df = pd.DataFrame(notes, columns=['Note1', 'Note2', 'Note3', 'Note4'])

                # Function to extract duration from note string
                def extract_duration(note):
                    if isinstance(note, str):
                        parts = note.split()
                        if len(parts) == 2 and parts[1].replace('.', '').isdigit():
                            return float(parts[1])
                    return 0.0

                # Add cumulative duration columns
                for col in df.columns:
                    df[col + '_Cumulative'] = df[col].apply(extract_duration).cumsum()

                # Display the updated DataFrame
                # print(df)
                # Get the index of the first sublist with less than 4 members
                index = next((i for i, sublist in enumerate(notes) if len(sublist) < 4), None)
                index = index -1
                # print("Index of the first sublist with less than 4 members:", index)
                # Function to check the next sublist after the given index
                def check_next_sublist_length(notes, index):
                    if index + 1 < len(notes):
                        next_sublist = notes[index + 1]
                        return len(next_sublist) < 4
                    return False

                # Check the next sublist
                has_less_than_4_items = check_next_sublist_length(notes, index)
                # print(f"The next sublist after index {index} has less than 4 items: {has_less_than_4_items}")
                # Retrieve the highest cumulative duration and corresponding column names
                def get_highest_cumulative_info(df, index):
                    if index >= 0:
                        # Get the cumulative duration values for the specified row
                        cumulative_values = df.iloc[index, df.columns.str.endswith('_Cumulative')]
                        # Find the maximum value
                        max_duration = cumulative_values.max()
                        # Get the column names with the maximum value
                        columns_with_max_duration = cumulative_values[cumulative_values == max_duration].index.tolist()
                        return max_duration, columns_with_max_duration
                    return None, []

                # Execute the function
                max_duration, columns_with_max_duration = get_highest_cumulative_info(df, index)

                # print(f"Highest cumulative duration at index {index}: {max_duration}")
                # print("Column names with this highest cumulative duration:", columns_with_max_duration)
                # Define the lists
                list1 = ['Note1_Cumulative', 'Note2_Cumulative', 'Note3_Cumulative', 'Note4_Cumulative']
                list2 = columns_with_max_duration

                # Retrieve members in list1 that are not in list2
                result = [item for item in list1 if item not in list2]

                print(result)  # Output: ['Note2_Cumulative']

                def replace_cumulative_notes(lst):
                    replacements = {
                        'Note1_Cumulative': 0,
                        'Note2_Cumulative': 1,
                        'Note3_Cumulative': 2,
                        'Note4_Cumulative': 3
                    }
                    
                    return [replacements.get(item, item) for item in lst]

                # Example usage
                input_list = ['Note1_Cumulative', 'Note2_Cumulative', 'Other', 'Note3_Cumulative', 'Note4_Cumulative']
                input_list = result
                output_list = replace_cumulative_notes(input_list)
                # print(output_list)
                original_list =notes[index + 1]
                desired_length = 4

                # Create a new list with '-' as placeholders
                modified_list = ['-'] * desired_length

                # Insert the original list elements at their respective indexes
                indices = output_list

                # Ensure the indices length matches the original_list length
                for i, item in enumerate(original_list):
                    if i < len(indices):
                        modified_list[indices[i]] = item

                # print(modified_list)

                # New value to replace notes[6]
                new_value = modified_list
                # Replace the element at index 6
                notes[index+1] = new_value
                
                # Print the updated list
                # print('kofi')
                # print(notes)
                aaa = notes.copy()
        def note_to_solfa(note, key):
            solfa_mappings = {
            'C major': {
                'C': 'd', 'D': 'r', 'E': 'm', 'F': 'f', 'G': 's',
                'A': 'l', 'B': 't', 'C#': 'di', 'D#': 'ri', 'F#': 'fi',
                'G#': 'si', 'A#': 'li'
            },
            'C# major': {
                'C#': 'd', 'D#': 'r', 'E#': 'm', 'F#': 'f', 'G#': 's',
                'A#': 'l', 'B#': 't', 'D': 'ra', 'F': 'fa', 'A': 'la'
            },
            'B minor': {
                'B': 'd', 'C#': 'r', 'D': 'm', 'E': 'f', 'F#': 's',
                'G': 'l', 'A': 't', 'E#': 'fi', 'A#': 'ti', 'C': 'ma'
            },
            'A minor': {
                'A': 'd', 'B': 'r', 'C': 'm', 'D': 'f', 'E': 's',
                'F': 'l', 'G': 't', 'C#': 'mi', 'D#': 'fi', 'G#': 'te'
            },
            'A major': {
                'A': 'd', 'B': 'r', 'C#': 'm', 'D': 'f', 'E': 's',
                'F#': 'l', 'G#': 't', 'D#': 'fi', 'G': 'le'
            },
            'D minor': {
                'D': 'd', 'E': 'r', 'F': 'm', 'G': 'f', 'A': 's',
                'B-': 'l', 'C': 't', 'E-': 'ri', 'A-': 'se'
            },
            'G minor': {
                'G': 'd', 'A': 'r', 'B-': 'm', 'C': 'f', 'D': 's',
                'E-': 'l', 'F': 't', 'A-': 'fi', 'D#': 'si'
            },
            'G major': {
                'G': 'd', 'A': 'r', 'B': 'm', 'C': 'f', 'D': 's',
                'E': 'l', 'F#': 't', 'F': 'fi', 'C#': 'fi'
            },
            'E- major': {
                'E-': 'd', 'F': 'r', 'G': 'm', 'A-': 'f', 'B-': 's',
                'C': 'l', 'D': 't', 'A': 'se', 'B': 'ma'
            },
            'C minor': {
                'C': 'd', 'D': 'r', 'E-': 'm', 'F': 'f', 'G': 's',
                'A-': 'l', 'B-': 't', 'E': 'mi', 'A': 'li'
            },
            'B- major': {
                'B-': 'd', 'C': 'r', 'D': 'm', 'E-': 'f', 'F': 's',
                'G': 'l', 'A': 't', 'D#': 'ra', 'F#': 'si'
            },
            'A- major': {
                'A-': 'd', 'B-': 'r', 'C': 'm', 'D-': 'f', 'E-': 's',
                'F': 'l', 'G': 't', 'D': 'ma', 'E': 'li'
            },
            'D major': {
                'D': 'd', 'E': 'r', 'F#': 'm', 'G': 'f', 'A': 's',
                'B': 'l', 'C#': 't', 'G#': 'ma', 'E#': 'ri'
            },
            'B- minor': {
                'B-': 'd', 'C': 'r', 'D-': 'm', 'E-': 'f', 'F': 's',
                'G-': 'l', 'A-': 't', 'E': 'mi', 'G': 'fi'
            },
            'F minor': {
                'F': 'd', 'G': 'r', 'A-': 'm', 'B-': 'f', 'C': 's',
                'D-': 'l', 'E-': 't', 'B': 'si', 'G-': 'fi'
            },
            'E minor': {
                'E': 'd', 'F#': 'r', 'G': 'm', 'A': 'f', 'B': 's',
                'C': 'l', 'D': 't', 'A#': 'li', 'G#': 'si'
            },
            'F major': {
                'F': 'd', 'G': 'r', 'A': 'm', 'B-': 'f', 'C': 's',
                'D': 'l', 'E': 't', 'C#': 'fi', 'G#': 'le'
            },
            'E major': {
                'E': 'd', 'F#': 'r', 'G#': 'm', 'A': 'f', 'B': 's',
                'C#': 'l', 'D#': 't', 'A#': 'li', 'B#': 'si'
            }
        }
            
            mapping = solfa_mappings[key]
            if note == '-':
                return '-'
            note_name, duration = note.split()
            note_name = note_name[:-1]  # Remove the octave number
            solfa = mapping.get(note_name, note_name)
            return f"{solfa} {duration}"

        notes_ = notes
        # Get the key signature
        key_signature = score.analyze('key')
#
        def capitalize_first_letter(s):
            if s and s[0].islower():
                return s[0].upper() + s[1:]
            return s

        # Example usage
        strin = str(key_signature)
        capitalized_string = capitalize_first_letter(strin)
        music_key = capitalized_string
#
        # print(f"The key of the piece is: {key_signature}")
        solfa_notes = [[note_to_solfa(note, key=capitalized_string) for note in chord] for chord in notes_]
        chords = []
        for chord in solfa_notes:
            chords.append(chord)
            # print(chord)
        notes = chords

        # Remove sublists with all members being '-'
        filtered_notes = [sublist for sublist in notes if sublist.count('-') < 4]

        filtered_notes
        new_data = filtered_notes.copy()
        data = [(index + 1, *row) for index, row in enumerate(new_data)]



    
        selected_voice_part = request.GET.get('voice_part')
        if selected_voice_part:
            if selected_voice_part == 'All':
                pass
            else:


                voice_map = {
                    'Soprano': 0,
                    'Alto': 1,
                    'Tenor': 2,
                    'Bass': 3
                }

                kogi = selected_voice_part
                voice_num = voice_map.get(kogi)

                # print(voice_num)  # Output will be 0

                # print('kpoooooooooo')
                # print(selected_voice_part)
                # Given music notes
                try:
                    music_notes = aaa
                except NameError:
                    music_notes = notes.copy()            # Create a stream
                melody = stream.Stream()

                # Extract and add the first note from each sublist
                for sublist in music_notes:
                    note_str = sublist[voice_num]  # First member of each sublist
                    if note_str == '-':
                        pass
                    else:

                        pitch, duration = note_str.split()  # Split into pitch and duration
                        duration = float(duration)  # Convert duration to float
                        # Create a note object and add it to the stream
                        n = note.Note(pitch)
                        n.quarterLength = duration
                        melody.append(n)

            # Show (and play) the stream
            # melody.show('midi')

            def generate_random_word():
                letters = string.ascii_lowercase
                return ''.join(random.choice(letters) for _ in range(4))

            random_word = generate_random_word()
            midi_file_path = f'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\media\\{random_word}.mid'
            # score.write('midi', fp=midi_file_path)
            request.session['random_word'] = random_word
            midi_messages = 1
            path = f"C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\anglican_tuness\\{hymn_number}.xml"
            # score = music21.converter.parse(path)
            melody.write('midi', fp=midi_file_path)
            # hymn_data = fetch_hymn_from_file_ang(hymn_number)

#         
        if hymn_data:
            hymn_data = re.sub(r'(?<!HYMN\s)(\d+)(?=\s)', r'<br><br> \1', hymn_data)
            aa = type(hymn_data)
            # lol
            print (hymn_number)
            return render(request, 'hymn_display_ang.html', {'hymn_number':hymn_number,'hymn_data': hymn_data, 'selected_voice_part': selected_voice_part,'music_key': music_key,'data':data,  'hymn_numbers': hymn_numbers})
        else:
            return render(request, 'hymn_display_ang.html', {'error_message': 'Hymn not found.', 'hymn_numbers': hymn_numbers})
    else:
        return render(request, 'hymn_display_ang.html', {'error_message': 'Please select or enter a hymn number.', 'hymn_numbers': hymn_numbers})


def fetch_hymn_from_file_ang(hymn_number):
    file_path = "C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\ang.txt"  # Adjust this path as per your file location
    with open(file_path, 'r') as f:
        hymn_found = False
        hymn_lines = []
        current_stanza = []
        for line in f:
            stripped_line = line.strip()
            if stripped_line == f'HYMN {hymn_number}':
                hymn_found = True
                hymn_lines.append(f'HYMN {hymn_number}')
            elif hymn_found and stripped_line.startswith('HYMN'):
                break
            elif hymn_found:
                if stripped_line and stripped_line[0].isdigit() and stripped_line[1] == ' ':
                    if current_stanza:
                        hymn_lines.append(' '.join(current_stanza).strip())
                        current_stanza = [stripped_line]
                    else:
                        current_stanza.append(stripped_line)
                else:
                    current_stanza.append(stripped_line)
        if current_stanza:
            hymn_lines.append(' '.join(current_stanza).strip())
        
        if hymn_lines:
            formatted_hymn = '\n\n'.join([f'<p>{line}</p>' for line in hymn_lines])
            return formatted_hymn
        else:
            return None


def display_hymn_presby(request):
    def extract_html_file_names(directory):
        # List all files ending with .html
        html_files = [file for file in os.listdir(directory) if file.endswith('.html')]

        # Extract base names without extension
        base_names = [re.match(r'(.+?)\.html', file).group(1) for file in html_files]

        # Sort using a custom key
        def custom_sort_key(name):
            # Split into parts: numbers and non-numbers
            parts = re.split(r'(\d+)', name)
            # Convert numeric parts to integers for correct sorting
            parts = [int(part) if part.isdigit() else part for part in parts]
            return parts

        sorted_base_names = sorted(base_names, key=custom_sort_key)
        return sorted_base_names

    # Example usage:
    directory_path = 'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\lyrics_presby' # Replace with your directory path
    html_files_list = extract_html_file_names(directory_path)
    hymn_numbers = html_files_list  # Define the list of hymn numbers
    hymn_number = request.GET.get('hymn_number')
    
    if hymn_number:
        def generate_random_word():
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(4))

        random_word = generate_random_word()
        midi_file_path = f'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\media\\{random_word}.mid'
        # score.write('midi', fp=midi_file_path)
        request.session['random_word'] = random_word
        midi_messages = 1
        # path = f"C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\tunes_presby\\{hymn_number}.xml"
        # score = music21.converter.parse(path)
        # score.write('midi', fp=midi_file_path)
        hymn_data = fetch_hymn_from_file_presby(hymn_number)
        if hymn_data:
            hymn_data = re.sub(r'(?<!HYMN\s)(\d+)(?=\s)', r'<br><br> \1', hymn_data)
            aa = type(hymn_data)
            # lol
            return render(request, 'hymn_display_presby.html', {'hymn_data': hymn_data, 'hymn_numbers': hymn_numbers})
        else:
            return render(request, 'hymn_display_presby.html', {'error_message': 'Hymn not found.', 'hymn_numbers': hymn_numbers})
    else:
        return render(request, 'hymn_display_presby.html', {'error_message': 'Please select or enter a hymn number.', 'hymn_numbers': hymn_numbers})

# def fetch_hymn_from_file_presby(hymn_number):
#     file_path = "C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\presby.txt"  # Adjust this path as per your file location
#     with open(file_path, 'r') as f:
#         hymn_found = False
#         hymn_lines = []
#         current_stanza = []
#         for line in f:
#             stripped_line = line.strip()
#             if stripped_line == f'HYMN {hymn_number}':
#                 hymn_found = True
#                 hymn_lines.append(f'HYMN {hymn_number}')
#             elif hymn_found and stripped_line.startswith('HYMN'):
#                 break
#             elif hymn_found:
#                 if stripped_line and stripped_line[0].isdigit() and stripped_line[1] == ' ':
#                     if current_stanza:
#                         hymn_lines.append(' '.join(current_stanza).strip())
#                         current_stanza = [stripped_line]
#                     else:
#                         current_stanza.append(stripped_line)
#                 else:
#                     current_stanza.append(stripped_line)
#         if current_stanza:
#             hymn_lines.append(' '.join(current_stanza).strip())
        
#         if hymn_lines:
#             formatted_hymn = '\n\n'.join([f'<p>{line}</p>' for line in hymn_lines])
#             return formatted_hymn
#         else:
#             return None

def fetch_hymn_from_file_presby(hymn_number):
    file_path = "C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\presby.txt"  # Adjust this path as per your file location
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            hymn_found = False
            hymn_lines = []
            current_stanza = []
            for line in f:
                stripped_line = line.strip()
                if stripped_line == f'HYMN {hymn_number}':
                    hymn_found = True
                    hymn_lines.append(f'HYMN {hymn_number}')
                elif hymn_found and stripped_line.startswith('HYMN'):
                    break
                elif hymn_found:
                    if stripped_line and stripped_line[0].isdigit() and stripped_line[1] == ' ':
                        if current_stanza:
                            hymn_lines.append(' '.join(current_stanza).strip())
                            current_stanza = [stripped_line]
                        else:
                            current_stanza.append(stripped_line)
                    else:
                        current_stanza.append(stripped_line)
            if current_stanza:
                hymn_lines.append(' '.join(current_stanza).strip())
            
            if hymn_lines:
                formatted_hymn = '\n\n'.join([f'<p>{line}</p>' for line in hymn_lines])
                return formatted_hymn
            else:
                return None
    except UnicodeDecodeError as e:
        print(f"Error reading the file: {e}")
        return None


# def fetch_hymn_from_file_presby(hymn_number):
#     file_path = "C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\presby.txt"  # Adjust this path as per your file location
#     with open(file_path, 'r') as f:
#         hymn_found = False
#         hymn_lines = []
#         current_stanza = []
#         for line in f:
#             stripped_line = line.strip()
#             if stripped_line == f'HYMN {hymn_number}':
#                 hymn_found = True
#                 hymn_lines.append(f'HYMN {hymn_number}')
#             elif hymn_found and stripped_line.startswith('HYMN'):
#                 break
#             elif hymn_found:
#                 if stripped_line and stripped_line[0].isdigit() and stripped_line[1] == ' ':
#                     if current_stanza:
#                         hymn_lines.append(' '.join(current_stanza).strip())
#                         current_stanza = [stripped_line]
#                     else:
#                         current_stanza.append(stripped_line)
#                 else:
#                     current_stanza.append(stripped_line)
#         if current_stanza:
#             hymn_lines.append(' '.join(current_stanza).strip())
        
#         if hymn_lines:
#             formatted_hymn = '\n\n'.join([f'<p>{line}</p>' for line in hymn_lines])
#             return formatted_hymn
#         else:
#             return None
def display_hymn_anthem_(request):
    selected_hymn = request.GET.get('varrick_armah')
    def extract_html_file_names(directory):
        # List all files ending with .html
        html_files = [file for file in os.listdir(directory) if file.endswith('.html')]

        # Extract base names without extension
        base_names = [re.match(r'(.+?)\.html', file).group(1) for file in html_files]

        # Sort using a custom key
        def custom_sort_key(name):
            # Split into parts: numbers and non-numbers
            parts = re.split(r'(\d+)', name)
            # Convert numeric parts to integers for correct sorting
            parts = [int(part) if part.isdigit() else part for part in parts]
            return parts

        sorted_base_names = sorted(base_names, key=custom_sort_key)
        return sorted_base_names

    # Example usage:
    directory_path = 'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\anthems_lyrics' # Replace with your directory path
    html_files_list = extract_html_file_names(directory_path)
    hymn_numbers = html_files_list  # Define the list of hymn numbers
    hymn_number = request.GET.get('hymn_number')


#
    if hymn_number:
        def generate_random_word():
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(4))

        random_word = generate_random_word()
        midi_file_path = f'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\media\\{random_word}.mid'
        # score.write('midi', fp=midi_file_path)
        request.session['random_word'] = random_word
        midi_messages = 1
        path = f"C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\tunes_anthems\\{hymn_number}.xml"
        score = music21.converter.parse(path)
        score.write('midi', fp=midi_file_path)
        hymn_data = fetch_hymn_from_file_anthem(hymn_number)
#


#
        if hymn_data:
            hymn_data = re.sub(r'(?<!HYMN\s)(\d+)(?=\s)', r'<br><br> \1', hymn_data)
            aa = type(hymn_data)
            # lol
            return render(request, 'varrick.html', {'hymn_data': hymn_data, 'hymn_numbers': hymn_numbers})
        else:
            return render(request, 'varrick.html', {'error_message': 'Hymn not found.', 'hymn_numbers': hymn_numbers})
    else:
        return render(request, 'varrick.html', {'error_message': 'Please select or type song title.', 'hymn_numbers': hymn_numbers})


def fetch_hymn_from_file_anthem_(hymn_number):
    file_path = "C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\armah.txt"  # Adjust this path as per your file location
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            hymn_found = False
            hymn_lines = []
            current_stanza = []
            for line in f:
                stripped_line = line.strip()
                # Check for the hymn number
                if stripped_line == hymn_number:
                    hymn_found = True
                    hymn_lines.append(hymn_number)
                elif hymn_found and stripped_line == '':
                    # Stop collecting lines if an empty line is encountered after finding the hymn
                    break
                elif hymn_found:
                    # Continue collecting lines for the current hymn
                    current_stanza.append(stripped_line)
            
            # Append the last stanza collected
            if current_stanza:
                hymn_lines.append(' '.join(current_stanza).strip())
            
            # Check if hymn lines were collected and format them
            if hymn_lines:
                formatted_hymn = '\n\n'.join([f'<p>{line}</p>' for line in hymn_lines])
                return formatted_hymn
            else:
                return None
    except UnicodeDecodeError as e:
        print(f"Error reading the file: {e}")
        return None


=======
>>>>>>> d64141e793585eba81673de8af9f37b259e7a589

def display_hymn_anthem(request):
    selected_composer = request.GET.get('composer')
    hymn_number = request.GET.get('hymn_number')
    hymn_numbers = []
    hymn_data = None
    error_message = None

    if selected_composer:
        hymn_numbers = extract_html_file_names('C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\anthems_lyrics')

    if hymn_number:
        random_word = generate_random_word()
        midi_file_path = f'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\media\\{random_word}.mid'
        request.session['random_word'] = random_word
        path = f"C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\tunes_anthems\\{hymn_number}.xml"
        score = music21.converter.parse(path)
        score.write('midi', fp=midi_file_path)
        hymn_data = fetch_hymn_from_file_anthem(hymn_number)
        if hymn_data:
            hymn_data = re.sub(r'(?<!HYMN\s)(\d+)(?=\s)', r'<br><br> \1', hymn_data)
        else:
            error_message = 'Hymn not found.'

    return render(request, 'varrick.html', {
        'hymn_data': hymn_data,
        'hymn_numbers': hymn_numbers,
        'selected_composer': selected_composer,
        'error_message': error_message,
        'hymn_number': hymn_number
    })

def extract_html_file_names(directory):
    html_files = [file for file in os.listdir(directory) if file.endswith('.html')]
    base_names = [re.match(r'(.+?)\.html', file).group(1) for file in html_files]

    def custom_sort_key(name):
        parts = re.split(r'(\d+)', name)
        parts = [int(part) if part.isdigit() else part for part in parts]
        return parts

    sorted_base_names = sorted(base_names, key=custom_sort_key)
    return sorted_base_names

def generate_random_word():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(4))

def fetch_hymn_from_file_anthem(hymn_number):
    file_path = "C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\armah.txt"
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            hymn_found = False
            hymn_lines = []
            current_stanza = []
            for line in f:
                stripped_line = line.strip()
                if stripped_line == hymn_number:
                    hymn_found = True
                    hymn_lines.append(hymn_number)
                elif hymn_found and stripped_line == '':
                    break
                elif hymn_found:
                    current_stanza.append(stripped_line)
            
            if current_stanza:
                hymn_lines.append(' '.join(current_stanza).strip())
            
            if hymn_lines:
                formatted_hymn = '\n\n'.join([f'<p>{line}</p>' for line in hymn_lines])
                return formatted_hymn
            else:
                return None
    except UnicodeDecodeError as e:
        print(f"Error reading the file: {e}")
        return None


# Example usage (you can comment this out or adjust as needed)
# result = fetch_hymn_from_file_presby(101)
# if result:
#     print(result)
# else:
#     print("Hymn not found or could not read the file.")




<<<<<<< HEAD
@csrf_exempt  # Only for demonstration purposes, not recommended for production
def handle_click_(request):
=======

def base(request):
    return render(request, 'lyrics/2.html')



@csrf_exempt  # Only for demonstration purposes, not recommended for production
def handle_click_presby(request):
    try:
        lists = list(range(1, 1001))
        directory = r"/home/kofi532/asedachorale/adom/templates/lyrics_presby"
        kpo = []

        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    kpo.append(entry.name)
        file_list = kpo

        # Remove '.html' from each element in the list
        file_list = [file_name.replace('.html', '') for file_name in file_list]
        def rearrange_list(input_list):
            def extract_integer(s):
                # Extracts the integer part from the string
                num = ''
                for char in s:
                    if char.isdigit():
                        num += char
                    else:
                        break
                return int(num) if num else None

            # Custom sorting function based on extracted integers
            def sort_key(elem):
                return extract_integer(elem)

            # Sort the list based on extracted integers
            sorted_list = sorted(input_list, key=sort_key)
            return sorted_list

        # Example list
        original_list = file_list

        # Rearrange the list
        rearranged_list = rearrange_list(original_list)
        lists = rearranged_list
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    kpo.append(entry.name)

        value_to_retrieve = request.GET.get('value_to_pass', None)
        print('hard')
        print(value_to_retrieve)
        if value_to_retrieve is not None:
            clicked_value = value_to_retrieve
            request.session['clicked_value'] = clicked_value
            # return JsonResponse({'status': 'success'})
            def generate_random_word():
                letters = string.ascii_lowercase
                return ''.join(random.choice(letters) for _ in range(4))

            random_word = generate_random_word()
            midi_file_path = f'/home/kofi532/asedachorale/aseda/media/{random_word}.mid'
            # score.write('midi', fp=midi_file_path)
            request.session['random_word'] = random_word
            midi_messages = 1
            path = f"/home/kofi532/asedachorale/adom/templates/tunes_ang/{clicked_value}.xml"
            score = music21.converter.parse(path)
            score.write('midi', fp=midi_file_path)

            return render(request, '/home/kofi532/asedachorale/lyrics_presby/'+str(clicked_value)+'.html', {'lists': lists, 'clicked_value':clicked_value})

        if request.method == 'POST':
            clicked_value = request.POST.get('num')
            request.session['clicked_value'] = clicked_value
            print(clicked_value)  # For demonstration, you can use this value as needed


            # return JsonResponse({'status': 'success'})
            def generate_random_word():
                letters = string.ascii_lowercase
                return ''.join(random.choice(letters) for _ in range(4))

            random_word = generate_random_word()
            midi_file_path = f'/home/kofi532/asedachorale/aseda/media/{random_word}.mid'
            # score.write('midi', fp=midi_file_path)
            request.session['random_word'] = random_word
            midi_messages = 1
            # try:
            path = f"/home/kofi532/asedachorale/adom/templates/tunes_ang/{clicked_value}.xml"

            score = music21.converter.parse(path)
            score.write('midi', fp=midi_file_path)

            # except:
            #     return render(request, 'sorry.html', {'lists': lists})
            return render(request, '/home/kofi532/asedachorale/lyrics_presby/'+str(clicked_value)+'.html', {'lists': lists, 'clicked_value':clicked_value, 'midi_messages':midi_messages})
            # return render(request, 'lyricshtml', {'lists': lists})
            # return redirect('landing_page', value_one=first_value)
        return render(request, '/home/kofi532/asedachorale/base_presby.html', {'lists': lists})
    except:
        return render(request, 'sorry.html', {})
    # return redirect('landing_page') + f'?value_one={first_value}'



@csrf_exempt  # Only for demonstration purposes, not recommended for production
def handle_click_ang(request):
>>>>>>> d64141e793585eba81673de8af9f37b259e7a589
    lists = list(range(1, 1001))
    directory = r"/home/kofi532/asedachorale/adom/templates/lyrics_ang"
    kpo = []

    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                kpo.append(entry.name)
    file_list = kpo

    # Remove '.html' from each element in the list
    file_list = [file_name.replace('.html', '') for file_name in file_list]
    def rearrange_list(input_list):
        def extract_integer(s):
            # Extracts the integer part from the string
            num = ''
            for char in s:
                if char.isdigit():
                    num += char
                else:
                    break
            return int(num) if num else None

        # Custom sorting function based on extracted integers
        def sort_key(elem):
            return extract_integer(elem)

        # Sort the list based on extracted integers
        sorted_list = sorted(input_list, key=sort_key)
        return sorted_list

    # Example list
    original_list = file_list

    # Rearrange the list
    rearranged_list = rearrange_list(original_list)
    lists = rearranged_list
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                kpo.append(entry.name)

    value_to_retrieve = request.GET.get('value_to_pass', None)
    print('hard')
    print(value_to_retrieve)
    if value_to_retrieve is not None:
        clicked_value = value_to_retrieve
        request.session['clicked_value'] = clicked_value
        # return JsonResponse({'status': 'success'})
        def generate_random_word():
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(4))

        random_word = generate_random_word()
<<<<<<< HEAD
        midi_file_path = f'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\media\\{random_word}.mid'
        # score.write('midi', fp=midi_file_path)
        request.session['random_word'] = random_word
        midi_messages = 1
        path = f"C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\tunes\\{clicked_value}.xml"
        score = music21.converter.parse(path)
        score.write('midi', fp=midi_file_path)
        return render(request, 'lyrics/'+str(clicked_value)+'.html', {'lists': lists, 'clicked_value':clicked_value})
=======
        midi_file_path = f'/home/kofi532/asedachorale/media/{random_word}.mid'
        # score.write('midi', fp=midi_file_path)
        request.session['random_word'] = random_word
        midi_messages = 1
        path = f"/home/kofi532/asedachorale/adom/templates/tunes_ang/{clicked_value}.xml"
        score = music21.converter.parse(path)
        score.write('midi', fp=midi_file_path)
        return render(request, 'lyrics_ang/'+str(clicked_value)+'.html', {'lists': lists, 'clicked_value':clicked_value})
>>>>>>> d64141e793585eba81673de8af9f37b259e7a589

    if request.method == 'POST':
        clicked_value = request.POST.get('num')
        request.session['clicked_value'] = clicked_value
        print(clicked_value)  # For demonstration, you can use this value as needed


        # return JsonResponse({'status': 'success'})
        def generate_random_word():
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(4))
<<<<<<< HEAD
=======

        random_word = generate_random_word()
        midi_file_path = f'/home/kofi532/asedachorale/media/{random_word}.mid'
        # score.write('midi', fp=midi_file_path)
        request.session['random_word'] = random_word
        midi_messages = 1
        # try:
        path = f"/home/kofi532/asedachorale/adom/templates/tunes_ang/{clicked_value}.xml"

        score = music21.converter.parse(path)
        score.write('midi', fp=midi_file_path)
        # except:
        #     return render(request, 'sorry.html', {'lists': lists})
        return render(request, 'lyrics_ang/'+str(clicked_value)+'.html', {'lists': lists, 'clicked_value':clicked_value, 'midi_messages':midi_messages})
        try:
            path = f"/adom/templates/tunes/{clicked_value}.xml"

            score = music21.converter.parse(path)
            score.write('midi', fp=midi_file_path)
        except:
            return render(request, 'sorry.html', {'lists': lists})
        path = f"/adom/templates/tunes/{clicked_value}.xml"
        score = music21.converter.parse(path)
        score.write('midi', fp=midi_file_path)
>>>>>>> d64141e793585eba81673de8af9f37b259e7a589

        random_word = generate_random_word()
        midi_file_path = f'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\media\\{random_word}.mid'
        # score.write('midi', fp=midi_file_path)
        request.session['random_word'] = random_word
        midi_messages = 1 
        try:
            # path = f"C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\tunes\\{clicked_value}.xml"
            
            score = music21.converter.parse(path)
            score.write('midi', fp=midi_file_path)
        except:
            return render(request, 'sorry.html', {'lists': lists})
        return render(request, 'lyrics/'+str(clicked_value)+'.html', {'lists': lists, 'clicked_value':clicked_value, 'midi_messages':midi_messages})
        # return render(request, 'lyricshtml', {'lists': lists})
        # return redirect('landing_page', value_one=first_value)
    return render(request, 'base_ang.html', {'lists': lists})

    # return redirect('landing_page') + f'?value_one={first_value}'

<<<<<<< HEAD
def search_hymn_presby (request):
    if request.method == 'POST':
        text_input_value = request.POST.get('text_input', '')
        # Process the text_input_value as needed
        print(text_input_value)
        

        directory_path = r"adom\templates\lyrics_presby"

        # Initialize an empty list to store file names
        kpo = []

        # Check if the directory exists
        if os.path.exists(directory_path) and os.path.isdir(directory_path):
            # Iterate through the files in the directory
            for filename in os.listdir(directory_path):
                # Append the file name to the 'kpo' list
                kpo.append(filename)

        carry = kpo.copy()
        # List all files in the directory
        file_list = os.listdir(directory_path)
        hymn_list = []
        # Loop through each file
        for file_name in file_list:
            # Check if the file is an HTML file
            if file_name.endswith(".html"):
                file_path = os.path.join(directory_path, file_name)
                with open(file_path, 'r', encoding='utf-8') as file:
                    # Read all lines into a list
                    lines = file.readlines()


                    # Print the content of line 6 (index 5 since Python uses zero-based indexing)
                    # if len(lines) >= 6:
                    if len(lines) >= 1:
                        with open(file_path, 'r', encoding='utf-8') as file:
                            html_content = file.read()
                            html_content = html_content[125:]
                            # print(html_content)
                        # print(lines[5])
                            # Remove '<br>', '<p>', and '</p>' from the string
                            cleaned_string = html_content.replace('<br/>', '').replace('<p>', '').replace('</p>', '').replace('<br>', '')
                            hymn_list.append(cleaned_string)

                        # print(cleaned_string)
                    else:
                        hymn_list.append(None)
                        # print("The file does not have at least 6 lines.")
        cut_hymn = []
        for item in hymn_list:
            # Split the string into words
            if item == None:
                cut_hymn.append(None)
            if len(str(item)) < 10:
                cut_hymn.append(None)

            if len(str(item))> 10:
                words = item.split()
                
                first_10_words = ' '.join(words[:70])
                cut_hymn.append(first_10_words)
        b = cut_hymn

        target_string = text_input_value

        # Calculate fuzz ratios for all items in the list
        ratios = [fuzz.ratio(item, target_string) for item in b]

        # Find the top 5 indexes with the highest fuzz ratios
        top_5_indexes = sorted(range(len(ratios)), key=lambda i: ratios[i], reverse=True)[:10]
        result = [carry[i] for i in top_5_indexes]
        result = [filename.replace('.html', '') for filename in result]

        hymning = [cut_hymn[i] for i in top_5_indexes]
=======


@csrf_exempt  # Only for demonstration purposes, not recommended for production
def handle_click(request):
    try:
        lists = list(range(1, 1001))
        directory = r"/home/kofi532/asedachorale/adom/templates/lyrics"
        kpo = []
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    kpo.append(entry.name)
        file_list = kpo

        # Remove '.html' from each element in the list
        file_list = [file_name.replace('.html', '') for file_name in file_list]
        def rearrange_list(input_list):
            def extract_integer(s):
                # Extracts the integer part from the string
                num = ''
                for char in s:
                    if char.isdigit():
                        num += char
                    else:
                        break
                return int(num) if num else None

            # Custom sorting function based on extracted integers
            def sort_key(elem):
                return extract_integer(elem)

            # Sort the list based on extracted integers
            sorted_list = sorted(input_list, key=sort_key)
            return sorted_list

        # Example list
        original_list = file_list

        # Rearrange the list
        rearranged_list = rearrange_list(original_list)
        lists = rearranged_list
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    kpo.append(entry.name)

        value_to_retrieve = request.GET.get('value_to_pass', None)

        if value_to_retrieve is not None:
            clicked_value = value_to_retrieve
            request.session['clicked_value'] = clicked_value
            def generate_random_word():
                letters = string.ascii_lowercase
                return ''.join(random.choice(letters) for _ in range(4))

            random_word = generate_random_word()
            midi_file_path = f'/home/kofi532/asedachorale/media/{random_word}.mid'
            # score.write('midi', fp=midi_file_path)
            request.session['random_word'] = random_word
            midi_messages = 1
            path = f"/home/kofi532/asedachorale/adom/templates/tunes/{clicked_value}.xml"
            score = music21.converter.parse(path)
            score.write('midi', fp=midi_file_path)
            return render(request, 'lyrics/'+str(clicked_value)+'.html', {'lists': lists, 'clicked_value':clicked_value})

        if request.method == 'POST':
            clicked_value = request.POST.get('num')
            request.session['clicked_value'] = clicked_value
            print(clicked_value)  # For demonstration, you can use this value as needed


            # return JsonResponse({'status': 'success'})
            # return JsonResponse({'status': 'success'})
            def generate_random_word():
                letters = string.ascii_lowercase
                return ''.join(random.choice(letters) for _ in range(4))

            random_word = generate_random_word()
            midi_file_path = f'/home/kofi532/asedachorale/media/{random_word}.mid'
            # score.write('midi', fp=midi_file_path)
            request.session['random_word'] = random_word
            midi_messages = 1
            path = f"/home/kofi532/asedachorale/adom/templates/tunes/{clicked_value}.xml"

            score = music21.converter.parse(path)
            score.write('midi', fp=midi_file_path)
            return render(request, 'lyrics/'+str(clicked_value)+'.html', {'lists': lists, 'clicked_value':clicked_value})
            # return render(request, 'lyricshtml', {'lists': lists})
            # return redirect('landing_page', value_one=first_value)
        return render(request, 'base.html', {'lists': lists})
    except:
        return render(request, 'sorry.html', {})
    # return redirect('landing_page') + f'?value_one={first_value}'


def search_hymn_presby (request):
    try:
        if request.method == 'POST':
            text_input_value = request.POST.get('text_input', '')
            # Process the text_input_value as needed
            print(text_input_value)


            directory_path = r"adom\templates\lyrics_presby"

            # Initialize an empty list to store file names
            kpo = []

            # Check if the directory exists
            if os.path.exists(directory_path) and os.path.isdir(directory_path):
                # Iterate through the files in the directory
                for filename in os.listdir(directory_path):
                    # Append the file name to the 'kpo' list
                    kpo.append(filename)

            carry = kpo.copy()
            # List all files in the directory
            file_list = os.listdir(directory_path)
            hymn_list = []
            # Loop through each file
            for file_name in file_list:
                # Check if the file is an HTML file
                if file_name.endswith(".html"):
                    file_path = os.path.join(directory_path, file_name)
                    with open(file_path, 'r', encoding='utf-8') as file:
                        # Read all lines into a list
                        lines = file.readlines()


                        # Print the content of line 6 (index 5 since Python uses zero-based indexing)
                        # if len(lines) >= 6:
                        if len(lines) >= 1:
                            with open(file_path, 'r', encoding='utf-8') as file:
                                html_content = file.read()
                                html_content = html_content[125:]
                                # print(html_content)
                            # print(lines[5])
                                # Remove '<br>', '<p>', and '</p>' from the string
                                cleaned_string = html_content.replace('<br/>', '').replace('<p>', '').replace('</p>', '').replace('<br>', '')
                                hymn_list.append(cleaned_string)

                            # print(cleaned_string)
                        else:
                            hymn_list.append(None)
                            # print("The file does not have at least 6 lines.")
            cut_hymn = []
            for item in hymn_list:
                # Split the string into words
                if item == None:
                    cut_hymn.append(None)
                if len(str(item)) < 10:
                    cut_hymn.append(None)

                if len(str(item))> 10:
                    words = item.split()

                    first_10_words = ' '.join(words[:70])
                    cut_hymn.append(first_10_words)
            b = cut_hymn

            target_string = text_input_value

            # Calculate fuzz ratios for all items in the list
            ratios = [fuzz.ratio(item, target_string) for item in b]

            # Find the top 5 indexes with the highest fuzz ratios
            top_5_indexes = sorted(range(len(ratios)), key=lambda i: ratios[i], reverse=True)[:10]
            result = [carry[i] for i in top_5_indexes]
            result = [filename.replace('.html', '') for filename in result]

            hymning = [cut_hymn[i] for i in top_5_indexes]
            mylist = zip(result, hymning)
            context = {
                'mylist': mylist,
            }
            return render(request, 'search_presby.html',context)
            # return HttpResponse(f'Text submitted: {result}')
        result = []
        hymning = []
>>>>>>> d64141e793585eba81673de8af9f37b259e7a589
        mylist = zip(result, hymning)
        context = {
            'mylist': mylist,
        }
        return render(request, 'search_presby.html',context)
<<<<<<< HEAD
        # return HttpResponse(f'Text submitted: {result}')
    result = []
    hymning = []
    mylist = zip(result, hymning)
    context = {
        'mylist': mylist,
    }
    return render(request, 'search_presby.html',context)

def search_hymn_ang (request):
    if request.method == 'POST':
        text_input_value = request.POST.get('text_input', '')
        # Process the text_input_value as needed
        print(text_input_value)
        

        directory_path = r"adom\templates\lyrics_ang"

        # Initialize an empty list to store file names
        kpo = []

        # Check if the directory exists
        if os.path.exists(directory_path) and os.path.isdir(directory_path):
            # Iterate through the files in the directory
            for filename in os.listdir(directory_path):
                # Append the file name to the 'kpo' list
                kpo.append(filename)

        carry = kpo.copy()
        # List all files in the directory
        file_list = os.listdir(directory_path)
        hymn_list = []
        # Loop through each file
        for file_name in file_list:
            # Check if the file is an HTML file
            if file_name.endswith(".html"):
                file_path = os.path.join(directory_path, file_name)
                with open(file_path, 'r', encoding='utf-8') as file:
                    # Read all lines into a list
                    lines = file.readlines()


                    # Print the content of line 6 (index 5 since Python uses zero-based indexing)
                    if len(lines) >= 6:

                        # print(lines[5])
                        # Remove '<br>', '<p>', and '</p>' from the string
                        cleaned_string = lines[5].replace('<br/>', '').replace('<p>', '').replace('</p>', '').replace('<br>', '')
                        hymn_list.append(cleaned_string)

                        # print(cleaned_string)
                    else:
                        hymn_list.append(None)
                        print("The file does not have at least 6 lines.")
        cut_hymn = []
        for item in hymn_list:
            # Split the string into words
            if item == None:
                cut_hymn.append(None)
            if len(str(item)) < 10:
                cut_hymn.append(None)

            if len(str(item))> 10:
                words = item.split()
                
                first_10_words = ' '.join(words[:20])
                cut_hymn.append(first_10_words)
        b = cut_hymn

        target_string = text_input_value

        # Calculate fuzz ratios for all items in the list
        ratios = [fuzz.ratio(item, target_string) for item in b]

        # Find the top 5 indexes with the highest fuzz ratios
        top_5_indexes = sorted(range(len(ratios)), key=lambda i: ratios[i], reverse=True)[:10]
        result = [carry[i] for i in top_5_indexes]
        result = [filename.replace('.html', '') for filename in result]

        hymning = [cut_hymn[i] for i in top_5_indexes]
        mylist = zip(result, hymning)
        context = {
            'mylist': mylist,
        }
        return render(request, 'search_ang.html',context)
        # return HttpResponse(f'Text submitted: {result}')
    result = []
    hymning = []
    mylist = zip(result, hymning)
    context = {
        'mylist': mylist,
    }
    return render(request, 'search_ang.html',context)



def search_hymn(request):
=======
    except:
        return render(request, 'sorry.html', {})

def search_hymn_ang (request):
>>>>>>> d64141e793585eba81673de8af9f37b259e7a589
    if request.method == 'POST':
        text_input_value = request.POST.get('text_input', '')
        # Process the text_input_value as needed
        print(text_input_value)


        directory_path = r"/home/kofi532/asedachorale/adom/templates/lyrics_ang"

        # Initialize an empty list to store file names
        kpo = []

        # Check if the directory exists
        if os.path.exists(directory_path) and os.path.isdir(directory_path):
            # Iterate through the files in the directory
            for filename in os.listdir(directory_path):
                # Append the file name to the 'kpo' list
                kpo.append(filename)

        carry = kpo.copy()
        # List all files in the directory
        file_list = os.listdir(directory_path)
        hymn_list = []
        # Loop through each file
        for file_name in file_list:
            # Check if the file is an HTML file
            if file_name.endswith(".html"):
                file_path = os.path.join(directory_path, file_name)
                with open(file_path, 'r', encoding='utf-8') as file:
                    # Read all lines into a list
                    lines = file.readlines()


                    # Print the content of line 6 (index 5 since Python uses zero-based indexing)
                    if len(lines) >= 6:

                        # print(lines[5])
                        # Remove '<br>', '<p>', and '</p>' from the string
                        cleaned_string = lines[5].replace('<br/>', '').replace('<p>', '').replace('</p>', '').replace('<br>', '')
                        hymn_list.append(cleaned_string)

                        # print(cleaned_string)
                    else:
                        hymn_list.append(None)
        cut_hymn = []
        for item in hymn_list:
            # Split the string into words
            if item == None:
                cut_hymn.append(None)
            if len(str(item)) < 10:
                cut_hymn.append(None)

            if len(str(item))> 10:
                words = item.split()

                first_10_words = ' '.join(words[:20])
                cut_hymn.append(first_10_words)
        b = cut_hymn

        target_string = text_input_value

        # Calculate fuzz ratios for all items in the list
        ratios = [fuzz.ratio(item, target_string) for item in b]

        # Find the top 5 indexes with the highest fuzz ratios
        top_5_indexes = sorted(range(len(ratios)), key=lambda i: ratios[i], reverse=True)[:10]
        result = [carry[i] for i in top_5_indexes]
        result = [filename.replace('.html', '') for filename in result]

        hymning = [cut_hymn[i] for i in top_5_indexes]
        mylist = zip(result, hymning)
        context = {
            'mylist': mylist,
        }
        return render(request, 'search_ang.html',context)
        # return HttpResponse(f'Text submitted: {result}')
    result = []
    hymning = []
    mylist = zip(result, hymning)
    context = {
        'mylist': mylist,
    }
    return render(request, 'search_ang.html',context)




def search_hymn(request):
    if request.method == 'POST':
        text_input_value = request.POST.get('text_input', '')
        # Process the text_input_value as needed
        print(text_input_value)


        directory_path = r"/home/kofi532/asedachorale/adom/templates/lyrics"

        # Initialize an empty list to store file names
        kpo = []

        # Check if the directory exists
        if os.path.exists(directory_path) and os.path.isdir(directory_path):
            # Iterate through the files in the directory
            for filename in os.listdir(directory_path):
                # Append the file name to the 'kpo' list
                kpo.append(filename)

        carry = kpo.copy()
        # List all files in the directory
        file_list = os.listdir(directory_path)
        hymn_list = []
        # Loop through each file
        for file_name in file_list:
            # Check if the file is an HTML file
            if file_name.endswith(".html"):
                file_path = os.path.join(directory_path, file_name)
                with open(file_path, 'r', encoding='utf-8') as file:
                    # Read all lines into a list
                    lines = file.readlines()


                    # Print the content of line 6 (index 5 since Python uses zero-based indexing)
                    if len(lines) >= 6:

                        # print(lines[5])
                        # Remove '<br>', '<p>', and '</p>' from the string
                        cleaned_string = lines[5].replace('<br/>', '').replace('<p>', '').replace('</p>', '').replace('<br>', '')
                        file_name = file_name.replace('.html', '')
                        hymn_list.append(file_name+' '+cleaned_string)

                        # print(cleaned_string)
                    else:
                        hymn_list.append(None)
                        print("The file does not have at least 6 lines.")
        cut_hymn = []
        for item in hymn_list:
            # Split the string into words
            if item == None:
                cut_hymn.append(None)
            if len(str(item)) < 10:
                cut_hymn.append(None)

            if len(str(item))> 10:
                words = item.split()

                first_10_words = ' '.join(words[:20])
                cut_hymn.append(first_10_words)
        b = cut_hymn

        target_string = text_input_value


        # Calculate fuzz ratios for all items in the list
        ratios = [fuzz.ratio(item, target_string) for item in b]

        # Find the top 5 indexes with the highest fuzz ratios
        top_5_indexes = sorted(range(len(ratios)), key=lambda i: ratios[i], reverse=True)[:10]


        hymning = [cut_hymn[i] for i in top_5_indexes]

        new_list = []

        for string in hymning:
            words = string.split()
            first_word = words[0]
            new_list.append(first_word)
        result = new_list.copy()
        mylist = zip(result, hymning)
        context = {
            'mylist': mylist,
        }
        return render(request, 'search.html',context)
        # return HttpResponse(f'Text submitted: {result}')
    result = []
    hymning = []
    mylist = zip(result, hymning)
    context = {
        'mylist': mylist,
    }
    return render(request, 'search.html',context)


def previous_view(request):

    first_value = "example_value"  # Replace this with your logic to get the actual value

    # Redirect to the landing page while passing the first value in the URL
    return redirect('music_view', value_one=first_value)




def one(request):
    onee= 'onee'
    return render(request, 'base.html', {'onee': onee})

def two(request):
    return render(request, 'index.html', {})




# views.py

<<<<<<< HEAD
def first(request):
    
    return render(request, 'first.html', {})

from django.conf import settings

def download_midi(request):
    random_word = request.session.get('random_word', None)

    midi_file_path = os.path.join(settings.MEDIA_ROOT, random_word+'.mid')
    response = FileResponse(open(midi_file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{random_word}.mid"'
    return response
=======
def music_view(request):

    clicked_value = request.session.get('clicked_value', None)
    print('Don')
    print(clicked_value)
    # path = f"/home/kofi532/asedachorale/adom/templates/tunes/{clicked_value}.xml"
    path = f"/home/kofi532/asedachorale/adom/templates/tunes/{clicked_value}.xml"

    score = music21.converter.parse(path)
    # C:\Users\KOFI ADUKPO\Downloads\solfa
    # score = music21.converter.parse(path)
    # Load a MusicXML file (replace 'your_music_score.xml' with the actual file path)
    # score = music21.converter.parse("C:\\Users\\KOFI ADUKPO\\Desktop\\code\\aseda\\adom\\templates\\848.xml")


    # Initialize a list to store notes and rests at each point in time
    notes_and_rests_by_time = []
    notes_and_rests_by_time_ = []


    # Get all the notes, chords, and rests from the score
    all_notes = score.flat.getElementsByClass(music21.note.GeneralNote)

    # Create a dictionary to group elements by their starting offset
    elements_by_offset = {}

    # Iterate through the notes, chords, and rests and group them by offset
    for element in all_notes:
        offset = element.offset
        if offset not in elements_by_offset:
            elements_by_offset[offset] = []
        elements_by_offset[offset].append(element)

    # Sort the offsets in ascending order
    sorted_offsets = sorted(elements_by_offset.keys())

    notss = []

    # Iterate through the sorted offsets and collect notes and rests at each point in time
    for offset in sorted_offsets:
        elements = elements_by_offset[offset]
        notes_and_rests = []
        nots=[]

        for element in elements:
            if isinstance(element, music21.note.Note):
                pitch = element.pitch
                parts = re.split(r'(\d+)', str(pitch))
                modified_item = ''.join(parts)
                pitch = modified_item
                notes_and_rests.append(f"{pitch}") # {element.duration.quarterLength}
                nots.append(f"{pitch} {element.duration.quarterLength}")


            elif isinstance(element, music21.chord.Chord):
                for chord_note in element:
                    chord_pitch = chord_note.pitch
                    parts = re.split(r'(\d+)', str(chord_pitch))
                    modified_item = ''.join(parts)
                    chord_pitch = modified_item
                    notes_and_rests.append(f"{chord_pitch}") # {chord_note.duration.quarterLength}
                    nots.append(f"{chord_pitch} {chord_note.duration.quarterLength}")

            elif isinstance(element, music21.note.Rest):
                pass
                # notes_and_rests.append(f"Rest Duration: {element.duration.quarterLength}")

        notes_and_rests_by_time.append(notes_and_rests)
        notes_and_rests_by_time_.append(nots)


    # # Print the notes and rests grouped by time
    # for i, notes_and_rests in enumerate(notes_and_rests_by_time):
    #     print(f"Time {i}: {', '.join(notes_and_rests)}")

    p = [['E-4 6.0'],['C4 1.0', 'E-4 6.0', 'A-2 1.0', 'A-3 3.0'], ['C4 1.0', 'C4 2.0', 'A-2 1.0', 'A-3 2.0'], ['E-4 1.0', 'C3 1.0']]
    p=notes_and_rests_by_time_
    t = []
    main = []
    data = p
    k=p

    ##taking care of the .75
    heavy=[]
    # Check if the decimal ends with .75
    for r in k:
        qw=[]
        qe=[]
        for u in r:
            pitch, duration = u.split()
            duration_float = float(duration)
            if duration_float % 1 == 0.75:
                # Subtract 0.25 from it
                new_duration = duration_float - 0.25
                qw.append(f"{pitch} {new_duration:.1f}")
                qe.append(f"{pitch} 0.25")
            else:
                qw.append(u)
        heavy.append(qw)
        if qe:
            heavy.append(qe)

    k=heavy

    # Create a new list to store the modified elements
    # Create a new list to store the modified elements
    new_k = []

    # Iterate through the sublists in 'k'
    for sublist_k in k:
        modified_sublist = []
        remaining_sublist = []
        for element in sublist_k:
            pitch, duration = element.split()  # Split the element into pitch and duration
            duration_float = float(duration)  # Convert duration to a float
            if duration_float > 1.0:
                if duration_float % 1 == 0.5:
                    # If duration ends with '.5', subtract 0.5 and add '.0' to the duration
                    modified_duration = f"{duration_float - 0.5:.1f}"
                    modified_sublist.append(f"{pitch} {modified_duration}")
                    remaining_sublist.append(f"{pitch} 0.5")  # Add a new element with '0.5' duration
                else:
                    # If duration is odd and greater than 1.0, subtract 1.0 and create a sublist for it
                    modified_duration = f"{duration_float - 1.0:.1f}"
                    modified_sublist.append(f"{pitch} {modified_duration}")
                    remaining_sublist.append(f"{pitch} 1.0")
            else:
                # Otherwise, keep the original element in the modified sublist
                modified_sublist.append(element)
        new_k.append(modified_sublist)
        if remaining_sublist:
            new_k.append(remaining_sublist)
    p=new_k

    for i in p:


        if i:

            # Calculate the minimum duration in the list
            # print(i)
            min_duration = min(float(note.split()[1]) for note in i)

            # Create a new list with equal durations
            equal_duration_list = [f"{note.split()[0]} {min_duration}" for note in i]
            t.append(equal_duration_list)

            # Create a remainder list with the original durations
            remainder = [f"{note.split()[0]} {float(note.split()[1]) - min_duration}" for note in i if float(note.split()[1]) > min_duration]
            if remainder:
                # Extract the second items from each element
                second_items = [float(note.split()[1]) for note in remainder]

                # Check if all second items are the same
                is_same_duration = all(item == second_items[0] for item in second_items)

                if is_same_duration:
                    t.append(remainder)
                else:
                    min_duration = min(float(note.split()[1]) for note in remainder) #leevel
                    # Create a new list with equal durations
                    equal_duration_list = [f"{note.split()[0]} {min_duration}" for note in remainder]
                    t.append(equal_duration_list)
                    # Create a remainder list with the original durations
                    remainder = [f"{note.split()[0]} {float(note.split()[1]) - min_duration}" for note in remainder if float(note.split()[1]) > min_duration]
                    # print(f'firstremain: {remainder}')
                    # Extract the second items from each element
                    if remainder:
                        second_items = [float(note.split()[1]) for note in remainder]


                        # Check if all second items are the same
                        is_same_duration = all(item == second_items[0] for item in second_items)

                        if is_same_duration:
                            t.append(remainder)
                        else:
                            min_duration = min(float(note.split()[1]) for note in remainder)
                            # Create a new list with equal durations
                            equal_duration_list = [f"{note.split()[0]} {min_duration}" for note in remainder]
                            t.append(equal_duration_list)
                            ##
                            remainder = [f"{note.split()[0]} {float(note.split()[1]) - min_duration}" for note in remainder if float(note.split()[1]) > min_duration]
                            # Extract the second items from each element
                            # print(f'remain: {remainder}')
                            if remainder:
                                second_items = [float(note.split()[1]) for note in remainder]

                                # Check if all second items are the same
                                is_same_duration = all(item == second_items[0] for item in second_items)

                                if is_same_duration:
                                    # print(remainder)
                                    t.append(remainder)

                                else:
                                    min_duration = min(float(note.split()[1]) for note in remainder)
                                    # Create a new list with equal durations
                                    equal_duration_list = [f"{note.split()[0]} {min_duration}" for note in remainder]
                                    t.append(equal_duration_list)
                                    remainder = [f"{note.split()[0]} {float(note.split()[1]) - min_duration}" for note in remainder if float(note.split()[1]) > min_duration]

                                    if remainder:
                                        second_items = [float(note.split()[1]) for note in remainder]

                                        # Check if all second items are the same
                                        is_same_duration = all(item == second_items[0] for item in second_items)

                                        if is_same_duration:
                                            t.append(remainder)
                                        else:
                                            min_duration = min(float(note.split()[1]) for note in remainder)
                                            # Create a new list with equal durations
                                            equal_duration_list = [f"{note.split()[0]} {min_duration}" for note in remainder]
                                            t.append(equal_duration_list)



        p = t
    new_p = []

    for f in p:
        pp=[]
        pl=[]
        for y in f:
            pitch, duration = y.split()
            duration_float = float(duration)

            if duration_float > 2.0 and duration_float % 2 == 1.0:
                # If duration is greater than or equal to 1.0 and odd, subtract 1.0 from it
                new_duration = duration_float - 1.0
                pp.append(f"{pitch} {new_duration:.1f}")
                pl.append(f"{pitch} 1.0")
            else:
                pp.append(y)
        new_p.append(pp)
        if pl:
            new_p.append(pl)



    t=new_p

    data = t

    # Find the highest value of the second item in each sublist
    max_values = [max(float(note.split()[1]) for note in sublist) for sublist in data]

    # Modify 'data' to contain the highest values as sublists
    durate = [[max_value] for max_value in max_values]
    timer = durate.copy()


    data = t

    # Remove the second items in each element in the sublists
    modified_data = [[note.split()[0] for note in sublist] for sublist in data]


    # Define the mapping of durations to names
    duration_names = {0.5: 'eighth',1.0: 'quarter',0.25: '16th', 2.0: 'half', 4.0: 'whole'}

    # Given list 'p'
    p = durate

    # Convert 'p' to their names
    durate = [[duration_names[d] for d in sublist] for sublist in p]

    data = t

    # Remove the second items in each element in the sublists
    modified_data = [[note.split()[0] for note in sublist] for sublist in data]

    # Define the chords as lists of note names
    chords = modified_data
    chords = [[i, *sublist] for i, sublist in enumerate(chords)]
    # Define the durations for each chord
    durations = durate
    # Create a stream to store the notes
    music_stream = stream.Stream()
    # music_stream.append(tempo.MetronomeMark(number=500))
    # Iterate through the chords and durations
    for i, chord_notes in enumerate(chords):
        if i < len(durations):
            chord_obj = chord.Chord(chord_notes)
            chord_obj.duration.type = (durations[i])[0]
            music_stream.append(chord_obj)
        else:
            pass
            # print(f"Warning: Not enough durations provided for chord {i + 1}. Skipping.")
    # total_duration = music_stream.duration.quarterLength
    # music_stream.show('midi')
    ##
    in_midi = []
    if request.method == 'POST':

        try:
            # action = data.get('action')
            action = request.POST.get('action')

            if action == None:
                music_stream.show('midi')
            data = json.loads(request.body.decode('utf-8'))
            values = data.get('values')

            if len(values) == 2:


                # Extract the selected values and their colors
                value1 = values[0]['value']
                color1 = values[0]['color']
                value2 = values[1]['value']
                color2 = values[1]['color']
                print(value1)
                print(value2)
                if value1 > value2:
                    chords = chords[value2:value1]
                    durations = durations[value2:value1]
                else:
                    chords = chords[value1:value2]
                    durations = durations[value1:value2]
                music_stream = stream.Stream()
                # music_stream.append(tempo.MetronomeMark(number=500))
                # Iterate through the chords and durations
                for i, chord_notes in enumerate(chords):
                    if i < len(durations):
                        chord_obj = chord.Chord(chord_notes)
                        chord_obj.duration.type = (durations[i])[0]
                        music_stream.append(chord_obj)
                    else:
                        pass
                music_stream.show('midi')


                # Handle the selected objects based on their colors
                if color1 == 'highlight-yellow':
                    pass
                    # Handle the first selected object with a yellow highlight
                    # Your logic here...

                if color2 == 'highlight-green':
                    pass
                    # Handle the second selected object with a green highlight
                    # Your logic here...
                # music_stream.stop()

            # For demonstration purposes, simply return the processed data
                return JsonResponse({'message': 'Data received and processed successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        # return render(request, 'home.html', {'timer':timer, 'chords':chords})
    else:
        return render(request, 'home.html', {'timer':timer, 'chords':chords})
        # return JsonResponse({'error': 'Invalid request method'}, status=405)




def music_view(request):
    value_to_retrieve = request.GET.get('value_to_pass', None)
    print('hard')
    print(value_to_retrieve)

    clicked_value = request.session.get('clicked_value', None)
    print('Don')
    print(clicked_value)
    path = f"/home/kofi532/asedachorale/adom/templates/tunes/{clicked_value}.xml"
    score = music21.converter.parse(path)
    # C:\Users\KOFI ADUKPO\Downloads\solfa
    # score = music21.converter.parse(path)
    # Load a MusicXML file (replace 'your_music_score.xml' with the actual file path)
    # score = music21.converter.parse("C:\\Users\\KOFI ADUKPO\\Desktop\\code\\aseda\\adom\\templates\\848.xml")


    # Initialize a list to store notes and rests at each point in time
    notes_and_rests_by_time = []
    notes_and_rests_by_time_ = []


    # Get all the notes, chords, and rests from the score
    all_notes = score.flat.getElementsByClass(music21.note.GeneralNote)

    # Create a dictionary to group elements by their starting offset
    elements_by_offset = {}

    # Iterate through the notes, chords, and rests and group them by offset
    for element in all_notes:
        offset = element.offset
        if offset not in elements_by_offset:
            elements_by_offset[offset] = []
        elements_by_offset[offset].append(element)

    # Sort the offsets in ascending order
    sorted_offsets = sorted(elements_by_offset.keys())

    notss = []

    # Iterate through the sorted offsets and collect notes and rests at each point in time
    for offset in sorted_offsets:
        elements = elements_by_offset[offset]
        notes_and_rests = []
        nots=[]

        for element in elements:
            if isinstance(element, music21.note.Note):
                pitch = element.pitch
                parts = re.split(r'(\d+)', str(pitch))
                modified_item = ''.join(parts)
                pitch = modified_item
                notes_and_rests.append(f"{pitch}") # {element.duration.quarterLength}
                nots.append(f"{pitch} {element.duration.quarterLength}")


            elif isinstance(element, music21.chord.Chord):
                for chord_note in element:
                    chord_pitch = chord_note.pitch
                    parts = re.split(r'(\d+)', str(chord_pitch))
                    modified_item = ''.join(parts)
                    chord_pitch = modified_item
                    notes_and_rests.append(f"{chord_pitch}") # {chord_note.duration.quarterLength}
                    nots.append(f"{chord_pitch} {chord_note.duration.quarterLength}")

            elif isinstance(element, music21.note.Rest):
                pass
                # notes_and_rests.append(f"Rest Duration: {element.duration.quarterLength}")

        notes_and_rests_by_time.append(notes_and_rests)
        notes_and_rests_by_time_.append(nots)


    # # Print the notes and rests grouped by time
    # for i, notes_and_rests in enumerate(notes_and_rests_by_time):
    #     print(f"Time {i}: {', '.join(notes_and_rests)}")

    modified_data = notes_and_rests_by_time_
    # Define the chords as lists of note names
    chords = modified_data

    chords = [[i, *sublist] for i, sublist in enumerate(chords)]
    # Define the durations for each chord
    # Create a stream to store the notes
    chrd = chords
>>>>>>> d64141e793585eba81673de8af9f37b259e7a589



from pydub import AudioSegment
import os


def download_midi_final(request):
    hymn_number = request.session.get('hymn_number', None)
    random_word = request.session.get('random_letters', None)
    
    request.session['random_word'] = random_word
  

    # Directory containing the audio files
    directory = r"C:\Users\Asamoah\Desktop\kofi\aseda_a\media\inn"

# "C:\Users\Asamoah\Desktop\kofi\aseda_a"

    target_code2 = random_word
    target_hymnnumber = hymn_number


    print('bbbbtt')
    print(target_code2)
    print(target_hymnnumber)
    # List to store matching file paths
    matching_files = []

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".mid"):
            # Split the filename into parts based on underscores
            parts = filename.split('_')
            
            # Check if the file matches the desired code2 and hymnnumber
            if len(parts) == 3 and parts[1] == target_code2 and parts[2].startswith(target_hymnnumber):
                # Add the full file path to the list
                matching_files.append(os.path.join(directory, filename))

    # Print the list of matching files
    print("Matching files:")
    for file in matching_files:
        print(file)

    people_num = len(matching_files)
    request.session['people_num'] = int(people_num)
    # List of file paths to the audio files you want to merge
    audio_files = matching_files



    # Load the first audio file
    combined = AudioSegment.from_file(audio_files[0])

    # Overlay (merge) the remaining audio files
    for file in audio_files[1:]:
        audio = AudioSegment.from_file(file)
        combined = combined.overlay(audio)

    # Specify the full path where you want to save the file
    output_path = f"C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\media\\inn\\final_{target_code2}_{target_hymnnumber}.mp3"
    combined.export(output_path, format="mp3")



    # Construct the filename with the new format
    # midi_filename = f'final_{random_word}_{hymn_number}.mid'
    midi_filename = f"final_{target_code2}_{target_hymnnumber}.mp3"

    print(midi_filename)
    # Construct the full path to the MIDI file in the 'inn' directory
    midi_file_path = os.path.join(settings.MEDIA_ROOT, 'inn', midi_filename)
    
    # Return the file response
    response = FileResponse(open(midi_file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{midi_filename}"'
    return response



def final_audio(request):
    hymn_numberr = request.session.get('hymn_number', None)
    random_wordd = request.session.get('random_letters', None)
    people_num = request.session.get('people_num', None)
    if people_num is not None:
        people_num = int(people_num)-1
    return render(request, 'final_audio.html', {'people_num':people_num, 'hymn_numberr':hymn_numberr, 'random_wordd':random_wordd})


def contact(request):
    return render(request, 'contact.html')

def privacy(request):
    return render(request, 'privacy.html')

def anthems(request):
    return render(request, 'search_anthems.html')

def armah(request):
    directory = r'C:\Users\KOFI ADUKPO\Desktop\code\aseda\adom\templates\anthems_lyrics'
    file_names = [filename[:-5] for filename in os.listdir(directory) if filename.endswith('.html')]
    if request.method == 'POST':
        clicked_value = request.POST.get('num')  # Extract the value of the clicked button
        # return JsonResponse({'status': 'success'})
        def generate_random_word():
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(4))

        random_word = generate_random_word()
        midi_file_path = f'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\media\\{random_word}.mid'
        # score.write('midi', fp=midi_file_path)
        request.session['random_word'] = random_word
        midi_messages = 1
        path = f"C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\tunes_anthems\\{clicked_value}.xml"
        score = music21.converter.parse(path)
        score.write('midi', fp=midi_file_path)
        # return render(request, 'lyrics/'+str(clicked_value)+'.html', {'lists': lists, 'clicked_value':clicked_value})
        clicked_value=clicked_value.upper()
        return render(request, 'anthems_lyrics/'+str(clicked_value)+'.html', {'clicked_value':clicked_value})

    return render(request, 'armah.html', {'file_names': file_names})


def armah_songs(request):
    # clicked_value = ''
    # request.session['clicked_value'] = clicked_value
    clicked_value = request.session.get('clicked_value', None)
    return render(request, 'anthems_lyrics/'+str(clicked_value)+'.html', {'clicked_value':clicked_value})


    
def display_pdf(request):
    pdf_path = "C:\\Users\\KOFI ADUKPO\\Downloads\\1557429_February_2024_payslip.pdf"  # Replace 'path_to_your_pdf.pdf' with the actual path to your PDF file
    if os.path.exists(pdf_path):
        with open(pdf_path, 'rb') as f:
            pdf_data = f.read()
            encoded_pdf = base64.b64encode(pdf_data).decode('utf-8')
        return render(request, 'music_player.html', {'encoded_pdf': encoded_pdf})
    else:
        return render(request, 'sorry.html')

# hymns/views.py

from django.shortcuts import render
from .forms import HymnSearchForm

HYMN_FILES = {
    'A & M': 'C:/Users/KOFI ADUKPO/Desktop/code/asedachorale_/adom/templates/ang.txt',
    'M.H.B': 'C:/Users/KOFI ADUKPO/Desktop/code/asedachorale_/adom/templates/mbh.txt',
    'P.H.B': 'C:/Users/KOFI ADUKPO/Desktop/code/asedachorale_/adom/templates/presby.txt',
}


def search_hymns(query):
    results = []
    query_lower = query.lower()
    
    for source, filepath in HYMN_FILES.items():
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            hymns = content.split('HYMN ')
            
            for hymn in hymns:
                if query_lower in hymn.lower():
                    hymn_number = 'HYMN ' + hymn.split('\n')[0].strip()
                    hymn_content = '\n'.join(hymn.split('\n')[1:]).strip()
                    results.append((source, hymn_number, hymn_content))
                    
    results = sorted(results, key=lambda x: x[1])[:5]
    return results

def hymn_search_view(request):
    form = HymnSearchForm()
    results = []
    if request.method == 'POST':
        form = HymnSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = search_hymns(query)
            for i, (source, hymn_number, hymn_content) in enumerate(results):
                hymn_number_cleaned = hymn_number.split()[1]
                if source == 'M.H.B':
                    results[i] = (source, hymn_number, hymn_content, f"/mhb/?hymn_number={hymn_number_cleaned}")
                elif source == 'P.H.B':
                    results[i] = (source, hymn_number, hymn_content, f"/presby/?hymn_number={hymn_number_cleaned}")
                elif source == 'A & M':
                    results[i] = (source, hymn_number, hymn_content, f"/anglican/?hymn_number={hymn_number_cleaned}")
    
    return render(request, 'search.html', {'form': form, 'results': results})

def hymn_detail_view(request, source, hymn_number):
    filepath = HYMN_FILES.get(source)
    print(hymn_number, source)
    hymn_content = ''
    if filepath:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            hymns = content.split('HYMN ')
            for hymn in hymns:
                if hymn.startswith(hymn_number):
                    hymn_content = '\n'.join(hymn.split('\n')[1:]).strip()
                    break
    
    return render(request, 'search.html', {'source': source, 'hymn_number': hymn_number, 'hymn_content': hymn_content})


def display_notes(request):
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
    return render(request, 'solfa.html', context)


from django.shortcuts import render

def music_notes_view(request):

    path = "C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\tunes\\271.xml"
    score = music21.converter.parse(path)

    # Initialize a list to store notes and rests at each point in time
    notes_and_rests_by_time = []
    notes_and_rests_by_time_ = []

    # Get all the notes, chords, and rests from the score
    all_notes = score.flat.getElementsByClass(music21.note.GeneralNote)

    # Create a dictionary to group elements by their starting offset
    elements_by_offset = {}

    # Iterate through the notes, chords, and rests and group them by offset
    for element in all_notes:
        offset = element.offset
        if offset not in elements_by_offset:
            elements_by_offset[offset] = []
        elements_by_offset[offset].append(element)

    # Sort the offsets in ascending order
    sorted_offsets = sorted(elements_by_offset.keys())

    notss = []

    # Iterate through the sorted offsets and collect notes and rests at each point in time
    for offset in sorted_offsets:
        elements = elements_by_offset[offset]
        notes_and_rests = []
        nots=[]

        for element in elements:
            if isinstance(element, music21.note.Note):
                pitch = element.pitch
                parts = re.split(r'(\d+)', str(pitch))
                modified_item = ''.join(parts)
                pitch = modified_item
                notes_and_rests.append(f"{pitch}") # {element.duration.quarterLength}
                nots.append(f"{pitch} {element.duration.quarterLength}")

            elif isinstance(element, music21.chord.Chord):
                for chord_note in element:
                    chord_pitch = chord_note.pitch
                    parts = re.split(r'(\d+)', str(chord_pitch))
                    modified_item = ''.join(parts)
                    chord_pitch = modified_item
                    notes_and_rests.append(f"{chord_pitch}") # {chord_note.duration.quarterLength}
                    nots.append(f"{chord_pitch} {chord_note.duration.quarterLength}")

            elif isinstance(element, music21.note.Rest):
                pass
                # notes_and_rests.append(f"Rest Duration: {element.duration.quarterLength}")

        notes_and_rests_by_time.append(notes_and_rests)
        notes_and_rests_by_time_.append(nots)
        notes = notes_and_rests_by_time_
    for sublist in notes:
        if len(sublist) < 4:
            print("A sublist has fewer than 4 items:", sublist)
            # Create DataFrame
            df = pd.DataFrame(notes, columns=['Note1', 'Note2', 'Note3', 'Note4'])

            # Function to extract duration from note string
            def extract_duration(note):
                if isinstance(note, str):
                    parts = note.split()
                    if len(parts) == 2 and parts[1].replace('.', '').isdigit():
                        return float(parts[1])
                return 0.0

            # Add cumulative duration columns
            for col in df.columns:
                df[col + '_Cumulative'] = df[col].apply(extract_duration).cumsum()

            # Display the updated DataFrame
            print(df)
            # Get the index of the first sublist with less than 4 members
            index = next((i for i, sublist in enumerate(notes) if len(sublist) < 4), None)
            index = index -1
            print("Index of the first sublist with less than 4 members:", index)
            # Function to check the next sublist after the given index
            def check_next_sublist_length(notes, index):
                if index + 1 < len(notes):
                    next_sublist = notes[index + 1]
                    return len(next_sublist) < 4
                return False

            # Check the next sublist
            has_less_than_4_items = check_next_sublist_length(notes, index)
            print(f"The next sublist after index {index} has less than 4 items: {has_less_than_4_items}")
            # Retrieve the highest cumulative duration and corresponding column names
            def get_highest_cumulative_info(df, index):
                if index >= 0:
                    # Get the cumulative duration values for the specified row
                    cumulative_values = df.iloc[index, df.columns.str.endswith('_Cumulative')]
                    # Find the maximum value
                    max_duration = cumulative_values.max()
                    # Get the column names with the maximum value
                    columns_with_max_duration = cumulative_values[cumulative_values == max_duration].index.tolist()
                    return max_duration, columns_with_max_duration
                return None, []

            # Execute the function
            max_duration, columns_with_max_duration = get_highest_cumulative_info(df, index)

            print(f"Highest cumulative duration at index {index}: {max_duration}")
            print("Column names with this highest cumulative duration:", columns_with_max_duration)
            # Define the lists
            list1 = ['Note1_Cumulative', 'Note2_Cumulative', 'Note3_Cumulative', 'Note4_Cumulative']
            list2 = columns_with_max_duration

            # Retrieve members in list1 that are not in list2
            result = [item for item in list1 if item not in list2]

            print(result)  # Output: ['Note2_Cumulative']

            def replace_cumulative_notes(lst):
                replacements = {
                    'Note1_Cumulative': 0,
                    'Note2_Cumulative': 1,
                    'Note3_Cumulative': 2,
                    'Note4_Cumulative': 3
                }
                
                return [replacements.get(item, item) for item in lst]

            # Example usage
            input_list = ['Note1_Cumulative', 'Note2_Cumulative', 'Other', 'Note3_Cumulative', 'Note4_Cumulative']
            input_list = result
            output_list = replace_cumulative_notes(input_list)
            print(output_list)
            original_list =notes[index + 1]
            desired_length = 4

            # Create a new list with '-' as placeholders
            modified_list = ['-'] * desired_length

            # Insert the original list elements at their respective indexes
            indices = output_list

            # Ensure the indices length matches the original_list length
            for i, item in enumerate(original_list):
                if i < len(indices):
                    modified_list[indices[i]] = item

            print(modified_list)

            # New value to replace notes[6]
            new_value = modified_list
            # Replace the element at index 6
            notes[index+1] = new_value
            
            # Print the updated list
            print('kofi')
            print(notes)
            aaa = notes.copy()
    def note_to_solfa(note, key):
        solfa_mappings = {
            'G major': {
                'F': 'r', 'B-': 's', 'D': 'ta', 'G': 'm', 'E-': 'd',
                'C': 'l', 'A': 'f', 'F#': 'r', 'B': 's', 'D#': 't',
                'C#': 'l', 'E': 'd', 'G#': 'm', 'A#': 'fe', 'A-': 'f'
            },
            'E- major': {
                'F': 'r', 'B-': 's', 'D': 'ta', 'G': 'm', 'E-': 'd',
                'C': 'l', 'A': 'f', 'F#': 'r', 'B': 's', 'D#': 't',
                'C#': 'l', 'E': 'd', 'G#': 'm','A#': 'fe', 'A-': 'f'
            }
        }
        
        mapping = solfa_mappings[key]
        if note == '-':
            return '-'
        note_name, duration = note.split()
        note_name = note_name[:-1]  # Remove the octave number
        solfa = mapping.get(note_name, note_name)
        return f"{solfa} {duration}"

    notes_ = notes

    solfa_notes = [[note_to_solfa(note, key='E- major') for note in chord] for chord in notes_]
    chords = []
    for chord in solfa_notes:
        chords.append(chord)
        print(chord)


                        # def note_to_solfa(note):
            #     solfa_mapping = {
            #         'F': 'r', 'B-': 's', 'D': 'ta', 'G': 'm', 'E-': 'd', 
            #         'C': 'l', 'A': 'f', 'F#': 'r', 'B': 's', 'D#': 't',
            #         'C#': 'l', 'E': 'd', 'G#': 'm','A#': 'fe', 'A-': 'f'
            #     }
            #     note_name, duration = note.split()
            #     note_name = note_name[:-1]  # Remove the octave number
            #     solfa = solfa_mapping.get(note_name, note_name)
            #     return f"{solfa} {duration}"

            # notes_ = notes

            # solfa_notes = [[note_to_solfa(note) for note in chord if note != '-'] for chord in notes_]
            # chords = []
            # for chord in solfa_notes:
            #     chords.append(chord)
            # notes = chords
    return render(request, 'jot_.html', {'data': chords})


from django.shortcuts import render, redirect
from .models import AudioRecording

def upload_audioo(request):
    if request.method == 'POST':
        audio_data = request.POST.get('audio_data')
        username = request.user.username  # Get the logged-in username

        # Save the audio recording with the username
        AudioRecording.objects.create(audio_data=audio_data, username=username)
        return redirect('display_hymn')  # Replace with your success URL

    return render(request, 'hymn_display.html')


import base64
import os
from django.conf import settings
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime



@csrf_exempt
def upload_audioo(request):
    if request.method == 'POST':

        # Get the current date and time
        current_datetime = datetime.now()

<<<<<<< HEAD
        # Format the date and time as a string
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        formatted_datetime = formatted_datetime.replace(" ", "^")
        username = request.user.username
        number_ofhymn = request.session.get('number_ofhymn', None)
        print(f"this is it {number_ofhymn} ")
        audio_data = request.POST.get('audio_data')
        format, audio_str = audio_data.split(';base64,')
        ext = format.split('/')[-1]
        audio_file = ContentFile(base64.b64decode(audio_str), name=f'recording.{ext}')
        
        # Ensure the 'inn' directory exists
        inn_directory = os.path.join(settings.MEDIA_ROOT, 'inn')
        os.makedirs(inn_directory, exist_ok=True)
        random_letters = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
        # Save the file to the 'inn' directory
        file_path = os.path.join(inn_directory, f'{str(username)}_{str(random_letters)}_{str(number_ofhymn)}.mid')
        with open(file_path, 'wb') as f:
            f.write(audio_file.read())
        
        return HttpResponse('Audio uploaded successfully')
    return HttpResponse('Invalid request method', status=405)
=======
            if len(values) == 2:

                # Extract the selected values and their colors
                value1 = values[0]['value']
                color1 = values[0]['color']
                value2 = values[1]['value']
                color2 = values[1]['color']
                print(value1)
                print(value2)
                if value1 > value2:
                    print(f'chords - {len(chords)} sorted - {len(sorted_offsets)} notes - {len(notes_and_rests_by_time_)}')
                    chords = chords[value2:value1]
                    sorted_offsets = sorted_offsets[value2:value1]
                    notes_and_rests_by_time_ = notes_and_rests_by_time_[value2:value1]
                    print(chords)
                    # durations = durations[value2:value1]
                else:
                    chords = chords[value1:value2]
                    durations = durations[value1:value2]
                music_stream = stream.Stream()

                # Iterate through the sorted offsets and add chords to the stream

                for offset, notes_and_rests in zip(sorted_offsets, notes_and_rests_by_time_):
                    chords = []

                    for item in notes_and_rests:
                        # Split the string into pitch (or 'Rest') and duration
                        parts = item.split()
                        if parts[0] == 'Rest':
                            # duration = float(parts[1])
                            # output_stream.append(music21.note.Rest(quarterLength=duration))
                            pass
                        else:
                            pitch = parts[0]
                            duration = float(parts[1])
                            chords.append(music21.note.Note(pitch, quarterLength=duration))

                    if chords:
                        # Create a chord and add it to the stream
                        music_stream.append(chord.Chord(chords))

                music_stream.show('midi')
>>>>>>> d64141e793585eba81673de8af9f37b259e7a589


from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.conf import settings
from .models import AudioRecord
import os
import base64
import random
import string
from datetime import datetime

def upload_audioo(request):
    if request.method == 'POST':
        # Get the current date and time
        current_datetime = datetime.now()

        # Format the date and time as a string
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        formatted_datetime = formatted_datetime.replace(" ", "^")
        username = request.user.username
        number_ofhymn = request.session.get('number_ofhymn', None)
        print(f"this is it {number_ofhymn} ")
        audio_data = request.POST.get('audio_data')
        format, audio_str = audio_data.split(';base64,')
        ext = format.split('/')[-1]
        audio_file = ContentFile(base64.b64decode(audio_str), name=f'recording.{ext}')
        
        # Ensure the 'inn' directory exists
        inn_directory = os.path.join(settings.MEDIA_ROOT, 'inn')
        os.makedirs(inn_directory, exist_ok=True)
        random_letters = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
        # Save the file to the 'inn' directory
        file_path = os.path.join(inn_directory, f'{str(username)}_{str(random_letters)}_{str(number_ofhymn)}.mid')
        with open(file_path, 'wb') as f:
            f.write(audio_file.read())
        
        # Save details to the database
        AudioRecord.objects.create(
            user=request.user,
            upload_datetime=current_datetime,
            # file_path=file_path,
            hymn_number=number_ofhymn,
            random_letters=random_letters
        )

        return HttpResponse('Audio uploaded successfully')
    return HttpResponse('Invalid request method', status=405)


from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
import os, random, string
from django.core.files.base import ContentFile
from .models import AudioRecord
from django.conf import settings

def upload_audio(request):
    if request.method == 'POST':
        # Get the current date and time
        current_datetime = datetime.now()

        # Format the date and time as a string
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        formatted_datetime = formatted_datetime.replace(" ", "^")
        username = request.user.username
        number_ofhymn = request.session.get('number_ofhymn', None)
        print(f"this is it {number_ofhymn} ")
        audio_data = request.POST.get('audio_data')
        format, audio_str = audio_data.split(';base64,')
        ext = format.split('/')[-1]
        audio_file = ContentFile(base64.b64decode(audio_str), name=f'recording.{ext}')
        
        # Ensure the 'inn' directory exists
        inn_directory = os.path.join(settings.MEDIA_ROOT, 'inn')
        os.makedirs(inn_directory, exist_ok=True)
        # random_letters = request.POST.get('recording_code')
        random_letters = request.session.get('random_letters', None)
        if random_letters == None:
            random_letters = request.session.get('random_word', None)
        print(f'I am fine {random_letters}')
        joining = request.session.get('joining', None)
        # if joining == 'true':
        if username:
            print(f'I am fine {username}')
            if random_letters is not None:
                random_letters = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
            
                # Save the file to the 'inn' directory
                file_path = os.path.join(inn_directory, f'{str(username)}_{str(random_letters)}_{str(number_ofhymn)}.mid')
                with open(file_path, 'wb') as f:
                    f.write(audio_file.read())
                # Redirect back to the same hymn with random_letters in the session
                request.session['random_letters'] = random_letters
                tempo_num = request.session.get('tempo_num', None)
                # Save details to the database
                AudioRecord.objects.create(
                    user=request.user,
                    upload_datetime=current_datetime,
                    hymn_number=number_ofhymn,
                    random_letters=random_letters,
                    tempo = tempo_num
                )
                print('seee')
                print(request.user)
                print(current_datetime)
                print(number_ofhymn)
                print(random_letters)
                print(tempo_num)
                return HttpResponse('Successfully submitted. <a href="/">Home</a>')

            else:
                # Save the file to the 'inn' directory
                print(f'the level is {random_letters}')
                random_code = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
                file_path = os.path.join(inn_directory, f'{str(random_code)}_{str(random_letters)}_{str(number_ofhymn)}.mid')
                with open(file_path, 'wb') as f:
                    f.write(audio_file.read())
                return HttpResponse('Successfully submitted. <a href="/">Home</a>')

            
                # Redirect back to the same hymn with random_letters in the session
                request.session['random_letters'] = random_letters
                # tempo_num = request.session.get('tempo_num', None)
                # # Save details to the database
                # AudioRecord.objects.create(
                #     user=request.user,
                #     upload_datetime=current_datetime,
                #     hymn_number=number_ofhymn,
                #     random_letters=random_letters,
                #     tempo = tempo_num
                # )

            return redirect('display_hymn')  # Assuming this is the hymn page URL pattern

        else:

            if random_letters == None:
                random_letters = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
            
                # Save the file to the 'inn' directory
                file_path = os.path.join(inn_directory, f'{str(username)}_{str(random_letters)}_{str(number_ofhymn)}.mid')
                with open(file_path, 'wb') as f:
                    f.write(audio_file.read())
                return HttpResponse('Successfully submitted. <a href="/">Home</a>')
            else:
                random_letterd = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
                # Save the file to the 'inn' directory
                file_path = os.path.join(inn_directory, f'{str(random_letterd)}_{str(random_letters)}_{str(number_ofhymn)}.mid')
                with open(file_path, 'wb') as f:
                    f.write(audio_file.read())
                return HttpResponse('Successfully submitted. <a href="/">Home</a>')
        # tempo_num = request.session.get('tempo_num', None)
        # # Save details to the database
        # AudioRecord.objects.create(
        #     user=request.user,
        #     upload_datetime=current_datetime,
        #     hymn_number=number_ofhymn,
        #     random_letters=random_letters,
        #     tempo = tempo_num
        # )
        # Redirect back to the same hymn with random_letters in the session
        request.session['random_letters'] = random_letters
        return redirect('display_hymn')  # Assuming this is the hymn page URL pattern

    return HttpResponse('Invalid request method', status=405)



import os
import base64
import os
import base64
# import audioread
# views.py
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_audioo(request):
    if request.method == 'POST':
        audio_data = request.FILES.get('audio_data')
        if audio_data:
            print("File received:", audio_data.name)  # Debugging statement
            # Define the path for the 'inn' directory within the media directory
            inn_directory = os.path.join(settings.MEDIA_ROOT, 'inn')
            if not os.path.exists(inn_directory):
                os.makedirs(inn_directory)

            # Save the uploaded file temporarily
            temp_path = default_storage.save('temp_audio.midi', audio_data)
            temp_file = default_storage.path(temp_path)

            # Define the output path for the MIDI file in the 'inn' directory
            mthd_path = os.path.join(inn_directory, 'audio_recording.midi')

            try:
                # Move the file to the final destination
                os.rename(temp_file, mthd_path)
                return HttpResponse('Audio file saved successfully in MThd format in the inn folder.')
            except Exception as e:
                print("Error moving file:", e)  # Debugging statement
                return HttpResponse('Failed to save audio file.')
    return HttpResponse('Failed to save audio file.')



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('hymn_search')  # Replace 'home' with your home view name
    else:
<<<<<<< HEAD
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


from django.shortcuts import render, redirect
from .models import AudioRecord  # Import your model

def join_group_recording(request):
    if request.method == "POST":
        recording_code = request.POST.get('recording_code')
        request.session['recording_code'] = recording_code
        print(f'___join_group_recording {recording_code}')
        number_ofhymn = request.session.get('number_ofhymn', None)
        recording_code = recording_code.replace(' ', '')
        
        if recording_code and number_ofhymn:
            # Query the database for a matching record
            try:
                record = AudioRecord.objects.get(random_letters=recording_code, hymn_number=number_ofhymn)
                username = record.user.username  # Retrieve the username
                tempo = record.tempo 
                print(number_ofhymn)
                print(f"Username: {username}")
            except AudioRecord.DoesNotExist:
                tempo = None
                print("No matching record found.")
            request.session['recording_code'] = recording_code
            request.session['number_ofhymn'] = number_ofhymn
        
            if tempo:
                request.session['tempo_num'] = tempo
                request.session['username'] = username 
        
                if number_ofhymn.startswith('am'):
            
                    return redirect('display_hymn_ang_ang')
                else:
                    return redirect('display_hymn_meth')  # Redirect after processing
            else:
                return HttpResponse('You entered an invalid code for this hymn.')

    # return redirect('display_hymn')


def display_hymn_meth(request):
    usernamee = request.session.get('username')
    request.session['joining'] = 'true'
    recording_code = request.session.get('recording_code', None)
    # number_ofhymn = request.session.get('number_ofhymn', None)
    print(f'<<<join_group_recording {recording_code}')
    request.session['recording_code'] = recording_code
    request.session['random_letters'] = recording_code
    def extract_html_file_names(directory):
        # List all files ending with .html
        html_files = [file for file in os.listdir(directory) if file.endswith('.html')]

        # Extract base names without extension
        base_names = [re.match(r'(.+?)\.html', file).group(1) for file in html_files]

        # Sort using a custom key
        def custom_sort_key(name):
            # Split into parts: numbers and non-numbers
            parts = re.split(r'(\d+)', name)
            # Convert numeric parts to integers for correct sorting
            parts = [int(part) if part.isdigit() else part for part in parts]
            return parts

        sorted_base_names = sorted(base_names, key=custom_sort_key)
        return sorted_base_names

    # Example usage:
    directory_path = 'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\lyrics' # Replace with your directory path
    html_files_list = extract_html_file_names(directory_path)
    hymn_numbers = html_files_list  # Define the list of hymn numbers
    number_ofhymn = request.session.get('number_ofhymn', None)
    hymn_number = str(number_ofhymn)
    hymn_number = hymn_number.replace('mhb', '')
    hymn_number = hymn_number.replace('am', '')

##
    if hymn_number is not None:
        # number_hymn = hymn_number.copy()
        print('there is the')
        print(type(hymn_number))
        print((hymn_number))
        # hymn_number = hymn_number.replace('mhb', '')
        # hymn_number = str(hymn_number)
=======
        timer = 1
>>>>>>> d64141e793585eba81673de8af9f37b259e7a589
        def generate_random_word():
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(4))

        random_word = generate_random_word()
<<<<<<< HEAD
        midi_file_path = f'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\media\\{random_word}.mid'
        # score.write('midi', fp=midi_file_path)
        request.session['random_word'] = random_word
        request.session['number_ofhymn'] = 'mhb'+hymn_number

        midi_messages = 1
        path = f"C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\tunes\\{hymn_number}.xml"
        score = music21.converter.parse(path)
        score.write('midi', fp=midi_file_path)
        hymn_data = fetch_hymn_from_file(hymn_number)
        # Initialize a list to store notes and rests at each point in time
        notes_and_rests_by_time = []
        notes_and_rests_by_time_ = []

        # Get all the notes, chords, and rests from the score
        all_notes = score.flat.getElementsByClass(music21.note.GeneralNote)

        # Create a dictionary to group elements by their starting offset
        elements_by_offset = {}

        # Iterate through the notes, chords, and rests and group them by offset
        for element in all_notes:
            offset = element.offset
            if offset not in elements_by_offset:
                elements_by_offset[offset] = []
            elements_by_offset[offset].append(element)

        # Sort the offsets in ascending order
        sorted_offsets = sorted(elements_by_offset.keys())

        notss = []

        # Iterate through the sorted offsets and collect notes and rests at each point in time
        for offset in sorted_offsets:
            elements = elements_by_offset[offset]
            notes_and_rests = []
            nots=[]

            for element in elements:
                if isinstance(element, music21.note.Note):
                    pitch = element.pitch
                    parts = re.split(r'(\d+)', str(pitch))
                    modified_item = ''.join(parts)
                    pitch = modified_item
                    notes_and_rests.append(f"{pitch}") # {element.duration.quarterLength}
                    nots.append(f"{pitch} {element.duration.quarterLength}")

                elif isinstance(element, music21.chord.Chord):
                    for chord_note in element:
                        chord_pitch = chord_note.pitch
                        parts = re.split(r'(\d+)', str(chord_pitch))
                        modified_item = ''.join(parts)
                        chord_pitch = modified_item
                        notes_and_rests.append(f"{chord_pitch}") # {chord_note.duration.quarterLength}
                        nots.append(f"{chord_pitch} {chord_note.duration.quarterLength}")

                elif isinstance(element, music21.note.Rest):
                    pass
                    # notes_and_rests.append(f"Rest Duration: {element.duration.quarterLength}")

            notes_and_rests_by_time.append(notes_and_rests)
            notes_and_rests_by_time_.append(nots)
            notes = notes_and_rests_by_time_
#
            data = notes
            # Function to extract note and octave
            def get_note_octave(note):
                parts = note.split()
                note_part = parts[0][:-1]
                octave = int(parts[0][-1])
                return note_part, octave

            # Sort each sublist by octave and then by note alphabetically
            sorted_data = [
                sorted(sublist, key=lambda x: (get_note_octave(x)[1], get_note_octave(x)[0]), reverse=True)
                for sublist in data
            ]

            sorted_data
#
            data = sorted_data
            data = notes_and_rests_by_time_
            # Function to remove duplicates if sublist has more than 4 members
            def remove_excess_duplicates(data):
                new_data = []
                for sublist in data:
                    if len(sublist) > 4:
                        seen = set()
                        filtered = []
                        for item in sublist:
                            if item not in seen:
                                seen.add(item)
                                filtered.append(item)
                            elif len(filtered) < 4:
                                filtered.append(item)
                        new_data.append(filtered[:4])
                    else:
                        new_data.append(sublist)
                return new_data

            result = remove_excess_duplicates(data)
            # print(result)
            notes_and_rests_by_time_ = result
            notes_and_rests_by_time_ = result
        # print('fir the check')
        # print(notes_and_rests_by_time_)
        for sublist in notes:
            if len(sublist) < 4:
                # print("A sublist has fewer than 4 items:", sublist)
                # Create DataFrame
                df = pd.DataFrame(notes, columns=['Note1', 'Note2', 'Note3', 'Note4'])

                # Function to extract duration from note string
                def extract_duration(note):
                    if isinstance(note, str):
                        parts = note.split()
                        if len(parts) == 2 and parts[1].replace('.', '').isdigit():
                            return float(parts[1])
                    return 0.0

                # Add cumulative duration columns
                for col in df.columns:
                    df[col + '_Cumulative'] = df[col].apply(extract_duration).cumsum()

                # Display the updated DataFrame
                # print(df)
                # Get the index of the first sublist with less than 4 members
                index = next((i for i, sublist in enumerate(notes) if len(sublist) < 4), None)
                index = index -1
                # print("Index of the first sublist with less than 4 members:", index)
                # Function to check the next sublist after the given index
                def check_next_sublist_length(notes, index):
                    if index + 1 < len(notes):
                        next_sublist = notes[index + 1]
                        return len(next_sublist) < 4
                    return False

                # Check the next sublist
                has_less_than_4_items = check_next_sublist_length(notes, index)
                # print(f"The next sublist after index {index} has less than 4 items: {has_less_than_4_items}")
                # Retrieve the highest cumulative duration and corresponding column names
                def get_highest_cumulative_info(df, index):
                    if index >= 0:
                        # Get the cumulative duration values for the specified row
                        cumulative_values = df.iloc[index, df.columns.str.endswith('_Cumulative')]
                        # Find the maximum value
                        max_duration = cumulative_values.max()
                        # Get the column names with the maximum value
                        columns_with_max_duration = cumulative_values[cumulative_values == max_duration].index.tolist()
                        return max_duration, columns_with_max_duration
                    return None, []

                # Execute the function
                max_duration, columns_with_max_duration = get_highest_cumulative_info(df, index)

                # print(f"Highest cumulative duration at index {index}: {max_duration}")
                # print("Column names with this highest cumulative duration:", columns_with_max_duration)
                # Define the lists
                list1 = ['Note1_Cumulative', 'Note2_Cumulative', 'Note3_Cumulative', 'Note4_Cumulative']
                list2 = columns_with_max_duration

                # Retrieve members in list1 that are not in list2
                result = [item for item in list1 if item not in list2]

                # print(result)  # Output: ['Note2_Cumulative']

                def replace_cumulative_notes(lst):
                    replacements = {
                        'Note1_Cumulative': 0,
                        'Note2_Cumulative': 1,
                        'Note3_Cumulative': 2,
                        'Note4_Cumulative': 3
                    }
                    
                    return [replacements.get(item, item) for item in lst]

                # Example usage
                input_list = ['Note1_Cumulative', 'Note2_Cumulative', 'Other', 'Note3_Cumulative', 'Note4_Cumulative']
                input_list = result
                output_list = replace_cumulative_notes(input_list)
                original_list =notes[index + 1]
                desired_length = 4

                # Create a new list with '-' as placeholders
                modified_list = ['-'] * desired_length

                # Insert the original list elements at their respective indexes
                indices = output_list

                # Ensure the indices length matches the original_list length
                for i, item in enumerate(original_list):
                    if i < len(indices):
                        modified_list[indices[i]] = item


                # New value to replace notes[6]
                new_value = modified_list
                # Replace the element at index 6
                notes[index+1] = new_value
                
                # Print the updated list
                aaa = notes.copy()
            else:
                aaa = notes_and_rests_by_time_.copy()
            
        def note_to_solfa(note, key):
            solfa_mappings = {
            'C major': {
                'C': 'd', 'D': 'r', 'E': 'm', 'F': 'f', 'G': 's',
                'A': 'l', 'B': 't', 'C#': 'di', 'D#': 'ri', 'F#': 'fi',
                'G#': 'si', 'A#': 'li'
            },
            'C# major': {
                'C#': 'd', 'D#': 'r', 'E#': 'm', 'F#': 'f', 'G#': 's',
                'A#': 'l', 'B#': 't', 'D': 'ra', 'F': 'fa', 'A': 'la'
            },
            'B minor': {
                'B': 'd', 'C#': 'r', 'D': 'm', 'E': 'f', 'F#': 's',
                'G': 'l', 'A': 't', 'E#': 'fi', 'A#': 'ti', 'C': 'ma'
            },
            'A minor': {
                'A': 'd', 'B': 'r', 'C': 'm', 'D': 'f', 'E': 's',
                'F': 'l', 'G': 't', 'C#': 'mi', 'D#': 'fi', 'G#': 'te'
            },
            'A major': {
                'A': 'd', 'B': 'r', 'C#': 'm', 'D': 'f', 'E': 's',
                'F#': 'l', 'G#': 't', 'D#': 'fi', 'G': 'le'
            },
            'D minor': {
                'D': 'd', 'E': 'r', 'F': 'm', 'G': 'f', 'A': 's',
                'B-': 'l', 'C': 't', 'E-': 'ri', 'A-': 'se'
            },
            'G minor': {
                'G': 'd', 'A': 'r', 'B-': 'm', 'C': 'f', 'D': 's',
                'E-': 'l', 'F': 't', 'A-': 'fi', 'D#': 'si'
            },
            'G major': {
                'G': 'd', 'A': 'r', 'B': 'm', 'C': 'f', 'D': 's',
                'E': 'l', 'F#': 't', 'F': 'fi', 'C#': 'fi'
            },
            'E- major': {
                'E-': 'd', 'F': 'r', 'G': 'm', 'A-': 'f', 'B-': 's',
                'C': 'l', 'D': 't', 'A': 'se', 'B': 'ma'
            },
            'C minor': {
                'C': 'd', 'D': 'r', 'E-': 'm', 'F': 'f', 'G': 's',
                'A-': 'l', 'B-': 't', 'E': 'mi', 'A': 'li'
            },
            'B- major': {
                'B-': 'd', 'C': 'r', 'D': 'm', 'E-': 'f', 'F': 's',
                'G': 'l', 'A': 't', 'D#': 'ra', 'F#': 'si'
            },
            'A- major': {
                'A-': 'd', 'B-': 'r', 'C': 'm', 'D-': 'f', 'E-': 's',
                'F': 'l', 'G': 't', 'D': 'ma', 'E': 'li'
            },
            'D major': {
                'D': 'd', 'E': 'r', 'F#': 'm', 'G': 'f', 'A': 's',
                'B': 'l', 'C#': 't', 'G#': 'ma', 'E#': 'ri'
            },
            'B- minor': {
                'B-': 'd', 'C': 'r', 'D-': 'm', 'E-': 'f', 'F': 's',
                'G-': 'l', 'A-': 't', 'E': 'mi', 'G': 'fi'
            },
            'F minor': {
                'F': 'd', 'G': 'r', 'A-': 'm', 'B-': 'f', 'C': 's',
                'D-': 'l', 'E-': 't', 'B': 'si', 'G-': 'fi'
            },
            'E minor': {
                'E': 'd', 'F#': 'r', 'G': 'm', 'A': 'f', 'B': 's',
                'C': 'l', 'D': 't', 'A#': 'li', 'G#': 'si'
            },
            'F major': {
                'F': 'd', 'G': 'r', 'A': 'm', 'B-': 'f', 'C': 's',
                'D': 'l', 'E': 't', 'C#': 'fi', 'G#': 'le'
            },
            'E major': {
                'E': 'd', 'F#': 'r', 'G#': 'm', 'A': 'f', 'B': 's',
                'C#': 'l', 'D#': 't', 'A#': 'li', 'B#': 'si'
            }
        }
            
            mapping = solfa_mappings[key]
            if note == '-':
                return '-'
            note_name, duration = note.split()
            note_name = note_name[:-1]  # Remove the octave number
            solfa = mapping.get(note_name, note_name)
            return f"{solfa} {duration}"

        notes_ = notes
        # Get the key signature
        key_signature = score.analyze('key')

    #
        def capitalize_first_letter(s):
            if s and s[0].islower():
                return s[0].upper() + s[1:]
            return s

        # Example usage
        strin = str(key_signature)
        capitalized_string = capitalize_first_letter(strin)
        music_key = capitalized_string
#
        print(f"The key of the piece is: {key_signature}")
        solfa_notes = [[note_to_solfa(note, key=capitalized_string) for note in chord] for chord in notes_]
        chords = []
        for chord in solfa_notes:
            chords.append(chord)
        notes = chords

        # Remove sublists with all members being '-'
        filtered_notes = [sublist for sublist in notes if sublist.count('-') < 4]

        filtered_notes
        new_data = filtered_notes.copy()
        data = [(index + 1, *row) for index, row in enumerate(new_data)]


        selected_voice_part = request.GET.get('voice_part')
        if selected_voice_part:
            if selected_voice_part == 'All':
                pass
            else:


                voice_map = {
                    'Soprano': 0,
                    'Alto': 1,
                    'Tenor': 2,
                    'Bass': 3
                }

                kogi = selected_voice_part
                voice_num = voice_map.get(kogi)


                # Given music notes
                try:
                    music_notes = notes_
                    # print(music_notes)
                except NameError:
                    music_notes = notes_.copy()
                    print(f'music notes are except {music_notes}')
                note_a = music_notes
                # Remove empty sublists
                filtered_notes = [sublist for sublist in note_a if sublist]

                music_notes = filtered_notes.copy()
                # print('Ongoing')
                # print(music_notes)
                # Create a stream
                melody = stream.Stream()
                tempo_num = request.session.get('tempo_num', None)

                # Extract and add the first note from each sublist
                for sublist in music_notes:
                    note_str = sublist[voice_num]  # First member of each sublist
                    if note_str == '-':
                        pass
                    else:

                        pitch, duration = note_str.split()  # Split into pitch and duration
                        duration = float(duration)  # Convert duration to float
                        # Create a note object and add it to the stream
                        n = note.Note(pitch)
                        n.quarterLength = duration*tempo_num
                        melody.append(n)

                # Show (and play) the stream
                # melody.show('midi')

                def generate_random_word():
                    letters = string.ascii_lowercase
                    return ''.join(random.choice(letters) for _ in range(4))

                random_word = generate_random_word()
                midi_file_path = f'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\media\\{random_word}.mid'
                # score.write('midi', fp=midi_file_path)
                request.session['random_word'] = random_word
                midi_messages = 1
                path = f"C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\tunes\\{hymn_number}.xml"
                # score = music21.converter.parse(path)
                melody.write('midi', fp=midi_file_path)
                # hymn_data = fetch_hymn_from_file_ang(hymn_number)


        if hymn_data:
            hymn_data = re.sub(r'(?<!HYMN\s)(\d+)(?=\s)', r'<br><br> \1', hymn_data)
            aa = type(hymn_data)
            # Retrieve the AudioRecord for the given hymn_number and logged-in user, if it exists
            random_letters = None
            # print(f"1this is the randomess {hymn_number}")
            if request.user.is_authenticated:
                # print('hemmy')
                try:
                    audio_record = AudioRecord.objects.get(user=request.user, hymn_number='mhb'+hymn_number)
                    random_letters = audio_record.random_letters
                    request.session['random_letters'] = random_letters
                    # print(f"this is the randomess {random_letters}")
                except AudioRecord.DoesNotExist:
                    random_letters = None
                return render(request, 'hymn_display_meth.html', {'usernamee':usernamee,'hymn_number':hymn_number, 'hymn_data': hymn_data, 'random_letters':random_letters, 'data':data, 'music_key': music_key, 'selected_voice_part': selected_voice_part, 'hymn_numbers': hymn_numbers})
            return render(request, 'hymn_display_meth.html', {'usernamee':usernamee,'hymn_number':hymn_number, 'hymn_data': hymn_data, 'data':data, 'music_key': music_key, 'selected_voice_part': selected_voice_part, 'hymn_numbers': hymn_numbers})
        else:
            return render(request, 'hymn_display_meth.html', {'error_message': 'Hymn not found.', 'hymn_numbers': hymn_numbers})
    else:
        return render(request, 'hymn_display_meth.html', {'error_message': 'Please select or enter a hymn number.', 'hymn_numbers': hymn_numbers})
=======
        midi_file_path = '/home/kofi532/asedachorale/media/'+random_word+'.mid'
        print(midi_file_path)
        print('rasta')
        music_stream.write('midi', fp=midi_file_path)
        request.session['random_word'] = random_word
        return render(request, 'home.html', {'timer':timer, 'chords':chrd, 'random_word': random_word})
        # return JsonResponse({'error': 'Invalid request method'}, status=405)
>>>>>>> d64141e793585eba81673de8af9f37b259e7a589

def download_midi(request):
    random_word = request.session.get('random_word', None)
    midi_file_path = os.path.join(settings.MEDIA_ROOT, random_word+'.mid')
    response = FileResponse(open(midi_file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{random_word}.mid"'
    return response

def contact(request):
    return render(request, 'contact.html')

def first(request):
    return render(request, 'first.html', {})


def privacy(request):
    return render(request, 'privacy.html')

def anthems(request):
    return render(request, 'search_anthems.html')

def armah(request):
    try:
        directory = r'/home/kofi532/asedachorale/adom/templates/anthems_lyrics'
        file_names = [filename[:-5] for filename in os.listdir(directory) if filename.endswith('.html')]
        if request.method == 'POST':
            clicked_value = request.POST.get('num')  # Extract the value of the clicked button
            # return JsonResponse({'status': 'success'})
            def generate_random_word():
                letters = string.ascii_lowercase
                return ''.join(random.choice(letters) for _ in range(4))

            random_word = generate_random_word()
            midi_file_path = f'/home/kofi532/asedachorale/media/{random_word}.mid'
            # score.write('midi', fp=midi_file_path)
            request.session['random_word'] = random_word
            midi_messages = 1
            clicked_value_ = clicked_value.replace('_', '-').lower()
            path = f"/home/kofi532/asedachorale/adom/templates/tunes_anthems/{clicked_value_}.xml"
            score = music21.converter.parse(path)
            score.write('midi', fp=midi_file_path)
            # return render(request, '/home/kofi532/asedachorale/lyrics/'+str(clicked_value)+'.html', {'lists': lists, 'clicked_value':clicked_value})
            clicked_value=clicked_value.upper()

            # clicked_value_ = replace_underscore_with_dash(clicked_value)
            clicked_value_ = clicked_value.lower()
            return render(request, '/home/kofi532/asedachorale/adom/templates/anthems_lyrics/'+str(clicked_value_)+'.html', {'clicked_value':clicked_value})

        return render(request, 'armah.html', {'file_names': file_names})
    except:
        return render(request, 'sorry.html', {})

def armah_songs(request):
    # clicked_value = ''
    # request.session['clicked_value'] = clicked_value
    clicked_value = request.session.get('clicked_value', None)
    return render(request, '/home/kofi532/asedachorale/anthems_lyrics/'+str(clicked_value)+'.html', {'clicked_value':clicked_value})




def display_hymn_ang(request):
    def extract_html_file_names(directory):
        # List all files ending with .html
        html_files = [file for file in os.listdir(directory) if file.endswith('.html')]

        # Extract base names without extension
        base_names = [re.match(r'(.+?)\.html', file).group(1) for file in html_files]

        # Sort using a custom key
        def custom_sort_key(name):
            # Split into parts: numbers and non-numbers
            parts = re.split(r'(\d+)', name)
            # Convert numeric parts to integers for correct sorting
            parts = [int(part) if part.isdigit() else part for part in parts]
            return parts

        sorted_base_names = sorted(base_names, key=custom_sort_key)
        return sorted_base_names

    # Example usage:
    directory_path = 'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\lyrics_ang' # Replace with your directory path
    html_files_list = extract_html_file_names(directory_path)
    hymn_numbers = html_files_list  # Define the list of hymn numbers
    hymn_number = request.GET.get('hymn_number')


##
    if hymn_number is not None:
        print('there is the')
        print(type(hymn_number))
        print((hymn_number))
        # hymn_number = hymn_number.replace('mhb', '')
        # hymn_number = str(hymn_number)
        def generate_random_word():
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(4))

        random_word = generate_random_word()
        midi_file_path = f'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\media\\{random_word}.mid'
        # score.write('midi', fp=midi_file_path)
        request.session['random_word'] = random_word
        request.session['number_ofhymn'] = 'am'+hymn_number

        midi_messages = 1
        path = f"C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\anglican_tunes\\{hymn_number}.xml"
        score = music21.converter.parse(path)
        score.write('midi', fp=midi_file_path)
        hymn_data = fetch_hymn_from_file(hymn_number)
        # Initialize a list to store notes and rests at each point in time
        notes_and_rests_by_time = []
        notes_and_rests_by_time_ = []

        # Get all the notes, chords, and rests from the score
        all_notes = score.flat.getElementsByClass(music21.note.GeneralNote)

        # Create a dictionary to group elements by their starting offset
        elements_by_offset = {}

        # Iterate through the notes, chords, and rests and group them by offset
        for element in all_notes:
            offset = element.offset
            if offset not in elements_by_offset:
                elements_by_offset[offset] = []
            elements_by_offset[offset].append(element)

        # Sort the offsets in ascending order
        sorted_offsets = sorted(elements_by_offset.keys())

        notss = []

        # Iterate through the sorted offsets and collect notes and rests at each point in time
        for offset in sorted_offsets:
            elements = elements_by_offset[offset]
            notes_and_rests = []
            nots=[]

            for element in elements:
                if isinstance(element, music21.note.Note):
                    pitch = element.pitch
                    parts = re.split(r'(\d+)', str(pitch))
                    modified_item = ''.join(parts)
                    pitch = modified_item
                    notes_and_rests.append(f"{pitch}") # {element.duration.quarterLength}
                    nots.append(f"{pitch} {element.duration.quarterLength}")

                elif isinstance(element, music21.chord.Chord):
                    for chord_note in element:
                        chord_pitch = chord_note.pitch
                        parts = re.split(r'(\d+)', str(chord_pitch))
                        modified_item = ''.join(parts)
                        chord_pitch = modified_item
                        notes_and_rests.append(f"{chord_pitch}") # {chord_note.duration.quarterLength}
                        nots.append(f"{chord_pitch} {chord_note.duration.quarterLength}")

                elif isinstance(element, music21.note.Rest):
                    pass
                    # notes_and_rests.append(f"Rest Duration: {element.duration.quarterLength}")

            notes_and_rests_by_time.append(notes_and_rests)
            notes_and_rests_by_time_.append(nots)
            notes = notes_and_rests_by_time_
#
            data = notes
            # Function to extract note and octave
            def get_note_octave(note):
                parts = note.split()
                note_part = parts[0][:-1]
                octave = int(parts[0][-1])
                return note_part, octave

            # Sort each sublist by octave and then by note alphabetically
            sorted_data = [
                sorted(sublist, key=lambda x: (get_note_octave(x)[1], get_note_octave(x)[0]), reverse=True)
                for sublist in data
            ]

            sorted_data
#
            data = sorted_data
            data = notes_and_rests_by_time_
            # Function to remove duplicates if sublist has more than 4 members
            def remove_excess_duplicates(data):
                new_data = []
                for sublist in data:
                    if len(sublist) > 4:
                        seen = set()
                        filtered = []
                        for item in sublist:
                            if item not in seen:
                                seen.add(item)
                                filtered.append(item)
                            elif len(filtered) < 4:
                                filtered.append(item)
                        new_data.append(filtered[:4])
                    else:
                        new_data.append(sublist)
                return new_data

            result = remove_excess_duplicates(data)
            # print(result)
            notes_and_rests_by_time_ = result
            notes_and_rests_by_time_ = result
        # print('fir the check')
        # print(notes_and_rests_by_time_)
        for sublist in notes:
            if len(sublist) < 4:
                # print("A sublist has fewer than 4 items:", sublist)
                # Create DataFrame
                df = pd.DataFrame(notes, columns=['Note1', 'Note2', 'Note3', 'Note4'])

                # Function to extract duration from note string
                def extract_duration(note):
                    if isinstance(note, str):
                        parts = note.split()
                        if len(parts) == 2 and parts[1].replace('.', '').isdigit():
                            return float(parts[1])
                    return 0.0

                # Add cumulative duration columns
                for col in df.columns:
                    df[col + '_Cumulative'] = df[col].apply(extract_duration).cumsum()

                # Display the updated DataFrame
                # print(df)
                # Get the index of the first sublist with less than 4 members
                index = next((i for i, sublist in enumerate(notes) if len(sublist) < 4), None)
                index = index -1
                # print("Index of the first sublist with less than 4 members:", index)
                # Function to check the next sublist after the given index
                def check_next_sublist_length(notes, index):
                    if index + 1 < len(notes):
                        next_sublist = notes[index + 1]
                        return len(next_sublist) < 4
                    return False

                # Check the next sublist
                has_less_than_4_items = check_next_sublist_length(notes, index)
                # print(f"The next sublist after index {index} has less than 4 items: {has_less_than_4_items}")
                # Retrieve the highest cumulative duration and corresponding column names
                def get_highest_cumulative_info(df, index):
                    if index >= 0:
                        # Get the cumulative duration values for the specified row
                        cumulative_values = df.iloc[index, df.columns.str.endswith('_Cumulative')]
                        # Find the maximum value
                        max_duration = cumulative_values.max()
                        # Get the column names with the maximum value
                        columns_with_max_duration = cumulative_values[cumulative_values == max_duration].index.tolist()
                        return max_duration, columns_with_max_duration
                    return None, []

                # Execute the function
                max_duration, columns_with_max_duration = get_highest_cumulative_info(df, index)

                # print(f"Highest cumulative duration at index {index}: {max_duration}")
                # print("Column names with this highest cumulative duration:", columns_with_max_duration)
                # Define the lists
                list1 = ['Note1_Cumulative', 'Note2_Cumulative', 'Note3_Cumulative', 'Note4_Cumulative']
                list2 = columns_with_max_duration

                # Retrieve members in list1 that are not in list2
                result = [item for item in list1 if item not in list2]

                # print(result)  # Output: ['Note2_Cumulative']

                def replace_cumulative_notes(lst):
                    replacements = {
                        'Note1_Cumulative': 0,
                        'Note2_Cumulative': 1,
                        'Note3_Cumulative': 2,
                        'Note4_Cumulative': 3
                    }
                    
                    return [replacements.get(item, item) for item in lst]

                # Example usage
                input_list = ['Note1_Cumulative', 'Note2_Cumulative', 'Other', 'Note3_Cumulative', 'Note4_Cumulative']
                input_list = result
                output_list = replace_cumulative_notes(input_list)
                original_list =notes[index + 1]
                desired_length = 4

                # Create a new list with '-' as placeholders
                modified_list = ['-'] * desired_length

                # Insert the original list elements at their respective indexes
                indices = output_list

                # Ensure the indices length matches the original_list length
                for i, item in enumerate(original_list):
                    if i < len(indices):
                        modified_list[indices[i]] = item


                # New value to replace notes[6]
                new_value = modified_list
                # Replace the element at index 6
                notes[index+1] = new_value
                
                # Print the updated list
                aaa = notes.copy()
            else:
                aaa = notes_and_rests_by_time_.copy()
            
        def note_to_solfa(note, key):
            solfa_mappings = {
            'C major': {
                'C': 'd', 'D': 'r', 'E': 'm', 'F': 'f', 'G': 's',
                'A': 'l', 'B': 't', 'C#': 'di', 'D#': 'ri', 'F#': 'fi',
                'G#': 'si', 'A#': 'li'
            },
            'C# major': {
                'C#': 'd', 'D#': 'r', 'E#': 'm', 'F#': 'f', 'G#': 's',
                'A#': 'l', 'B#': 't', 'D': 'ra', 'F': 'fa', 'A': 'la'
            },
            'B minor': {
                'B': 'd', 'C#': 'r', 'D': 'm', 'E': 'f', 'F#': 's',
                'G': 'l', 'A': 't', 'E#': 'fi', 'A#': 'ti', 'C': 'ma'
            },
            'A minor': {
                'A': 'd', 'B': 'r', 'C': 'm', 'D': 'f', 'E': 's',
                'F': 'l', 'G': 't', 'C#': 'mi', 'D#': 'fi', 'G#': 'te'
            },
            'A major': {
                'A': 'd', 'B': 'r', 'C#': 'm', 'D': 'f', 'E': 's',
                'F#': 'l', 'G#': 't', 'D#': 'fi', 'G': 'le'
            },
            'D minor': {
                'D': 'd', 'E': 'r', 'F': 'm', 'G': 'f', 'A': 's',
                'B-': 'l', 'C': 't', 'E-': 'ri', 'A-': 'se'
            },
            'G minor': {
                'G': 'd', 'A': 'r', 'B-': 'm', 'C': 'f', 'D': 's',
                'E-': 'l', 'F': 't', 'A-': 'fi', 'D#': 'si'
            },
            'G major': {
                'G': 'd', 'A': 'r', 'B': 'm', 'C': 'f', 'D': 's',
                'E': 'l', 'F#': 't', 'F': 'fi', 'C#': 'fi'
            },
            'E- major': {
                'E-': 'd', 'F': 'r', 'G': 'm', 'A-': 'f', 'B-': 's',
                'C': 'l', 'D': 't', 'A': 'se', 'B': 'ma'
            },
            'C minor': {
                'C': 'd', 'D': 'r', 'E-': 'm', 'F': 'f', 'G': 's',
                'A-': 'l', 'B-': 't', 'E': 'mi', 'A': 'li'
            },
            'B- major': {
                'B-': 'd', 'C': 'r', 'D': 'm', 'E-': 'f', 'F': 's',
                'G': 'l', 'A': 't', 'D#': 'ra', 'F#': 'si'
            },
            'A- major': {
                'A-': 'd', 'B-': 'r', 'C': 'm', 'D-': 'f', 'E-': 's',
                'F': 'l', 'G': 't', 'D': 'ma', 'E': 'li'
            },
            'D major': {
                'D': 'd', 'E': 'r', 'F#': 'm', 'G': 'f', 'A': 's',
                'B': 'l', 'C#': 't', 'G#': 'ma', 'E#': 'ri'
            },
            'B- minor': {
                'B-': 'd', 'C': 'r', 'D-': 'm', 'E-': 'f', 'F': 's',
                'G-': 'l', 'A-': 't', 'E': 'mi', 'G': 'fi'
            },
            'F minor': {
                'F': 'd', 'G': 'r', 'A-': 'm', 'B-': 'f', 'C': 's',
                'D-': 'l', 'E-': 't', 'B': 'si', 'G-': 'fi'
            },
            'E minor': {
                'E': 'd', 'F#': 'r', 'G': 'm', 'A': 'f', 'B': 's',
                'C': 'l', 'D': 't', 'A#': 'li', 'G#': 'si'
            },
            'F major': {
                'F': 'd', 'G': 'r', 'A': 'm', 'B-': 'f', 'C': 's',
                'D': 'l', 'E': 't', 'C#': 'fi', 'G#': 'le'
            },
            'E major': {
                'E': 'd', 'F#': 'r', 'G#': 'm', 'A': 'f', 'B': 's',
                'C#': 'l', 'D#': 't', 'A#': 'li', 'B#': 'si'
            }
        }
            
            mapping = solfa_mappings[key]
            if note == '-':
                return '-'
            note_name, duration = note.split()
            note_name = note_name[:-1]  # Remove the octave number
            solfa = mapping.get(note_name, note_name)
            return f"{solfa} {duration}"

        notes_ = notes
        # Get the key signature
        key_signature = score.analyze('key')

    #
        def capitalize_first_letter(s):
            if s and s[0].islower():
                return s[0].upper() + s[1:]
            return s

        # Example usage
        strin = str(key_signature)
        capitalized_string = capitalize_first_letter(strin)
        music_key = capitalized_string
#
        print(f"The key of the piece is: {key_signature}")
        solfa_notes = [[note_to_solfa(note, key=capitalized_string) for note in chord] for chord in notes_]
        chords = []
        for chord in solfa_notes:
            chords.append(chord)
        notes = chords

        # Remove sublists with all members being '-'
        filtered_notes = [sublist for sublist in notes if sublist.count('-') < 4]

        filtered_notes
        new_data = filtered_notes.copy()
        data = [(index + 1, *row) for index, row in enumerate(new_data)]
        tempo = request.GET.get('tempo','1x')

        selected_voice_part = request.GET.get('voice_part')
        if selected_voice_part:
            if selected_voice_part == 'All':
                pass
            else:
                if tempo:
                    tempo_map = {   
                        '1x':1,
                        '3x': 0.60,
                        '2x': 0.85,
                        '-2x': 1.30,
                        '-3x': 1.50,
                    }

                    tempo_num = tempo_map.get(tempo)
                    request.session['tempo_num'] = tempo_num
                else:
                    tempo_num = 1
                voice_map = {
                    'Soprano': 0,
                    'Alto': 1,
                    'Tenor': 2,
                    'Bass': 3
                }

                kogi = selected_voice_part
                voice_num = voice_map.get(kogi)


                # Given music notes
                try:
                    music_notes = notes_
                    # print(music_notes)
                except NameError:
                    music_notes = notes_.copy()
                    print(f'music notes are except {music_notes}')
                note_a = music_notes
                # Remove empty sublists
                filtered_notes = [sublist for sublist in note_a if sublist]

                music_notes = filtered_notes.copy()
                print('Ongoing')
                print(music_notes)
                # Create a stream
                melody = stream.Stream()

                # Extract and add the first note from each sublist
                for sublist in music_notes:
                    note_str = sublist[voice_num]  # First member of each sublist
                    if note_str == '-':
                        pass
                    else:

                        pitch, duration = note_str.split()  # Split into pitch and duration
                        duration = float(duration)  # Convert duration to float
                        # Create a note object and add it to the stream
                        n = note.Note(pitch)
                        n.quarterLength = duration*tempo_num
                        melody.append(n)

                # Show (and play) the stream
                # melody.show('midi')

                def generate_random_word():
                    letters = string.ascii_lowercase
                    return ''.join(random.choice(letters) for _ in range(4))

                random_word = generate_random_word()
                midi_file_path = f'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\media\\{random_word}.mid'
                # score.write('midi', fp=midi_file_path)
                request.session['random_word'] = random_word
                midi_messages = 1
                path = f"C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\anglican_tunes\\{hymn_number}.xml"
                # score = music21.converter.parse(path)
                melody.write('midi', fp=midi_file_path)
                # hymn_data = fetch_hymn_from_file_ang(hymn_number)


        if hymn_data:
            hymn_data = re.sub(r'(?<!HYMN\s)(\d+)(?=\s)', r'<br><br> \1', hymn_data)
            aa = type(hymn_data)
            # Retrieve the AudioRecord for the given hymn_number and logged-in user, if it exists
            random_letters = None
            # print(f"1this is the randomess {hymn_number}")
            if request.user.is_authenticated:
                # print('hemmy')
                try:
                    audio_record = AudioRecord.objects.get(user=request.user, hymn_number='am'+hymn_number)
                    random_letters = audio_record.random_letters
                    request.session['hymn_number'] = 'am'+hymn_number
                    request.session['random_letters'] = random_letters
                    # print(f"this is the randomess {random_letters}")
                except AudioRecord.DoesNotExist:
                    random_letters = None
                return render(request, 'hymn_display_ang.html', {'hymn_number':hymn_number, 'hymn_data': hymn_data, 'random_letters':random_letters, 'data':data, 'music_key': music_key, 'selected_voice_part': selected_voice_part, 'hymn_numbers': hymn_numbers})
            return render(request, 'hymn_display_ang.html', {'hymn_number':hymn_number, 'hymn_data': hymn_data, 'data':data, 'music_key': music_key, 'selected_voice_part': selected_voice_part, 'hymn_numbers': hymn_numbers})
        else:
            return render(request, 'hymn_display_ang.html', {'error_message': 'Hymn not found.', 'hymn_numbers': hymn_numbers})
    else:
        return render(request, 'hymn_display_ang.html', {'error_message': 'Please select or enter a hymn number.', 'hymn_numbers': hymn_numbers})


def display_hymn_ang_angg(request):
    def extract_html_file_names(directory):
        # List all files ending with .html
        html_files = [file for file in os.listdir(directory) if file.endswith('.html')]

        # Extract base names without extension
        base_names = [re.match(r'(.+?)\.html', file).group(1) for file in html_files]

        # Sort using a custom key
        def custom_sort_key(name):
            # Split into parts: numbers and non-numbers
            parts = re.split(r'(\d+)', name)
            # Convert numeric parts to integers for correct sorting
            parts = [int(part) if part.isdigit() else part for part in parts]
            return parts

        sorted_base_names = sorted(base_names, key=custom_sort_key)
        return sorted_base_names

    # Example usage:
    directory_path = 'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\lyrics_ang' # Replace with your directory path
    html_files_list = extract_html_file_names(directory_path)
    hymn_numbers = html_files_list  # Define the list of hymn numbers
    hymn_number = request.GET.get('hymn_number')
    number_ofhymn = request.session.get('number_ofhymn', None)
    hymn_number = str(number_ofhymn)
    hymn_number = hymn_number.replace('mhb', '')
    hymn_number = hymn_number.replace('am', '')
##
    if hymn_number is not None:
        print('there is the')
        print(type(hymn_number))
        print((hymn_number))
        # hymn_number = hymn_number.replace('mhb', '')
        # hymn_number = str(hymn_number)
        def generate_random_word():
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(4))

        random_word = generate_random_word()
        midi_file_path = f'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\media\\{random_word}.mid'
        # score.write('midi', fp=midi_file_path)
        request.session['random_word'] = random_word
        request.session['number_ofhymn'] = 'am'+hymn_number

        midi_messages = 1
        path = f"C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\anglican_tunes\\{hymn_number}.xml"
        score = music21.converter.parse(path)
        score.write('midi', fp=midi_file_path)
        hymn_data = fetch_hymn_from_file(hymn_number)
        # Initialize a list to store notes and rests at each point in time
        notes_and_rests_by_time = []
        notes_and_rests_by_time_ = []

        # Get all the notes, chords, and rests from the score
        all_notes = score.flat.getElementsByClass(music21.note.GeneralNote)

        # Create a dictionary to group elements by their starting offset
        elements_by_offset = {}

        # Iterate through the notes, chords, and rests and group them by offset
        for element in all_notes:
            offset = element.offset
            if offset not in elements_by_offset:
                elements_by_offset[offset] = []
            elements_by_offset[offset].append(element)

        # Sort the offsets in ascending order
        sorted_offsets = sorted(elements_by_offset.keys())

        notss = []

        # Iterate through the sorted offsets and collect notes and rests at each point in time
        for offset in sorted_offsets:
            elements = elements_by_offset[offset]
            notes_and_rests = []
            nots=[]

            for element in elements:
                if isinstance(element, music21.note.Note):
                    pitch = element.pitch
                    parts = re.split(r'(\d+)', str(pitch))
                    modified_item = ''.join(parts)
                    pitch = modified_item
                    notes_and_rests.append(f"{pitch}") # {element.duration.quarterLength}
                    nots.append(f"{pitch} {element.duration.quarterLength}")

                elif isinstance(element, music21.chord.Chord):
                    for chord_note in element:
                        chord_pitch = chord_note.pitch
                        parts = re.split(r'(\d+)', str(chord_pitch))
                        modified_item = ''.join(parts)
                        chord_pitch = modified_item
                        notes_and_rests.append(f"{chord_pitch}") # {chord_note.duration.quarterLength}
                        nots.append(f"{chord_pitch} {chord_note.duration.quarterLength}")

                elif isinstance(element, music21.note.Rest):
                    pass
                    # notes_and_rests.append(f"Rest Duration: {element.duration.quarterLength}")

            notes_and_rests_by_time.append(notes_and_rests)
            notes_and_rests_by_time_.append(nots)
            notes = notes_and_rests_by_time_
#
            data = notes
            # Function to extract note and octave
            def get_note_octave(note):
                parts = note.split()
                note_part = parts[0][:-1]
                octave = int(parts[0][-1])
                return note_part, octave

            # Sort each sublist by octave and then by note alphabetically
            sorted_data = [
                sorted(sublist, key=lambda x: (get_note_octave(x)[1], get_note_octave(x)[0]), reverse=True)
                for sublist in data
            ]

            sorted_data
#
            data = sorted_data
            data = notes_and_rests_by_time_
            # Function to remove duplicates if sublist has more than 4 members
            def remove_excess_duplicates(data):
                new_data = []
                for sublist in data:
                    if len(sublist) > 4:
                        seen = set()
                        filtered = []
                        for item in sublist:
                            if item not in seen:
                                seen.add(item)
                                filtered.append(item)
                            elif len(filtered) < 4:
                                filtered.append(item)
                        new_data.append(filtered[:4])
                    else:
                        new_data.append(sublist)
                return new_data

            result = remove_excess_duplicates(data)
            # print(result)
            notes_and_rests_by_time_ = result
            notes_and_rests_by_time_ = result
        # print('fir the check')
        # print(notes_and_rests_by_time_)
        for sublist in notes:
            if len(sublist) < 4:
                # print("A sublist has fewer than 4 items:", sublist)
                # Create DataFrame
                df = pd.DataFrame(notes, columns=['Note1', 'Note2', 'Note3', 'Note4'])

                # Function to extract duration from note string
                def extract_duration(note):
                    if isinstance(note, str):
                        parts = note.split()
                        if len(parts) == 2 and parts[1].replace('.', '').isdigit():
                            return float(parts[1])
                    return 0.0

                # Add cumulative duration columns
                for col in df.columns:
                    df[col + '_Cumulative'] = df[col].apply(extract_duration).cumsum()

                # Display the updated DataFrame
                # print(df)
                # Get the index of the first sublist with less than 4 members
                index = next((i for i, sublist in enumerate(notes) if len(sublist) < 4), None)
                index = index -1
                # print("Index of the first sublist with less than 4 members:", index)
                # Function to check the next sublist after the given index
                def check_next_sublist_length(notes, index):
                    if index + 1 < len(notes):
                        next_sublist = notes[index + 1]
                        return len(next_sublist) < 4
                    return False

                # Check the next sublist
                has_less_than_4_items = check_next_sublist_length(notes, index)
                # print(f"The next sublist after index {index} has less than 4 items: {has_less_than_4_items}")
                # Retrieve the highest cumulative duration and corresponding column names
                def get_highest_cumulative_info(df, index):
                    if index >= 0:
                        # Get the cumulative duration values for the specified row
                        cumulative_values = df.iloc[index, df.columns.str.endswith('_Cumulative')]
                        # Find the maximum value
                        max_duration = cumulative_values.max()
                        # Get the column names with the maximum value
                        columns_with_max_duration = cumulative_values[cumulative_values == max_duration].index.tolist()
                        return max_duration, columns_with_max_duration
                    return None, []

                # Execute the function
                max_duration, columns_with_max_duration = get_highest_cumulative_info(df, index)

                # print(f"Highest cumulative duration at index {index}: {max_duration}")
                # print("Column names with this highest cumulative duration:", columns_with_max_duration)
                # Define the lists
                list1 = ['Note1_Cumulative', 'Note2_Cumulative', 'Note3_Cumulative', 'Note4_Cumulative']
                list2 = columns_with_max_duration

                # Retrieve members in list1 that are not in list2
                result = [item for item in list1 if item not in list2]

                # print(result)  # Output: ['Note2_Cumulative']

                def replace_cumulative_notes(lst):
                    replacements = {
                        'Note1_Cumulative': 0,
                        'Note2_Cumulative': 1,
                        'Note3_Cumulative': 2,
                        'Note4_Cumulative': 3
                    }
                    
                    return [replacements.get(item, item) for item in lst]

                # Example usage
                input_list = ['Note1_Cumulative', 'Note2_Cumulative', 'Other', 'Note3_Cumulative', 'Note4_Cumulative']
                input_list = result
                output_list = replace_cumulative_notes(input_list)
                original_list =notes[index + 1]
                desired_length = 4

                # Create a new list with '-' as placeholders
                modified_list = ['-'] * desired_length

                # Insert the original list elements at their respective indexes
                indices = output_list

                # Ensure the indices length matches the original_list length
                for i, item in enumerate(original_list):
                    if i < len(indices):
                        modified_list[indices[i]] = item


                # New value to replace notes[6]
                new_value = modified_list
                # Replace the element at index 6
                notes[index+1] = new_value
                
                # Print the updated list
                aaa = notes.copy()
            else:
                aaa = notes_and_rests_by_time_.copy()
            
        def note_to_solfa(note, key):
            solfa_mappings = {
            'C major': {
                'C': 'd', 'D': 'r', 'E': 'm', 'F': 'f', 'G': 's',
                'A': 'l', 'B': 't', 'C#': 'di', 'D#': 'ri', 'F#': 'fi',
                'G#': 'si', 'A#': 'li'
            },
            'C# major': {
                'C#': 'd', 'D#': 'r', 'E#': 'm', 'F#': 'f', 'G#': 's',
                'A#': 'l', 'B#': 't', 'D': 'ra', 'F': 'fa', 'A': 'la'
            },
            'B minor': {
                'B': 'd', 'C#': 'r', 'D': 'm', 'E': 'f', 'F#': 's',
                'G': 'l', 'A': 't', 'E#': 'fi', 'A#': 'ti', 'C': 'ma'
            },
            'A minor': {
                'A': 'd', 'B': 'r', 'C': 'm', 'D': 'f', 'E': 's',
                'F': 'l', 'G': 't', 'C#': 'mi', 'D#': 'fi', 'G#': 'te'
            },
            'A major': {
                'A': 'd', 'B': 'r', 'C#': 'm', 'D': 'f', 'E': 's',
                'F#': 'l', 'G#': 't', 'D#': 'fi', 'G': 'le'
            },
            'D minor': {
                'D': 'd', 'E': 'r', 'F': 'm', 'G': 'f', 'A': 's',
                'B-': 'l', 'C': 't', 'E-': 'ri', 'A-': 'se'
            },
            'G minor': {
                'G': 'd', 'A': 'r', 'B-': 'm', 'C': 'f', 'D': 's',
                'E-': 'l', 'F': 't', 'A-': 'fi', 'D#': 'si'
            },
            'G major': {
                'G': 'd', 'A': 'r', 'B': 'm', 'C': 'f', 'D': 's',
                'E': 'l', 'F#': 't', 'F': 'fi', 'C#': 'fi'
            },
            'E- major': {
                'E-': 'd', 'F': 'r', 'G': 'm', 'A-': 'f', 'B-': 's',
                'C': 'l', 'D': 't', 'A': 'se', 'B': 'ma'
            },
            'C minor': {
                'C': 'd', 'D': 'r', 'E-': 'm', 'F': 'f', 'G': 's',
                'A-': 'l', 'B-': 't', 'E': 'mi', 'A': 'li'
            },
            'B- major': {
                'B-': 'd', 'C': 'r', 'D': 'm', 'E-': 'f', 'F': 's',
                'G': 'l', 'A': 't', 'D#': 'ra', 'F#': 'si'
            },
            'A- major': {
                'A-': 'd', 'B-': 'r', 'C': 'm', 'D-': 'f', 'E-': 's',
                'F': 'l', 'G': 't', 'D': 'ma', 'E': 'li'
            },
            'D major': {
                'D': 'd', 'E': 'r', 'F#': 'm', 'G': 'f', 'A': 's',
                'B': 'l', 'C#': 't', 'G#': 'ma', 'E#': 'ri'
            },
            'B- minor': {
                'B-': 'd', 'C': 'r', 'D-': 'm', 'E-': 'f', 'F': 's',
                'G-': 'l', 'A-': 't', 'E': 'mi', 'G': 'fi'
            },
            'F minor': {
                'F': 'd', 'G': 'r', 'A-': 'm', 'B-': 'f', 'C': 's',
                'D-': 'l', 'E-': 't', 'B': 'si', 'G-': 'fi'
            },
            'E minor': {
                'E': 'd', 'F#': 'r', 'G': 'm', 'A': 'f', 'B': 's',
                'C': 'l', 'D': 't', 'A#': 'li', 'G#': 'si'
            },
            'F major': {
                'F': 'd', 'G': 'r', 'A': 'm', 'B-': 'f', 'C': 's',
                'D': 'l', 'E': 't', 'C#': 'fi', 'G#': 'le'
            },
            'E major': {
                'E': 'd', 'F#': 'r', 'G#': 'm', 'A': 'f', 'B': 's',
                'C#': 'l', 'D#': 't', 'A#': 'li', 'B#': 'si'
            }
        }
            
            mapping = solfa_mappings[key]
            if note == '-':
                return '-'
            note_name, duration = note.split()
            note_name = note_name[:-1]  # Remove the octave number
            solfa = mapping.get(note_name, note_name)
            return f"{solfa} {duration}"

        notes_ = notes
        # Get the key signature
        key_signature = score.analyze('key')

    #
        def capitalize_first_letter(s):
            if s and s[0].islower():
                return s[0].upper() + s[1:]
            return s

        # Example usage
        strin = str(key_signature)
        capitalized_string = capitalize_first_letter(strin)
        music_key = capitalized_string
#
        print(f"The key of the piece is: {key_signature}")
        solfa_notes = [[note_to_solfa(note, key=capitalized_string) for note in chord] for chord in notes_]
        chords = []
        for chord in solfa_notes:
            chords.append(chord)
        notes = chords

        # Remove sublists with all members being '-'
        filtered_notes = [sublist for sublist in notes if sublist.count('-') < 4]

        filtered_notes
        new_data = filtered_notes.copy()
        data = [(index + 1, *row) for index, row in enumerate(new_data)]

        selected_voice_part = request.GET.get('voice_part')
        if selected_voice_part:
            if selected_voice_part == 'All':
                pass
            else:
                if tempo:
                    tempo_map = {   
                        '1x':1,
                        '3x': 0.60,
                        '2x': 0.85,
                        '-2x': 1.30,
                        '-3x': 1.50,
                    }

                    tempo_num = tempo_map.get(tempo)
                    request.session['tempo_num'] = tempo_num
                else:
                    tempo_num = 1
                voice_map = {
                    'Soprano': 0,
                    'Alto': 1,
                    'Tenor': 2,
                    'Bass': 3
                }

                kogi = selected_voice_part
                voice_num = voice_map.get(kogi)


                # Given music notes
                try:
                    music_notes = notes_
                    # print(music_notes)
                except NameError:
                    music_notes = notes_.copy()
                    print(f'music notes are except {music_notes}')
                note_a = music_notes
                # Remove empty sublists
                filtered_notes = [sublist for sublist in note_a if sublist]
                music_notes = filtered_notes.copy()
                print('Ongoing')
                print(music_notes)
                # Create a stream
                melody = stream.Stream()
                tempo_num = request.session.get('tempo_num', None)
                # Extract and add the first note from each sublist
                for sublist in music_notes:
                    note_str = sublist[voice_num]  # First member of each sublist
                    if note_str == '-':
                        pass
                    else:

                        pitch, duration = note_str.split()  # Split into pitch and duration
                        duration = float(duration)  # Convert duration to float
                        # Create a note object and add it to the stream
                        n = note.Note(pitch)
                        n.quarterLength = duration*tempo_num
                        melody.append(n)
                # Show (and play) the stream
                # melody.show('midi')

                def generate_random_word():
                    letters = string.ascii_lowercase
                    return ''.join(random.choice(letters) for _ in range(4))

                random_word = generate_random_word()
                midi_file_path = f'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\media\\{random_word}.mid'
                # score.write('midi', fp=midi_file_path)
                request.session['random_word'] = random_word
                midi_messages = 1
                path = f"C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\anglican_tunes\\{hymn_number}.xml"
                # score = music21.converter.parse(path)
                melody.write('midi', fp=midi_file_path)
                # hymn_data = fetch_hymn_from_file_ang(hymn_number)


        if hymn_data:
            hymn_data = re.sub(r'(?<!HYMN\s)(\d+)(?=\s)', r'<br><br> \1', hymn_data)
            aa = type(hymn_data)
            # Retrieve the AudioRecord for the given hymn_number and logged-in user, if it exists
            random_letters = None
            # print(f"1this is the randomess {hymn_number}")
            if request.user.is_authenticated:
                # print('hemmy')
                try:
                    audio_record = AudioRecord.objects.get(user=request.user, hymn_number=hymn_number)
                    random_letters = audio_record.random_letters
                    request.session['hymn_number'] = 'am'+hymn_number
                    request.session['random_letters'] = random_letters
                    # print(f"this is the randomess {random_letters}")
                except AudioRecord.DoesNotExist:
                    random_letters = None
                return render(request, 'hymn_display_ang_ang.html', {'hymn_number':hymn_number, 'hymn_data': hymn_data, 'random_letters':random_letters, 'data':data, 'music_key': music_key, 'selected_voice_part': selected_voice_part, 'hymn_numbers': hymn_numbers})
            return render(request, 'hymn_display_ang_ang.html', {'hymn_number':hymn_number, 'hymn_data': hymn_data, 'data':data, 'music_key': music_key, 'selected_voice_part': selected_voice_part, 'hymn_numbers': hymn_numbers})
        else:
            return render(request, 'hymn_display_ang.html', {'error_message': 'Hymn not found.', 'hymn_numbers': hymn_numbers})
    else:
        return render(request, 'hymn_display_ang.html', {'error_message': 'Please select or enter a hymn number.', 'hymn_numbers': hymn_numbers})



def display_hymn_ang_ang(request):
    usernamee = request.session.get('username')
    request.session['joining'] = 'true'
    recording_code = request.session.get('recording_code', None)
    # number_ofhymn = request.session.get('number_ofhymn', None)
    print(f'<<<join_group_recording {recording_code}')
    request.session['recording_code'] = recording_code
    request.session['random_letters'] = recording_code
    def extract_html_file_names(directory):
        # List all files ending with .html
        html_files = [file for file in os.listdir(directory) if file.endswith('.html')]

        # Extract base names without extension
        base_names = [re.match(r'(.+?)\.html', file).group(1) for file in html_files]

        # Sort using a custom key
        def custom_sort_key(name):
            # Split into parts: numbers and non-numbers
            parts = re.split(r'(\d+)', name)
            # Convert numeric parts to integers for correct sorting
            parts = [int(part) if part.isdigit() else part for part in parts]
            return parts

        sorted_base_names = sorted(base_names, key=custom_sort_key)
        return sorted_base_names

    # Example usage:
    directory_path = 'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\lyrics_ang' # Replace with your directory path
    html_files_list = extract_html_file_names(directory_path)
    hymn_numbers = html_files_list  # Define the list of hymn numbers
    number_ofhymn = request.session.get('number_ofhymn', None)
    hymn_number = str(number_ofhymn)
    hymn_number = hymn_number.replace('mhb', '')
    hymn_number = hymn_number.replace('am', '')

##
    if hymn_number is not None:
        # number_hymn = hymn_number.copy()
        print('there is the')
        print(type(hymn_number))
        print((hymn_number))
        # hymn_number = hymn_number.replace('mhb', '')
        # hymn_number = str(hymn_number)
        def generate_random_word():
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(4))

        random_word = generate_random_word()
        midi_file_path = f'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\media\\{random_word}.mid'
        # score.write('midi', fp=midi_file_path)
        request.session['random_word'] = random_word
        request.session['number_ofhymn'] = 'am'+hymn_number

        midi_messages = 1
        path = f"C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\anglican_tunes\\{hymn_number}.xml"
        score = music21.converter.parse(path)
        score.write('midi', fp=midi_file_path)
        hymn_data = fetch_hymn_from_file(hymn_number)
        # Initialize a list to store notes and rests at each point in time
        notes_and_rests_by_time = []
        notes_and_rests_by_time_ = []

        # Get all the notes, chords, and rests from the score
        all_notes = score.flat.getElementsByClass(music21.note.GeneralNote)

        # Create a dictionary to group elements by their starting offset
        elements_by_offset = {}

        # Iterate through the notes, chords, and rests and group them by offset
        for element in all_notes:
            offset = element.offset
            if offset not in elements_by_offset:
                elements_by_offset[offset] = []
            elements_by_offset[offset].append(element)

        # Sort the offsets in ascending order
        sorted_offsets = sorted(elements_by_offset.keys())

        notss = []

        # Iterate through the sorted offsets and collect notes and rests at each point in time
        for offset in sorted_offsets:
            elements = elements_by_offset[offset]
            notes_and_rests = []
            nots=[]

            for element in elements:
                if isinstance(element, music21.note.Note):
                    pitch = element.pitch
                    parts = re.split(r'(\d+)', str(pitch))
                    modified_item = ''.join(parts)
                    pitch = modified_item
                    notes_and_rests.append(f"{pitch}") # {element.duration.quarterLength}
                    nots.append(f"{pitch} {element.duration.quarterLength}")

                elif isinstance(element, music21.chord.Chord):
                    for chord_note in element:
                        chord_pitch = chord_note.pitch
                        parts = re.split(r'(\d+)', str(chord_pitch))
                        modified_item = ''.join(parts)
                        chord_pitch = modified_item
                        notes_and_rests.append(f"{chord_pitch}") # {chord_note.duration.quarterLength}
                        nots.append(f"{chord_pitch} {chord_note.duration.quarterLength}")

                elif isinstance(element, music21.note.Rest):
                    pass
                    # notes_and_rests.append(f"Rest Duration: {element.duration.quarterLength}")

            notes_and_rests_by_time.append(notes_and_rests)
            notes_and_rests_by_time_.append(nots)
            notes = notes_and_rests_by_time_
#
            data = notes
            # Function to extract note and octave
            def get_note_octave(note):
                parts = note.split()
                note_part = parts[0][:-1]
                octave = int(parts[0][-1])
                return note_part, octave

            # Sort each sublist by octave and then by note alphabetically
            sorted_data = [
                sorted(sublist, key=lambda x: (get_note_octave(x)[1], get_note_octave(x)[0]), reverse=True)
                for sublist in data
            ]

            sorted_data
#
            data = sorted_data
            data = notes_and_rests_by_time_
            # Function to remove duplicates if sublist has more than 4 members
            def remove_excess_duplicates(data):
                new_data = []
                for sublist in data:
                    if len(sublist) > 4:
                        seen = set()
                        filtered = []
                        for item in sublist:
                            if item not in seen:
                                seen.add(item)
                                filtered.append(item)
                            elif len(filtered) < 4:
                                filtered.append(item)
                        new_data.append(filtered[:4])
                    else:
                        new_data.append(sublist)
                return new_data

            result = remove_excess_duplicates(data)
            # print(result)
            notes_and_rests_by_time_ = result
            notes_and_rests_by_time_ = result
        # print('fir the check')
        # print(notes_and_rests_by_time_)
        for sublist in notes:
            if len(sublist) < 4:
                # print("A sublist has fewer than 4 items:", sublist)
                # Create DataFrame
                df = pd.DataFrame(notes, columns=['Note1', 'Note2', 'Note3', 'Note4'])

                # Function to extract duration from note string
                def extract_duration(note):
                    if isinstance(note, str):
                        parts = note.split()
                        if len(parts) == 2 and parts[1].replace('.', '').isdigit():
                            return float(parts[1])
                    return 0.0

                # Add cumulative duration columns
                for col in df.columns:
                    df[col + '_Cumulative'] = df[col].apply(extract_duration).cumsum()

                # Display the updated DataFrame
                # print(df)
                # Get the index of the first sublist with less than 4 members
                index = next((i for i, sublist in enumerate(notes) if len(sublist) < 4), None)
                index = index -1
                # print("Index of the first sublist with less than 4 members:", index)
                # Function to check the next sublist after the given index
                def check_next_sublist_length(notes, index):
                    if index + 1 < len(notes):
                        next_sublist = notes[index + 1]
                        return len(next_sublist) < 4
                    return False

                # Check the next sublist
                has_less_than_4_items = check_next_sublist_length(notes, index)
                # print(f"The next sublist after index {index} has less than 4 items: {has_less_than_4_items}")
                # Retrieve the highest cumulative duration and corresponding column names
                def get_highest_cumulative_info(df, index):
                    if index >= 0:
                        # Get the cumulative duration values for the specified row
                        cumulative_values = df.iloc[index, df.columns.str.endswith('_Cumulative')]
                        # Find the maximum value
                        max_duration = cumulative_values.max()
                        # Get the column names with the maximum value
                        columns_with_max_duration = cumulative_values[cumulative_values == max_duration].index.tolist()
                        return max_duration, columns_with_max_duration
                    return None, []

                # Execute the function
                max_duration, columns_with_max_duration = get_highest_cumulative_info(df, index)

                # print(f"Highest cumulative duration at index {index}: {max_duration}")
                # print("Column names with this highest cumulative duration:", columns_with_max_duration)
                # Define the lists
                list1 = ['Note1_Cumulative', 'Note2_Cumulative', 'Note3_Cumulative', 'Note4_Cumulative']
                list2 = columns_with_max_duration

                # Retrieve members in list1 that are not in list2
                result = [item for item in list1 if item not in list2]

                # print(result)  # Output: ['Note2_Cumulative']

                def replace_cumulative_notes(lst):
                    replacements = {
                        'Note1_Cumulative': 0,
                        'Note2_Cumulative': 1,
                        'Note3_Cumulative': 2,
                        'Note4_Cumulative': 3
                    }
                    
                    return [replacements.get(item, item) for item in lst]

                # Example usage
                input_list = ['Note1_Cumulative', 'Note2_Cumulative', 'Other', 'Note3_Cumulative', 'Note4_Cumulative']
                input_list = result
                output_list = replace_cumulative_notes(input_list)
                original_list =notes[index + 1]
                desired_length = 4

                # Create a new list with '-' as placeholders
                modified_list = ['-'] * desired_length

                # Insert the original list elements at their respective indexes
                indices = output_list

                # Ensure the indices length matches the original_list length
                for i, item in enumerate(original_list):
                    if i < len(indices):
                        modified_list[indices[i]] = item


                # New value to replace notes[6]
                new_value = modified_list
                # Replace the element at index 6
                notes[index+1] = new_value
                
                # Print the updated list
                aaa = notes.copy()
            else:
                aaa = notes_and_rests_by_time_.copy()
            
        def note_to_solfa(note, key):
            solfa_mappings = {
            'C major': {
                'C': 'd', 'D': 'r', 'E': 'm', 'F': 'f', 'G': 's',
                'A': 'l', 'B': 't', 'C#': 'di', 'D#': 'ri', 'F#': 'fi',
                'G#': 'si', 'A#': 'li'
            },
            'C# major': {
                'C#': 'd', 'D#': 'r', 'E#': 'm', 'F#': 'f', 'G#': 's',
                'A#': 'l', 'B#': 't', 'D': 'ra', 'F': 'fa', 'A': 'la'
            },
            'B minor': {
                'B': 'd', 'C#': 'r', 'D': 'm', 'E': 'f', 'F#': 's',
                'G': 'l', 'A': 't', 'E#': 'fi', 'A#': 'ti', 'C': 'ma'
            },
            'A minor': {
                'A': 'd', 'B': 'r', 'C': 'm', 'D': 'f', 'E': 's',
                'F': 'l', 'G': 't', 'C#': 'mi', 'D#': 'fi', 'G#': 'te'
            },
            'A major': {
                'A': 'd', 'B': 'r', 'C#': 'm', 'D': 'f', 'E': 's',
                'F#': 'l', 'G#': 't', 'D#': 'fi', 'G': 'le'
            },
            'D minor': {
                'D': 'd', 'E': 'r', 'F': 'm', 'G': 'f', 'A': 's',
                'B-': 'l', 'C': 't', 'E-': 'ri', 'A-': 'se'
            },
            'G minor': {
                'G': 'd', 'A': 'r', 'B-': 'm', 'C': 'f', 'D': 's',
                'E-': 'l', 'F': 't', 'A-': 'fi', 'D#': 'si'
            },
            'G major': {
                'G': 'd', 'A': 'r', 'B': 'm', 'C': 'f', 'D': 's',
                'E': 'l', 'F#': 't', 'F': 'fi', 'C#': 'fi'
            },
            'E- major': {
                'E-': 'd', 'F': 'r', 'G': 'm', 'A-': 'f', 'B-': 's',
                'C': 'l', 'D': 't', 'A': 'se', 'B': 'ma'
            },
            'C minor': {
                'C': 'd', 'D': 'r', 'E-': 'm', 'F': 'f', 'G': 's',
                'A-': 'l', 'B-': 't', 'E': 'mi', 'A': 'li'
            },
            'B- major': {
                'B-': 'd', 'C': 'r', 'D': 'm', 'E-': 'f', 'F': 's',
                'G': 'l', 'A': 't', 'D#': 'ra', 'F#': 'si'
            },
            'A- major': {
                'A-': 'd', 'B-': 'r', 'C': 'm', 'D-': 'f', 'E-': 's',
                'F': 'l', 'G': 't', 'D': 'ma', 'E': 'li'
            },
            'D major': {
                'D': 'd', 'E': 'r', 'F#': 'm', 'G': 'f', 'A': 's',
                'B': 'l', 'C#': 't', 'G#': 'ma', 'E#': 'ri'
            },
            'B- minor': {
                'B-': 'd', 'C': 'r', 'D-': 'm', 'E-': 'f', 'F': 's',
                'G-': 'l', 'A-': 't', 'E': 'mi', 'G': 'fi'
            },
            'F minor': {
                'F': 'd', 'G': 'r', 'A-': 'm', 'B-': 'f', 'C': 's',
                'D-': 'l', 'E-': 't', 'B': 'si', 'G-': 'fi'
            },
            'E minor': {
                'E': 'd', 'F#': 'r', 'G': 'm', 'A': 'f', 'B': 's',
                'C': 'l', 'D': 't', 'A#': 'li', 'G#': 'si'
            },
            'F major': {
                'F': 'd', 'G': 'r', 'A': 'm', 'B-': 'f', 'C': 's',
                'D': 'l', 'E': 't', 'C#': 'fi', 'G#': 'le'
            },
            'E major': {
                'E': 'd', 'F#': 'r', 'G#': 'm', 'A': 'f', 'B': 's',
                'C#': 'l', 'D#': 't', 'A#': 'li', 'B#': 'si'
            }
        }
            
            mapping = solfa_mappings[key]
            if note == '-':
                return '-'
            note_name, duration = note.split()
            note_name = note_name[:-1]  # Remove the octave number
            solfa = mapping.get(note_name, note_name)
            return f"{solfa} {duration}"

        notes_ = notes
        # Get the key signature
        key_signature = score.analyze('key')

    #
        def capitalize_first_letter(s):
            if s and s[0].islower():
                return s[0].upper() + s[1:]
            return s

        # Example usage
        strin = str(key_signature)
        capitalized_string = capitalize_first_letter(strin)
        music_key = capitalized_string
#
        print(f"The key of the piece is: {key_signature}")
        solfa_notes = [[note_to_solfa(note, key=capitalized_string) for note in chord] for chord in notes_]
        chords = []
        for chord in solfa_notes:
            chords.append(chord)
        notes = chords

        # Remove sublists with all members being '-'
        filtered_notes = [sublist for sublist in notes if sublist.count('-') < 4]

        filtered_notes
        new_data = filtered_notes.copy()
        data = [(index + 1, *row) for index, row in enumerate(new_data)]


        selected_voice_part = request.GET.get('voice_part')
        if selected_voice_part:
            if selected_voice_part == 'All':
                pass
            else:


                voice_map = {
                    'Soprano': 0,
                    'Alto': 1,
                    'Tenor': 2,
                    'Bass': 3
                }

                kogi = selected_voice_part
                voice_num = voice_map.get(kogi)


                # Given music notes
                try:
                    music_notes = notes_
                    # print(music_notes)
                except NameError:
                    music_notes = notes_.copy()
                    print(f'music notes are except {music_notes}')
                note_a = music_notes
                # Remove empty sublists
                filtered_notes = [sublist for sublist in note_a if sublist]

                music_notes = filtered_notes.copy()
                # print('Ongoing')
                # print(music_notes)
                # Create a stream
                melody = stream.Stream()
                tempo_num = request.session.get('tempo_num', None)

                # Extract and add the first note from each sublist
                for sublist in music_notes:
                    note_str = sublist[voice_num]  # First member of each sublist
                    if note_str == '-':
                        pass
                    else:

                        pitch, duration = note_str.split()  # Split into pitch and duration
                        duration = float(duration)  # Convert duration to float
                        # Create a note object and add it to the stream
                        n = note.Note(pitch)
                        n.quarterLength = duration*tempo_num
                        melody.append(n)

                # Show (and play) the stream
                # melody.show('midi')

                def generate_random_word():
                    letters = string.ascii_lowercase
                    return ''.join(random.choice(letters) for _ in range(4))

                random_word = generate_random_word()
                midi_file_path = f'C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\media\\{random_word}.mid'
                # score.write('midi', fp=midi_file_path)
                request.session['random_word'] = random_word
                midi_messages = 1
                path = f"C:\\Users\\Asamoah\\Desktop\\kofi\\aseda_a\\adom\\templates\\anglican_tunes\\{hymn_number}.xml"
                # score = music21.converter.parse(path)
                melody.write('midi', fp=midi_file_path)
                # hymn_data = fetch_hymn_from_file_ang(hymn_number)


        if hymn_data:
            hymn_data = re.sub(r'(?<!HYMN\s)(\d+)(?=\s)', r'<br><br> \1', hymn_data)
            aa = type(hymn_data)
            # Retrieve the AudioRecord for the given hymn_number and logged-in user, if it exists
            random_letters = None
            # print(f"1this is the randomess {hymn_number}")
            if request.user.is_authenticated:
                # print('hemmy')
                try:
                    audio_record = AudioRecord.objects.get(user=request.user, hymn_number='am'+hymn_number)
                    random_letters = audio_record.random_letters
                    request.session['random_letters'] = random_letters
                    # print(f"this is the randomess {random_letters}")
                except AudioRecord.DoesNotExist:
                    random_letters = None
                return render(request, 'hymn_display_ang_ang.html', {'usernamee':usernamee,'hymn_number':hymn_number, 'hymn_data': hymn_data, 'random_letters':random_letters, 'data':data, 'music_key': music_key, 'selected_voice_part': selected_voice_part, 'hymn_numbers': hymn_numbers})
            return render(request, 'hymn_display_ang_ang.html', {'usernamee':usernamee,'hymn_number':hymn_number, 'hymn_data': hymn_data, 'data':data, 'music_key': music_key, 'selected_voice_part': selected_voice_part, 'hymn_numbers': hymn_numbers})
        else:
            return render(request, 'hymn_display_ang.html', {'error_message': 'Hymn not found.', 'hymn_numbers': hymn_numbers})
    else:
        return render(request, 'hymn_display_ang.html', {'error_message': 'Please select or enter a hymn number.', 'hymn_numbers': hymn_numbers})

