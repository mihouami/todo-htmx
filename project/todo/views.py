from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm, TodoFilterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .filters import TodoFilter


# VIEW, ADD, UPDATE
@login_required(login_url='user/login/')
def home(request):
    #description = request.GET.get('todo')
    #todos = Todo.objects.all()
    #if description:
    #    todos = Todo.objects.filter(description__icontains=description)
    #form2 = TodoFilterForm() 

    todofilter = TodoFilter(request.GET, queryset=Todo.objects.all())
    form = TodoForm(request.POST or None)
    if request.method == 'POST':
        if 'add' in request.POST:
            if form.is_valid():
                todo = form.save(commit=False)
                todo.user = request.user
                messages.success(request, 'Todo Added')
                todo.save()
                return redirect('home')
        else:
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
        

