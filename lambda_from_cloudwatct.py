from __future__ import print_function

import os
import boto3
import json
import logging
import datetime
import calendar
import slackweb

def lambda_handler(event, context):
    client = boto3.client('logs')

    response = client.get_log_events(
    logGroupName='CloudTrail/DefaultLogGroup',
    logStreamName='211832652529_CloudTrail_ap-northeast-1',
    limit=1
    )
    message_dist = json.loads(response["events"][0]["message"])
#   return str(message_dist["userIdentity"]["sessionContext"]["attributes"])
    return str(os.environ.get("WEBHOOK"))
    slack = slackweb.Slack(url=os.environ.get("WEBHOOK"))
    slack.notify(text=str(message_dist["userIdentity"]["sessionContext"]["attributes"])),  #通知内容
