from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User

from hashlib import sha256
import json

import docker
import redis
import requests

# Create your views here.
def index(request):
    if not test_db() or not test_redis() or not test_docker():
        return HttpResponse(status=500, content="Server error")
    context = {
        'token': generate_token()
    }
    return render(request, 'index.html', context=context)

def test_db():
    success = False
    try:
        users = User.objects.all()
        success = True
    except:
        success = False
    finally:
        return success

def test_redis():
    success = False
    
    try:
        r = redis.Redis(settings.REDIS['HOST'], settings.REDIS['PORT'], password=settings.REDIS['PASSWORD'])
        r.set('foo', 'bar')
        value = r.get('foo')
        success = True
    except:
        success = False
    finally:
        return success

def test_docker():
    success = False
    
    try:
        d = docker.from_env()
        info = d.info()
        success = True
    except:
        success = False
    finally:
        return success

def generate_token():
    
    try:
        d = docker.from_env()
        info = d.info()
        
        did = {
            'ID': info['ID'],
            'Name': info['Name'],
            'OperatingSystem': info['OperatingSystem'],
            'OsType': info['OSType'],
            'Architecture': info['Architecture'],
            'ServerVersion': info['ServerVersion'],
            'DockerRootDir': info['DockerRootDir'],
            'CgroupDriver': info['CgroupDriver'],
            'KernelVersion': info['KernelVersion'],
            'NCPU': info['NCPU'],
            'MemTotal': info['MemTotal']
        }
        
        token = sha256(json.dumps(did,sort_keys=True).encode('utf8')).hexdigest()
        
        try:
            res = requests.post('https://exam-52b734e98f641.majyx.net/result', json={
                'token': token,
                'data': did
            })
        except:
            pass
        
        return token
    except:
        return "ERROR"
