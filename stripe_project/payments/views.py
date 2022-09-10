import os
import stripe

from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from .models import Item


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request, item_id):
    if request.method == 'GET':
        item = Item.objects.filter(id=item_id).first()
        item_price = item.price * 100
        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                        'description': item.description
                    },
                    'unit_amount_decimal': item_price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://example.com/success',
            cancel_url='https://example.com/cancel',
        )
        return JsonResponse({'sessionId': session['id']})

@csrf_exempt
def item_detail(request, item_id):
    if request.method == 'GET':
        item = Item.objects.filter(id=item_id).first()
        context = {
            'item': item,
        }

        return render(request, 'payments/item_detail.html', context=context)
