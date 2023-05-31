from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct
import aws_cdk as cdk
from aws_cdk import aws_lambda as _lambda
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
# from cdk_lambda_example.cdk_lambda_example_app_stage import MyPipelineAppStage
# from aws_cdk.pipelines import ManualApprovalStep


class CdkLambdaExampleStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkLambdaExampleQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        ## ++++++++++
        # secret = cdk.SecretValue.plain_text('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')
        # print("secret:{}".format(secret))
        # source   = CodePipelineSource.git_hub("paeinkai/cdk_lambda_example", "main", authentication=secret)

        # pipeline = CodePipeline(self, "Pipeline",
        #                         pipeline_name="MyPipeline",
        #                         synth=ShellStep("Synth",
        #                                 input=source,
        #                                 commands=["npm install -g aws-cdk",
        #                                             "python -m pip install -r requirements.txt",
        #                                             "cdk synth"]
        #                             )
        #                         )
        ## ----------
        self.build_lambda_func()

        # pipeline.add_stage(MyPipelineAppStage(self, "test",
        #     env=cdk.Environment(account="437006856469", region="us-east-2")))

        # testing_stage = pipeline.add_stage(MyPipelineAppStage(self, "testing",
        #     env=cdk.Environment(account="437006856469", region="us-east-2")))

        # testing_stage.add_post(ManualApprovalStep('approval'))
        
    def build_lambda_func(self):
        self.prediction_lambda = _lambda.DockerImageFunction(
            scope=self,
            id="CDKDockerLambda",
            # Function name on AWS
            function_name="CDKDockerLambda",
            # Use aws_cdk.aws_lambda.DockerImageCode.from_image_asset to build
            # a docker image on deployment
            code=_lambda.DockerImageCode.from_image_asset(
                # Directory relative to where you execute cdk deploy
                # contains a Dockerfile
                directory="cdk_lambda_example/ExampleDockerLambda"
            ),
        )