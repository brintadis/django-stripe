from django.urls import path

from .views import create_checkout_session, item_detail, stripe_config


urlpatterns = [
    path('config/', stripe_config, name='stripe_config'),
    path("buy/<int:item_id>", create_checkout_session, name='buy_item'),
    path("item/<int:item_id>", item_detail, name='item_detail')
]
