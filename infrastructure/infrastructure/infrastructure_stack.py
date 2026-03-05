from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
    aws_s3_deployment as s3deploy,
    CfnOutput,
    RemovalPolicy,
)
from constructs import Construct

class InfrastructureStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        bucket = s3.Bucket(
            # Holds static profolio website file.
            self, "PortfolioBucket",
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        distribution = cloudfront.Distribution(
            # CDN serves via HTTP 
            self, "PortfolioDistribution",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3BucketOrigin.with_origin_access_control(bucket),
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
            ),
            default_root_object="index.html",
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
            # provide the clourfront url when the deployment finishes
            self, "PortfolioURL",
            value=f"https://{distribution.distribution_domain_name}",
            description="personal website URL",
        )

        
