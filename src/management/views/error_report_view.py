import os

from django.utils import timezone

from ..models import Mailbox


class ReportBug:
    @staticmethod
    def save_log_attempt_success(mailbox: Mailbox, attempt: int) -> None:
        ReportBug.__save_into_file(mailbox=mailbox, attempt=attempt, result="Email send successfully")

    @staticmethod
    def save_log_attempt_failed(mailbox: Mailbox, attempt: int) -> None:
        ReportBug.__save_into_file(mailbox=mailbox, attempt=attempt, result="Error when sending email")

    @staticmethod
    def __save_into_file(mailbox: Mailbox, attempt: int, result: str) -> None:
        # file_dir = "src/logs/"
        # if not os.path.exists(file_dir):
        #     os.makedirs(file_dir)

        with open(os.path.join("email_log.log"), "a") as file:
            file.write(
                f"{result} from: {mailbox.host};"
                f"email: {mailbox.email_from}. Attempt numer {attempt}, at {timezone.now()} \n"
            )
