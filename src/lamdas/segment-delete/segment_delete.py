import logging
import os
import time

import boto3

client = boto3.client("pinpoint")


def lambda_handler(event, context):
    global log_level  # TODO: undefined at module level, can we remove?
    log_level = str(os.environ.get("LOG_LEVEL")).upper()
    if log_level not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        log_level = "ERROR"
    logging.getLogger().setLevel(log_level)
    logging.info(event)

    response = client.delete_segment(
        ApplicationId=os.environ.get("PINPOINT_PROJECT_ID"),
        SegmentId=event["SegmentId"],
    )
    logging.info(response)
    db_logging_status = "CAMPAIGN_FAILED"

    return {
        "SegmentId": event["SegmentId"],
        "interest": event["interest"],
        "CampaignStatus": event["CampaignStatus"],
        "product_name": event["product_name"],
        "product_link": event["product_link"],
        "db_logging_status": db_logging_status,
    }
