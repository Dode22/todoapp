from django.shortcuts import render
from .models import Todolist, Category

# Create your views here.

def index(request): # the index view
    todo_items = Todolist.objects.all() # querying all todo items with the object manager
    categories = Category.objects.all() # getting all categories with object manager
    if request.method == "POST": # checking if the request method is a POST
        if "taskAdd" in request.POST: # checking if there is a request to add a todo
            title = request.POST["description"] # title
            date = str(request.POST["date"]) # date
            category = request.POST["category_select"] # category
            content = title + "--" + date + " " + category # content
            Todo = Todolist(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save() # saving the todo
            
        if "taskDelete" in request.POST: # checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"] # checked todo_items to be deleted
            for todo_id in checkedlist:
                todo = Todolist.objects.get(id=int(todo_id)) # getting todo id
                todo.delete() # deleting todo 
    return render(request, "todolist/index.html", {"todos": todo_items, "categories":categories})