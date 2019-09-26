"""定义learning_logs 的URL模式"""
from django.urls import path

from . import views  # 从当前的文件夹导入

urlpatterns = [
    # 主页
    path('', views.index, name='index'),  # r'^$'正则表示将字符串头尾检查

    # 显示所有主题
    path('topics/', views.topics, name='topics'),

    # 特定主题的详细信息
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # 用于添加新主题的网页
    path(r'new_topic/', views.new_topic, name='new_topic'),

    # 用于添加新条目的页面
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # 用于编辑条目的页面
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')

    ]
