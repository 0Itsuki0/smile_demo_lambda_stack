# FROM amazon/aws-lambda-python:latest
FROM public.ecr.aws/lambda/python:3.7

LABEL maintainer="Itsuki"
RUN yum update -y && \
    yum install -y python3 python3-dev python3-pip gcc && \
    rm -Rf /var/cache/yum

COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN pip install opencv-python
RUN pip install numpy
COPY . ./

CMD ["lambda_function.handler"]