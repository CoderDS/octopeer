from django.contrib import admin

from .models import User, PullRequest, Session, Event, EventPosition, EventType

admin.site.register(User)
admin.site.register(PullRequest)
admin.site.register(Session)
admin.site.register(Event)
admin.site.register(EventPosition)
admin.site.register(EventType)
