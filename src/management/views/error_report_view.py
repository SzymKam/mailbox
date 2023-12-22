import os

from django.utils import timezone

from ..models import Mailbox


class ReportBug:
    def __init__(self, mailbox: Mailbox, attempt: int) -> None:
        self.error = None
        self.mailbox = mailbox
        self.attempt = attempt
        self.result: str = ""

    def save_log_attempt_success(self) -> None:
        self.result = "Email send successfully"
        self.__save_into_file()

    def save_log_attempt_failed(self, error: Exception) -> None:
        self.error = error
        self.result = "Error when sending email"
        self.__save_into_file()

    def __save_into_file(self) -> None:
        file_dir = "src/logs/"
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

        with open(os.path.join(file_dir, "email_log.log"), "a") as file:
            file.write(
                f"{self.result} from: {self.mailbox.host};"
                f"email: {self.mailbox.email_from}. Attempt numer {self.attempt}, at {timezone.now()} \n"
            )
            if self.error:
                file.write(f"Error: {self.error}\n")
