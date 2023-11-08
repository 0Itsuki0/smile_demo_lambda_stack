from aws_cdk import (
    Stack,
    aws_lambda as _lambda
)
from constructs import Construct


class SmileConfirmDemoStak(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.build_lambda_func()


    def build_lambda_func(self):
        self.lambda_from_image = _lambda.DockerImageFunction(
            scope=self,
            id="smile_confirm_demo",
            function_name="smile_confirm_demo",
            code=_lambda.DockerImageCode.from_image_asset(
                directory="lambda_function"
            ),
        ).add_function_url(
            auth_type=_lambda.FunctionUrlAuthType.NONE,
        )
