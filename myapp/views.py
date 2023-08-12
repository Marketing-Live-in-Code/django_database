from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, 'test.html', {
        'title': '測試',
        'data' : '這裡是標題'
    })