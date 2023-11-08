import aws_cdk as core
import aws_cdk.assertions as assertions

from smile_confirm_demo.smile_confirm_demo_stack import SmileConfirmDemoStak

# example tests. To run these tests, uncomment this file along with the example
# resource in faq_lambda/faq_lambda_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SmileConfirmDemoStak(app, "smile_confirm_demo")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
