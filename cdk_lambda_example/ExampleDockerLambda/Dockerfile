FROM public.ecr.aws/lambda/python:3.8

# ENV AWS_DEFAULT_REGION=us-east-2

# LABEL maintainer="Wesley Cheek"
# Installs python, removes cache file to make things smaller
# RUN apt update -y && \
#     apt install -y python3 python3-dev python3-pip gcc
    # rm -Rf /var/cache/apt
# Be sure to copy over the function itself!
COPY example_docker_lambda.py ${LAMBDA_TASK_ROOT}
# Copies requirements.txt file into the container
COPY requirements.txt ./
# Installs dependencies found in your requirements.txt file
RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Allow for caching python modules
# VOLUME ["/.venv/lib/python3.10/site-packages/"]

# Points to the handler function of your lambda function
CMD ["example_docker_lambda.handler"]