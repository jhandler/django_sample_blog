from django.shortcuts import render

# Create your views here.
#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from datetime import datetime, timedelta
 
from django.db.models import Q
 
from django.contrib.auth.models import User
 
from blog.models import *
 
# Create your views here.
@never_cache
def index(request):
        post_list = Blog_Post.objects.all()
       
        template = loader.get_template('blog/index.html')
        context = RequestContext(request, {
                'post_list': post_list,
        })
        return HttpResponse(template.render(context))