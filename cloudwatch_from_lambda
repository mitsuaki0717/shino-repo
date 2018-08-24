from __future__ import print_function

import boto3
import json
import logging
import datetime
import calendar
import slackweb

def lambda_handler(event, context):
    client = boto3.client('logs')
    #response = client.describe_log_groups(
    #    logGroupNamePrefix='CloudTrail/DefaultLogGroup',
    #    limit=2
    #)
    response = client.get_log_events(
    logGroupName='CloudTrail/DefaultLogGroup',
    logStreamName='211832652529_CloudTrail_ap-northeast-1',
    limit=1
    )
    return str(response["events"])
    slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
    slack.notify(text="testです" + (response["events"])),  #通知内容
