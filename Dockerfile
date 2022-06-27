FROM public.ecr.aws/w5r9l1c8/swsoc-docker-lambda-base:latest

ARG ROOT="/"
ARG FUNCTION_DIR="/function/"
ARG DEV_FUNCTION_DIR="/dev_function/"

WORKDIR ${FUNCTION_DIR}

RUN curl -Lo /usr/local/bin/aws-lambda-rie \
    https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie && \
    chmod +x /usr/local/bin/aws-lambda-rie

COPY entry_script.sh ${FUNCTION_DIR}

# # # Install dependencies
# # RUN pip install \
# #     --target ${DEV_FUNCTION_DIR} \
# #     awslambdaric

# COPY src/* ${DEV_FUNCTION_DIR}

WORKDIR ${ROOT}

# Copy function code
RUN git clone https://github.com/dbarrous/lambda_container_test.git \
    && cd lambda_container_test/src \
    && ls \
    && mv prod.py ${FUNCTION_DIR}/src/
    

RUN 
COPY src/. ${FUNCTION_DIR}

ENTRYPOINT [ "sh", "entry_script.sh" ]
CMD [ "lambda.handler" ]