"""An AWS Python Pulumi program"""
import json
import mimetypes
import os

import pulumi
from pulumi_aws import s3
from sphinx.cmd import build


def public_read_policy_for_bucket(bucket_name):
    return json.dumps(
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": ["s3:GetObject"],
                    "Resource": [
                        f"arn:aws:s3:::{bucket_name}/*",
                    ],
                }
            ],
        }
    )


def main(content_directory: str) -> None:
    # Create an AWS resource (S3 Bucket)
    bucket = s3.Bucket(
        "cdubos-public-website",
        website=s3.BucketWebsiteArgs(
            index_document="index.html",
        ),
    )

    for dir_name, _, files in os.walk(content_directory):
        for file in files:
            filepath = os.path.join(dir_name, file)
            mime_type, _ = mimetypes.guess_type(filepath)
            s3.BucketObject(
                (
                    filepath.replace(content_directory, "")
                    .removeprefix("/")
                    .replace(os.path.sep, "-")
                ),
                bucket=bucket.id,
                source=pulumi.FileAsset(filepath),
                content_type=mime_type,
            )

    s3.BucketPolicy(
        "bucket-policy",
        bucket=bucket.id,
        policy=bucket.id.apply(public_read_policy_for_bucket),
    )
    pulumi.export("bucket_name", bucket.id)
    pulumi.export("website_url", bucket.website_endpoint)


parent_directory = os.path.join(os.path.dirname(__file__), "..")
source_directory = os.path.join(parent_directory, "source")
build_directory = os.path.join(parent_directory, "build", "html")

build.main([source_directory, build_directory, "-b=html"])
main(build_directory)
