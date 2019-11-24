from django.contrib import messages
from django.contrib.messages import get_messages
from django.shortcuts import redirect, render
from .forms import DimensionForm

from matrix_calculator.Calculations import calculator

import numpy as np

def get_matrix_dimensions(request):
    if request.method == 'POST':

        form = DimensionForm(request.POST)
        if form.is_valid():
            ff_number = form.cleaned_data['first_number']
            ss_number = form.cleaned_data['second_number']
            
           
            return redirect(enter_matrix_numbers, f_number = ff_number, s_number = ss_number)
    
    else:
        form = DimensionForm()

    return render(request, 'home.html', {'form': form})
    
def enter_matrix_numbers(request, f_number, s_number):
    range_first = range(int(f_number))
    range_second = range(int(s_number))

    return render(request, 'enter_number.html', {'f_number': f_number, 's_number': s_number, 
                           'range_first': range_first, 'range_second': range_second})

def calculate(request):
    if request.method == 'POST':
        
        content = request.POST.dict()
        field_values = calculator.MatrixCalculator(content)
        
        dimensions = field_values.dimensions_to_normal_form()
        array_numbers = field_values.numbers_to_normal_form()
        
        range_first = range(dimensions[0] + 1)
        range_second = range(dimensions[1] + 1)

        if request.POST.get('determinant'):
            operation = 'determinant'
            try: 
                result = field_values.Determinant(array_numbers, dimensions)
            except np.linalg.LinAlgError as error:
                messages.add_message(request, messages.ERROR, error)
                result = ''

        elif request.POST.get('rank'):
            operation = 'rank'
            result = field_values.Rank(array_numbers, dimensions)
    
    else:
        print('')
        
        
    return render(request, 'enter_number.html', {'result': result, 'operation': operation, 
                                                'f_number': dimensions[0] + 1, 's_number': dimensions[1] + 1, 
                                                'range_first': range_first, 'range_second': range_second})
