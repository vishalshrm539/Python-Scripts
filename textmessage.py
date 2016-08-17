from twilio.rest import TwilioRestClient

account_sid = "AC42e86fe420c875b631303e90444c0826" # Your Account SID from www.twilio.com/console
auth_token  = " 338583e1783b9f4e918cd8a88d110ca8 "  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello Python",
    to="+919999260926",    # Replace with your phone number
    from_="+201528-1574") # Replace with your Twilio number

print(message.sid)
