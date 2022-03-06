from slack_common_notice.aws_sns import subscribe
from slack_common_notice.notice import Notice


def lambda_handler(event, context):
    if subscribe(event):
        return
    Notice(event).send()
