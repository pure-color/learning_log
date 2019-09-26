from django.contrib import admin

# 向管理网站注册Topic,这时可以通过django在网页管理
from learning_logs.models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)
