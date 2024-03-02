from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .filters import TodoFilter
import csv
from django.views.decorators.http import require_POST, require_http_methods

# ADD todo with HTMX
@login_required(login_url='user/login/')
@require_POST
def submit_todo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()
        #return and HTML partial
        context = {'todo':todo}
        return render(request, 'home.html#todo-partial', context)



# VIEW, ADD, UPDATE
@login_required(login_url='user/login/')
def home(request):
    todofilter = TodoFilter(request.GET, queryset=Todo.objects.all())
    form = TodoForm(request.POST or None)
    if request.method == 'POST':
        '''
        if 'add' in request.POST:
            if form.is_valid():
                todo = form.save(commit=False)
                todo.user = request.user
                messages.success(request, 'Todo Added')
                todo.save()
                return redirect('home')
        '''
        if 1==1:
            pk = request.POST.get('edit') or request.POST.get('update')
            todo = Todo.objects.get(id=pk)
            if request.user == todo.user:
                if 'update' in request.POST:
                    form = TodoForm(instance=todo)
                else:
                    form = TodoForm(request.POST, instance=todo)
                    if form.is_valid():
                        todo = form.save(commit=False)
                        todo.user = request.user
                        todo.save()
                        return redirect('home')
            else:
                messages.warning(request, 'You are not allowed to update this todo')
    elif request.method == 'GET':
        if 'sort' in request.GET:
            sort_value = request.GET.get('sort')
            order = request.GET.get('order')
            if order == 'desc':
                todofilter = TodoFilter(request.GET, queryset=Todo.objects.order_by('-' + sort_value))
            else:
                todofilter = TodoFilter(request.GET, queryset=Todo.objects.order_by(sort_value)) 
    context = {'form':form, 'todos':todofilter.qs, 'form2':todofilter.form}
    return render(request, 'home.html', context)

# Donwload CSV file
@login_required(login_url='user/login/')
def download_csv(request):
    filter = TodoFilter(request.GET, queryset=Todo.objects.all()).qs
    # Create a CSV file in memory
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="table_data.csv"'
    # Write table data to CSV
    writer = csv.writer(response)
    # Write header row
    header_row = [field.name for field in Todo._meta.fields]  # Get field names
    writer.writerow(header_row)
    # Write data rows
    for obj in filter:
        row = [getattr(obj, field.name) for field in Todo._meta.fields]
        writer.writerow(row)
    return response


'''
# MARK COMPLETE VIEW
@login_required(login_url='user/login/')
def complete(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.user == todo.user:
        if todo.is_completed == True:
            todo.is_completed = False
        else:
            todo.is_completed = True
        todo.save()
    else:
        messages.warning(request, 'You are not allowed to update this todo')
    return redirect('home')
'''

# MARK COMPLETE VIEW USING HTMX
@login_required(login_url='user/login/')
@require_POST
def complete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if todo.is_completed == True:
        todo.is_completed = False
    else:
        todo.is_completed = True
    todo.save()
    context = {'todo':todo}
    return render(request, 'home.html#todo-partial', context)


'''
# DELETE VIEW
@login_required(login_url='user/login/')
def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.user == todo.user:
        todo.delete()
        messages.success(request, 'Todo deleted with success')
    else:
        messages.warning(request, 'You are not allowed to delete this todo')
    return redirect('home')
'''

# DELETE VIEW WITH HTMX
@login_required(login_url='user/login/')
@require_http_methods(['DELETE'])
def delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.delete()
    response = HttpResponse(status=204)
    response['HX-Trigger'] = 'delete'
    return response

# Update VIEW WITH HTMX
@login_required(login_url='user/login/')
@require_POST
def update_one(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    form = TodoForm(instance=todo)
    context = {'form':form,'todo':todo}
    return render(request, 'home.html#todo-partial_update', context)

# Update VIEW WITH HTMX
@login_required(login_url='user/login/')
@require_POST
def update_two(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    form = TodoForm(request.POST, instance=todo)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()
    context = {'form':form,'todo':todo}
    return render(request, 'home.html#todo-partial', context)



