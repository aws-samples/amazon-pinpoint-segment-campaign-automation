import datetime
import logging
import os

import boto3

region = os.environ["AWS_REGION"]
dynamodbendpointurl = "https://dynamodb." + region + ".amazonaws.com"
dynamodb = boto3.resource("dynamodb", endpoint_url=dynamodbendpointurl)
table = dynamodb.Table(os.environ["TABLE_NAME"])


def lambda_handler(event, context):
    log_level = str(os.environ.get("LOG_LEVEL")).upper()
    if log_level not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        log_level = "ERROR"
    logging.getLogger().setLevel(log_level)
    logging.info(event)

    time_stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    OutputDate = (
        event["db_logging_status"] + "_" + event["product_name"] + "_" + time_stamp
    )

    if event["db_logging_status"] == "SEGMENT_FAILED":
        response = table.put_item(
            Item={
                "OutputDate": OutputDate,
                "interest": event["interest"],
                "product_name": event["product_name"],
                "product_link": event["product_link"],
            }
        )
        SegmentId = "NA"
        CampaignStatus = "NA"
        CampaignId = "NA"
        Start = "NA"
        End = "NA"
        TotalEndpointCount = "NA"
        SuccessfulEndpointCount = "NA"
    elif event["db_logging_status"] == "CAMPAIGN_FAILED":
        response = table.put_item(
            Item={
                "OutputDate": OutputDate,
                "interest": event["interest"],
                "product_name": event["product_name"],
                "product_link": event["product_link"],
                "SegmentId": event["SegmentId"],
                "CampaignStatus": event["CampaignStatus"],
            }
        )
        SegmentId = event["SegmentId"]
        CampaignStatus = event["CampaignStatus"]
        CampaignId = "NA"
        Start = "NA"
        End = "NA"
        TotalEndpointCount = "NA"
        SuccessfulEndpointCount = "NA"
    elif event["db_logging_status"] == "SEGMENT_CAMPAIGN_SUCCESS":
        response = table.put_item(
            Item={
                "OutputDate": OutputDate,
                "SegmentId": event["SegmentId"],
                "interest": event["interest"],
                "product_name": event["product_name"],
                "product_link": event["product_link"],
                "CampaignStatus": event["CampaignStatus"],
                "CampaignId": event["CampaignId"],
                "Start": event["Start"],
                "End": event["End"],
                "TotalEndpointCount": event["TotalEndpointCount"],
                "SuccessfulEndpointCount": event["SuccessfulEndpointCount"],
            }
        )
        SegmentId = event["SegmentId"]
        CampaignStatus = event["CampaignStatus"]
        CampaignId = event["CampaignId"]
        Start = event["Start"]
        End = event["End"]
        TotalEndpointCount = event["TotalEndpointCount"]
        SuccessfulEndpointCount = event["SuccessfulEndpointCount"]

    logging.info(response)
    return {
        "SegmentId": event["SegmentId"],
        "interest": event["interest"],
        "product_name": event["product_name"],
        "product_link": event["product_link"],
        "CampaignStatus": CampaignStatus,
        "CampaignId": CampaignId,
        "Start": Start,
        "End": End,
        "TotalEndpointCount": TotalEndpointCount,
        "SuccessfulEndpointCount": SuccessfulEndpointCount,
    }
