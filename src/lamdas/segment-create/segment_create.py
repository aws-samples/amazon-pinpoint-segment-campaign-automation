import logging
import os

import boto3

client = boto3.client("pinpoint")
appid = os.environ.get("PINPOINT_PROJECT_ID")


def lambda_handler(event, context):
    interest = event["interest"]
    product_name = event["product_name"]
    product_link = event["product_link"]
    segment_name = "segment" + "_" + interest + "_" + product_name
    log_level = str(os.environ.get("LOG_LEVEL")).upper()
    if log_level not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        log_level = "ERROR"
    logging.getLogger().setLevel(log_level)
    logging.info(event)
    response = client.create_segment(
        ApplicationId=appid,
        WriteSegmentRequest={
            "Dimensions": {
                "UserAttributes": {
                    "interests": {
                        "AttributeType": "CONTAINS",
                        "Values": [
                            interest,
                        ],
                    }
                },
                "Behavior": {
                    "Recency": {"Duration": "DAY_30", "RecencyType": "ACTIVE"}
                },
            },
            "Name": segment_name,
        },
    )
    logging.info(response)
    return {
        "SegmentId": response["SegmentResponse"]["Id"],
        "product_name": product_name,
        "interest": interest,
        "product_link": product_link,
    }
