import datetime
import boto3
import pprint

def lambda_handler(event, context):
  client = boto3.client('iam')
  response = client.list_users()
  jsonObj = [""] * len(response["Users"])
  i = 0
  dt_now = datetime.datetime.now()
  print(dt_now)
  for user in response["Users"]:
    jsonObj[i] = {}
    jsonObj[i]["UserName"] = getValueFromUser(user, "UserName")
    jsonObj[i]["CreateDate"] = getValueFromUser(user, "CreateDate")
    jsonObj[i]["PasswordLastUsed"] = getValueFromUser(user, "PasswordLastUsed")
    print(response['Users'][i]['CreateDate'])
    pprint.pprint(user["CreateDate"])
    i = i + 1

def getValueFromUser(user, key):
  try:
      return str(user[key])
  except (KeyError):
      return "None"
