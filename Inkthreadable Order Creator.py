import requests
import hashlib
import json
import hmac

## Example of how to connect to the Print on Demand provider Inkthreadable in the UK

## Build an order array
## Use the inkthreadable API documentation for explanations on the individual elements within the array

order = {
 "brandName": "",
 "comment": """<a href="/">Test order.</a>""",
 "external_id": "",
 "shipping_address": {
  "firstName": "",
  "lastName": "",
  "address1": "",
  "city": "",
  "county": "",
  "postcode": "",
  "country": "",
  "phone1": "",
 },
 "shipping": {
  "shippingMethod": ""
 },
 "items": [
  { "pn":  "", "title": "", "retailPrice": "", "quantity": "", "description": "", "brandName": "", "designs": {"front": "",}, "mockups":{"front": ""}}
 ]
}

## Create a JSON dump of the array

data = str(json.dumps(order))

## Add your API Key

key = ''

## Validate the call with a signature

combo = data + key
combo = combo.encode()
signature = hashlib.sha1(combo).hexdigest()

## Add your Inkthreadable App ID

url = 'https://www.inkthreadable.co.uk/api/orders.php?AppId=APP-YOUR ID'

headers = {"Content-Type": "application/json", "Accept": "application/json", "Content-Length": str(len(combo)),}

## Print the result of your test order

print(requests.post(url + '&Signature=' + str(signature), data=data, headers=headers).json())