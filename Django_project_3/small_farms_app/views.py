from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from .models import InfrustructureItem, InfrustructureType, ManagmentLog, LogAction

# Views and Create Functions

class IndexView(TemplateView):
    template_name = 'small_farms_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_list'] = {
            'item_view': ItemView.as_view(),
            'infrastructure_type_view': TypeView.as_view(),
            'log_action_view': LogActionView.as_view(),
            'management_log_view': ManagementLogView.as_view(),
        }
        return context

class ItemView(View):
    template_name = 'small_farms_app/Item.html'

    def get(self, request, *args, **kwargs):
        queryset = InfrustructureItem.objects.all()
        context = {'items_list': queryset}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        InfrustructureItem.objects.create(name=name)
        return redirect('item_view')

class TypeView(View):
    template_name = 'small_farms_app/InfrustructureType.html'

    def get(self, request, *args, **kwargs):
        queryset = InfrustructureType.objects.all()
        context = {'types_list': queryset}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        InfrustructureType.objects.create(name=name)
        return redirect('infrastructure_type_view')

class ManagementLogView(View):
    template_name = 'small_farms_app/ManagmentLog.html'

    def get(self, request, *args, **kwargs):
        queryset = ManagmentLog.objects.all()
        context = {'logs_list': queryset}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        condition = request.POST.get('condition')
        ManagmentLog.objects.create(condition=condition)
        return redirect('management_log_view')

class LogActionView(View):
    template_name = 'small_farms_app/LogAction.html'

    def get(self, request, *args, **kwargs):
        queryset = LogAction.objects.all()
        context = {'actions_list': queryset}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        sort_order = request.POST.get('sort_order')
        LogAction.objects.create(sort_order=sort_order)
        return redirect('log_action_view')
    
class DeleteItemView(View):
    def post(self, request, item_id):
        item = get_object_or_404(InfrustructureItem, pk=item_id)
        item.delete()
        return redirect('infrastructure_item_view')

class DeleteTypeView(View):
    def post(self, request, type_id):
        type = get_object_or_404(InfrustructureType, pk=type_id)
        type.delete()
        return redirect('infrastructure_type_view')

class DeleteLogView(View):
    def post(self, request, log_id):
        log = get_object_or_404(ManagmentLog, pk=log_id)
        log.delete()
        return redirect('managment_log_view')

class DeleteActionView(View):
    def post(self, request, action_id):
        action = get_object_or_404(LogAction, pk=action_id)
        action.delete()
        return redirect('log_action_view')

# Detail Functions

class DetailViews(TemplateView):
    template_name = 'small_farms_app/Details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detail_list'] = {
            'item_detail': ItemDetailView.as_view(),
            'type_detail': TypeDetailView.as_view(),
            'log_action_detail': LogActionDetailView.as_view(),
            'management_log_detail': ManagementLogDetailView.as_view(),
        }
        return context

class ItemDetailView(View):
    template_name = 'small_farms_app/item_detail.html'

    def get(self, request, item_id, *args, **kwargs):
        item = get_object_or_404(InfrustructureItem, pk=item_id)
        context = {'items_list': item}
        return render(request, self.template_name, context)

class TypeDetailView(View):
    template_name = 'small_farms_app/type_detail.html'

    def get(self, request, type_id, *args, **kwargs):
        type = get_object_or_404(InfrustructureType, pk=type_id)
        context = {'types_list': type}
        return render(request, self.template_name, context)

class ManagementLogDetailView(View):
    template_name = 'small_farms_app/managment_log_detail.html'

    def get(self, request, log_id, *args, **kwargs):
        log = get_object_or_404(ManagmentLog, pk=log_id)
        context = {'logs_list': log}
        return render(request, self.template_name, context)

class LogActionDetailView(View):
    template_name = 'small_farms_app/log_action_detail.html'

    def get(self, request, action_id, *args, **kwargs):
        action = get_object_or_404(LogAction, pk=action_id)
        context = {'actions_list': action}
        return render(request, self.template_name, context)


