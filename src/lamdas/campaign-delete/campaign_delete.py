import logging
import os
import time

import boto3

client = boto3.client("pinpoint")


def lambda_handler(event, context):
    log_level = str(os.environ.get("LOG_LEVEL")).upper()
    if log_level not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        log_level = "ERROR"
    logging.getLogger().setLevel(log_level)
    logging.info(event)
    response = client.delete_campaign(
        ApplicationId=os.environ.get("PINPOINT_PROJECT_ID"),
        CampaignId=event["CampaignId"],
    )
    logging.info(response)
    time.sleep(3)

    response = client.delete_segment(
        ApplicationId=os.environ.get("PINPOINT_PROJECT_ID"),
        SegmentId=event["SegmentId"],
    )
    logging.info(response)
    db_logging_status = "SEGMENT_CAMPAIGN_SUCCESS"

    return {
        "SegmentId": event["SegmentId"],
        "CampaignId": event["CampaignId"],
        "CampaignStatus": event["CampaignStatus"],
        "Start": event["Start"],
        "End": event["End"],
        "TotalEndpointCount": event["TotalEndpointCount"],
        "SuccessfulEndpointCount": event["SuccessfulEndpointCount"],
        "interest": event["interest"],
        "product_name": event["product_name"],
        "product_link": event["product_link"],
        "db_logging_status": db_logging_status,
    }
