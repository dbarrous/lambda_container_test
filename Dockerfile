# Repo where this image's Dockerfile is maintained: https://github.com/HERMES-SOC/docker-lambda-base
FROM public.ecr.aws/w5r9l1c8/swsoc-docker-lambda-base:latest

# Working Directory Arguments
ARG ROOT="/"
ARG FUNCTION_DIR="/function/"

# Change working directory to /function
WORKDIR ${FUNCTION_DIR}

# Copy files from the source folder
COPY src/. ${FUNCTION_DIR}

# Change name of file processor module in container
RUN mv file_processor dev_file_processor \
    && ls

# Copy entry script into function director (Script is used distinguish dev/production mode)
COPY entry_script.sh ${FUNCTION_DIR}

# Change working directory to root
WORKDIR ${ROOT}

# Pull the latest official release of repo and copy it's file processor module into function directory
RUN git clone https://github.com/dbarrous/lambda_container_test.git \
    && cd lambda_container_test/src \
    && cp file_processor /function/

# Runs entry script to decide wether to run function in local environment or in production environment
ENTRYPOINT [ "sh", "entry_script.sh" ]

# Runs lambda handler function
CMD [ "lambda.handler" ]