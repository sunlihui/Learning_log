"""定义learning_logs的URL模式"""

from django.conf.urls import url

from django.contrib.auth.views import LoginView

urlpatterns = [
    # 主页
    url(r'^login/$', LoginView.as_view(template_name='users/login.html')),

]