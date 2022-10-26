from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Coupon
from .forms import CouponApplyForm
from django.views.decorators.http import require_POST


# Create your views here.


@require_POST
def coupon_apply_view(request):
    now = timezone.now()
    coupon_form = CouponApplyForm(request.POST)
    if coupon_form.is_valid():
        code = coupon_form.cleaned_data['code']
    try:
        coupon = Coupon.objects.get(code__iexact=code, valid_from__lte=now, valid_to__gte=now)
        request.session['coupon_id'] = coupon.id
    except:
        request.session['coupon_id'] = None
    return redirect('cart:cart_detail')
