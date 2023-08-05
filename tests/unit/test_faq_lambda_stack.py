import aws_cdk as core
import aws_cdk.assertions as assertions

from faq_lambda.faq_lambda_stack import FaqLambdaStack

# example tests. To run these tests, uncomment this file along with the example
# resource in faq_lambda/faq_lambda_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = FaqLambdaStack(app, "faq-lambda")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
