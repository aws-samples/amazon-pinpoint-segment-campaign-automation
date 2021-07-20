import logging
import os

import boto3

client = boto3.client("pinpoint")


def lambda_handler(event, context):
    log_level = str(os.environ.get("LOG_LEVEL")).upper()
    if log_level not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        log_level = "ERROR"
    logging.getLogger().setLevel(log_level)
    logging.info(event)
    response = client.get_campaign_activities(
        ApplicationId=os.environ.get("PINPOINT_PROJECT_ID"),
        CampaignId=event["CampaignId"],
    )
    logging.info(response)
    activity = response["ActivitiesResponse"]["Item"][0]
    if activity["State"] == "COMPLETED":
        end = activity["End"]
        start = activity["Start"]
        successendpoints = activity["SuccessfulEndpointCount"]
        totalendpoints = activity["TotalEndpointCount"]
    else:
        end = "NA"
        start = "NA"
        successendpoints = "NA"
        totalendpoints = "NA"

    return {
        "SegmentId": event["SegmentId"],
        "CampaignId": activity["CampaignId"],
        "CampaignStatus": activity["State"],
        "Start": start,
        "End": end,
        "SuccessfulEndpointCount": successendpoints,
        "TotalEndpointCount": totalendpoints,
        "interest": event["interest"],
        "product_name": event["product_name"],
        "product_link": event["product_link"],
    }
