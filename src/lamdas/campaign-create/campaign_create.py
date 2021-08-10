import logging
import os

import boto3

client = boto3.client("pinpoint")


def lambda_handler(event, context):
    interest = event["interest"]
    segment_id = event["SegmentId"]
    product_name = event["product_name"]
    product_link = event["product_link"]
    formatted_prod_link = ('"' + {} + '"').format(product_link)
    from_email = os.environ.get("FROM_ADDRESS")
    campaign_name = "campaign" + "_" + interest + "_" + product_name
    appid = os.environ.get("PINPOINT_PROJECT_ID")
    log_level = str(os.environ.get("LOG_LEVEL")).upper()
    if log_level not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        log_level = "ERROR"
    logging.getLogger().setLevel(log_level)
    logging.info(event)

    response = client.create_campaign(
        ApplicationId=appid,
        WriteCampaignRequest={
            "MessageConfiguration": {
                "EmailMessage": {
                    "Body": "Hello we have a new product arrival that you might be interested in.",
                    "FromAddress": from_email,
                    "HtmlBody": """<html>
                          <head></head>
                          <body>
                            <h1> Hello, are you interested in """
                    + interest
                    + """? </h1>
                            <p> There is a new product arrival: """
                    + product_name
                    + """ </p>
                            <a href="""
                    + formatted_prod_link
                    + """>Click here to view """
                    + product_name
                    + """ on our website!</a>
                            <p> Hope to see you back soon! </p>
                          </body>
                          </html>
                          """,
                    "Title": "New Product Arrival: " + product_name,
                }
            },
            "Name": campaign_name,
            "Schedule": {
                "Frequency": "ONCE",
                "IsLocalTime": False,
                "StartTime": "IMMEDIATE",
                "Timezone": "UTC+01",
            },
            "SegmentId": segment_id,
        },
    )

    logging.info(response)
    return {
        "CampaignId": response["CampaignResponse"]["Id"],
        "SegmentId": response["CampaignResponse"]["SegmentId"],
        "CampaignStatus": response["CampaignResponse"]["State"]["CampaignStatus"],
        "interest": event["interest"],
        "product_name": event["product_name"],
        "product_link": event["product_link"],
    }
