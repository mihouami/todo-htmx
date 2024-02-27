from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# VIEW, ADD, UPDATE
@login_required(login_url='user/login/')
def home(request):
    form = TodoForm(request.POST or None)
    todos = Todo.objects.all()
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
                        messages.success(request, 'Todo Updated')
                        todo.save()
                        return redirect('home')
            else:
                messages.warning(request, 'You are not allowed to update this todo')
    context = {'form':form, 'todos':todos}
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
        

