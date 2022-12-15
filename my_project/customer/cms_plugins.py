from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import CustomerMaster, CustomerPluginModel
from django.utils.translation import gettext as _


@plugin_pool.register_plugin  # register the plugin
class CustomerPlugin(CMSPluginBase):
    model = CustomerPluginModel  # model where plugin data are saved
    module = _("Core Plugins")
    name = _("Customer Plugin")  # name of the plugin in the interface
    render_template = "customerplugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        if instance.is_active:
            context.update({'customers': CustomerMaster.objects.filter(is_active=True)})
        else:
            context.update({'customers': CustomerMaster.objects.all()})
        return context