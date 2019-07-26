from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .models import *
import json
from .forms import StoreForm

def main(request):
    # post = MachineID.objects.all()
    return render(request, 'main.html', {})

# Json Context 출력
def Result(status, msg, data=None):
    result = {}
    result['status'] = status
    result['message'] = msg
    result['data'] = data
    return result

@require_http_methods(["POST"])
def checkMachineAPI(request):
    # MachineID 가져오기
    machineID = request.POST.get('machineID', None)

    # MachineID 존재 여부 확인
    try:
        user = MachineID.objects.get(uuid=machineID)
        context = Result("success", user.nickname +"님, 환영합니다.")
    except:
        context = Result("error", "처음 접속 유저입니다.")

    return HttpResponse(json.dumps(context), content_type="application/json")


@require_http_methods(["POST"])
def createMachineAPI(request):
    # MachineID 가져오기
    machineID = request.POST.get('machineID', None)
    nickname = request.POST.get('nickname', None)
    # MachineID 존재 여부 확인
    
    try:
        # print(machineID)
        # print(nickname)
        user = MachineID.objects.create(uuid=machineID, nickname=nickname)
        print(user)
        context = Result("success", user.nickname +"님, 환영합니다.")
    except:
        context = Result("error", "이미 존재하는 uuid 입니다.")

    return HttpResponse(json.dumps(context), content_type="application/json")


def test(request):
    testform = StoreForm()
    print(request.POST["menu"])
    return render(request, 'a.html', {'testform': testform})

def detail(request, pk):
    post = Store.objects.get(pk=pk)
    return render(request, 'detail.html', {'s_post':post})

def category(request):
    post = Store.objects.all()
    return render(request, 'category.html', {'form': post})

def g_category(request):
    gun_post = Store.objects.filter(tag='사격')
    return render(request, 'category.html', {'form': gun_post})

def r_category(request):
    room_post = Store.objects.filter(tag='방탈출')
    return render(request, 'category.html', {'form': room_post})

def f_category(request):
    fish_post = Store.objects.filter(tag='낚시')
    return render(request, 'category.html', {'form': fish_post})

def b_category(request):
    break_post = Store.objects.filter(tag='레이지룸')
    return render(request, 'category.html', {'form': break_post})

def write(request):
    if request.method == 'POST':
        w_form = StoreForm(request.POST, request.FILES)

        if w_form.is_valid():
            post = w_form.save(commit = False)
        # Post.objects.create(title=request.POST['post_title_text'], content=request.POST.get('fields', ''))
            post.save()
            return redirect('API:category')
    else:
        w_form = StoreForm()
        return render(request, 'review.html', {'w_form':w_form})