from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from .models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class Task_list_view(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'
class Task_details_view(DetailView):
    model= Task
    template_name = 'details.html'
    context_object_name = 'task'
class Task_update_view(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ['name', 'priority','date']
    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk':self.object.id})
class Task_delete_view(DeleteView):
    model = Task
    template_name = 'delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('cbvhome')

# Create your views here.
def add(request):
    task1 = Task.objects.all()
    if request.method=="POST":
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html', {'task1': task1})
def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')

    return render(request, 'delete.html')
def update(request,id):
    task=Task.objects.get(id=id)
    form1=TodoForm(request.POST or None, instance=task)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request,'edit.html',{'form1':form1,'task':task})