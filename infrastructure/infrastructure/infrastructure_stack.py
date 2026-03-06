from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
    aws_s3_deployment as s3deploy,
    aws_certificatemanager as acm,
    CfnOutput,
    RemovalPolicy,
)
from constructs import Construct

CERTIFICATE_ARN = "arn:aws:acm:us-east-1:981265948876:certificate/a9911ef0-5e38-4ce4-9ff9-e8fcd19802f9"
DOMAIN_NAMES = ["zaranara.uk", "www.zaranara.uk"]

class InfrastructureStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(
            # Holds static portfolio website files.
            self, "PortfolioBucket",
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        certificate = acm.Certificate.from_certificate_arn(
            self, "PortfolioCert", CERTIFICATE_ARN
        )

        distribution = cloudfront.Distribution(
            # CDN serves via HTTPS with custom domain
            self, "PortfolioDistribution",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3BucketOrigin.with_origin_access_control(bucket),
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
            ),
            default_root_object="index.html",
            domain_names=DOMAIN_NAMES,
            certificate=certificate,
        )

        s3deploy.BucketDeployment(
            # Frontend build injected into S3 bucket
            self, "DeployPortfolio",
            sources=[s3deploy.Source.asset("../frontend/build")],
            destination_bucket=bucket,
            distribution=distribution,
            distribution_paths=["/*"],
        )

        CfnOutput(
            self, "PortfolioURL",
            value="https://zaranara.uk",
            description="Personal website URL",
        )

        CfnOutput(
            self, "CloudFrontDomain",
            value=distribution.distribution_domain_name,
            description="CloudFront domain — add CNAME in Cloudflare pointing here",
        )
