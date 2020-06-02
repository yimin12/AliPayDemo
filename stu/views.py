from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from utils.AliPay import AliPay


def index_veiw(request):
    return render(request, 'index.html')


alipay = AliPay(appid='2016091100486702', app_notify_url='http://127.0.0.1:8000/stu/checkPay/',
                app_private_key_path='stu/keys/my_private_key.txt',
                alipay_public_key_path='stu/keys/alipay_public_key.txt',
                return_url='http://127.0.0.1:8000/stu/checkPay/', debug=True)

# 获取支付二维码界面
def pay_view(request):
    import uuid
    # 获取请求参数
    m = request.POST.get('m', 0)
    # 获取扫码支付请求参数
    params = alipay.direct_pay(subject="YIMIN Market", out_trade_no=uuid.uuid4().get_hex(), total_amount=str(m))
    # 获取扫码支付请求地址
    url = alipay.gateway + "?" + params
    return HttpResponseRedirect(url)

def checkPay_view(request):
    # 获取所有请求参数
    params = request.GET.dict()
    # 移除并获取sign参数的值
    sign = params.pop('sign')
    # 校验是否成功支付
    if alipay.verify(params, sign):
        return HttpResponse("支付成功！")
    return HttpResponse("支付失败！")
