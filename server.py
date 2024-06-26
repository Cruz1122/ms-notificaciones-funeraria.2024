from flask import Flask, request
import os
import boto3
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Hola, soy Flask"


@app.route("/sms", methods=["POST"])
def sms():
    data = request.get_json()
    destination = data["destination"]
    message = data["message"]
    print(destination)
    print(message) 
    # Create an SNS client
    client = boto3.client(
        "sns",
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
        region_name=os.environ.get("AWS_REGION"),
    )

    # Send your sms message.
    client.publish(PhoneNumber=destination, Message=message)
    return "OK"

@app.route("/sms-2fa", methods=["POST"])
def sms_2fa():
    data = request.get_json()
    name = data["name"]
    destination = data["destination"]
    message = "Hola, "+ name+". \n" + data["message"]
    print(destination)
    print(message)
    # Create an SNS client
    client = boto3.client(
        "sns",
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
        region_name=os.environ.get("AWS_REGION"),
    )

    # Send your sms message.
    client.publish(PhoneNumber=destination, Message=message)
    return "OK"


# based on the code above, build the email api method using AWS SES
@app.route("/email", methods=["POST"])
def email():
    data = request.get_json()
    destination = data["destination"]
    message = data["message"]
    subject = data["subject"]
    # Create an SES client
    client = boto3.client(
        "ses",
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
        region_name=os.environ.get("AWS_REGION"),
    )
    # send the email message using the client
    response = client.send_templated_email(
        Destination={
            "ToAddresses": [
                destination,
            ],
        },
        Template="AWS-SES-Email-Without-Name",
        TemplateData='{"message":"'
        + message
        + '", "subject":"'
        + subject
        + '"}',
        Source="funerariadigitaluc@gmail.com",
    )
    return response

@app.route("/email-2fa", methods=["POST"])
def email_2fa():
    data = request.get_json()
    destination = data["destination"]
    name = data["name"]
    message = data["message"]
    subject = data["subject"]

    # Create an SES client
    client = boto3.client(
        "ses",
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
        region_name=os.environ.get("AWS_REGION"),
    )
    # send the email message using the client
    response = client.send_templated_email(
        Destination={
            "ToAddresses": [
                destination,
            ],
        },
        Template="AWS-SES-Email-With-Name",
        TemplateData='{"message":"'
        + message
        + '", "subject":"'
        + subject
        + '", "name":"'
        + name
        + '"}',
        Source="funerariadigitaluc@gmail.com",
    )
    return response

if __name__ == "__main__":
    app.run(debug=True, port=5000)
