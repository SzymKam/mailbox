from django.utils import timezone

from ..models import Mailbox


class ReportBug:
    def __init__(self, mailbox: Mailbox, attempt: int) -> None:
        self._mailbox = mailbox
        self._attempt = attempt

    def _save_bug_into_file(self):
        with open("logs/email.log", "w") as file:
            file.write(
                f"Connection error when sending email from: {self._mailbox.host}; "
                f"email: {self._mailbox.email_from}. Attempt numer {self._attempt}, at {timezone.now()}"
            )
