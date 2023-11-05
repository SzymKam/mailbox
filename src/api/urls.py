from rest_framework.routers import SimpleRouter

from .views.email_view import EmailView
from .views.mailbox_view import MailboxView
from .views.template_view import TemplateView

router = SimpleRouter()

router.register(r"mailbox", MailboxView, basename="mailbox")
router.register(r"template", TemplateView, basename="template")
router.register(r"email", EmailView, basename="email")

urlpatterns = router.urls
