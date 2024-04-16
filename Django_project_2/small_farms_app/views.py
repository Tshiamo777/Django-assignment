from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import InfrustructureItem, InfrustructureType, ManagmentLog, LogAction


#VIEWS AND CREATE FUNCTIONS.

def index(request):
    view_functions = {
        'item_view': item_view,
        'infrastructure_type_view': type_view,
        'log_action_view': log_action_view,
        'management_log_view': managment_log_view,
    }
    context = {'view_list': view_functions}
    
    return render(request, 'small_farms_app/index.html', context)

def item_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        new_item = InfrustructureItem.objects.create(name=name)
        return redirect('infrastructure_item_view')  # Redirect to the same view after creating
    
    queryset = InfrustructureItem.objects.all()

    processed_items = queryset  # Placeholder, replace this with your actual processing logic

    context = {'items_list': processed_items}
    return render(request, 'small_farms_app/Item.html', context)

def type_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        new_type = InfrustructureType.objects.create(name=name)
        return redirect('infrastructure_type_view')  # Redirect to the same view after creating

    infrustructure_type_objects = InfrustructureType.objects.all()

    processed_types = infrustructure_type_objects

    context = {'types_list' : processed_types}
    return render(request, 'small_farms_app/InfrustructureType.html', context)

def managment_log_view(request):
    if request.method == 'POST':
        condition = request.POST.get('condition')
        new_log = ManagmentLog.objects.create(condition=condition)
        return redirect('managment_log_view')  # Redirect to the same view after creating

    managment_log_objects = ManagmentLog.objects.all()

    processesed_logs = managment_log_objects

    context = {'logs_list' : processesed_logs}
    return render(request, 'small_farms_app/ManagmentLog.html', context)

def log_action_view(request):
    if request.method == 'POST':
        sort_order = request.POST.get('sort_order')
        new_action = LogAction.objects.create(sort_order=sort_order)
        return redirect('log_action_view')  # Redirect to the same view after creating
    
    log_action_objects = LogAction.objects.all()

    processed_actions = log_action_objects

    context = {'actions_list' : processed_actions}
    return render(request, 'small_farms_app/LogAction.html', context)

#DELETE FUNCTIONS

def delete_item(request, item_id):
    item = get_object_or_404(InfrustructureItem, pk=item_id)
    item.delete()
    return redirect('infrastructure_item_view')  # Redirect back to item view after deletion

def delete_type(request, type_id):
    type = get_object_or_404(InfrustructureType, pk=type_id)
    type.delete()
    return redirect('infrastructure_type_view')  # Redirect back to type view after deletion

def delete_log(request, log_id):
    log = get_object_or_404(ManagmentLog, pk=log_id)
    log.delete()
    return redirect('managment_log_view')  # Redirect back to log view after deletion

def delete_action(request, action_id):
    action = get_object_or_404(LogAction, pk=action_id)
    action.delete()
    return redirect('log_action_view')  # Redirect back to action view after deletion


#DETAIL FUNCTIONS
def Details_index(request):
    detail_functions = {
        'item_detail': item_detail,
        'type_detail': type_detail,
        'log_action_detail': log_action_detail,
        'management_log_detail': managment_log_detail,
    }
    context = {'detail_list': detail_functions}
    
    return render(request, 'small_farms_app/Details.html', context)

def item_detail(request, item_id):
    item = get_object_or_404(InfrustructureItem, pk=item_id)
    
    context = {'items_list': item}

    return render(request, 'small_farms_app/item_detail.html', context )

def type_detail(request, type_id):
    type = get_object_or_404(InfrustructureType, pk=type_id)

    context = {'types_list': type}

    return render(request, 'small_farms_app/type_detail.html', context)

def managment_log_detail(request, log_id):
    log = get_object_or_404(ManagmentLog, pk=log_id)

    context = {'logs_list': log}

    return render(request, 'small_farms_app/managment_log_detail.html', context)

def log_action_detail(request, action_id):
    action = get_object_or_404(LogAction, pk=action_id)

    context = {'actions_list': action}
    return render(request, 'small_farms_app/log_action_detail.html', context)

