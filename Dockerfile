FROM public.ecr.aws/w5r9l1c8/swsoc-docker-lambda-base:latest

ARG FUNCTION_DIR="/function"
WORKDIR ${FUNCTION_DIR}

RUN curl -Lo /usr/local/bin/aws-lambda-rie \
    https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie && \
    chmod +x /usr/local/bin/aws-lambda-rie

COPY entry_script.sh ${FUNCTION_DIR}

# Install dependencies
RUN pip install \
    --target ${FUNCTION_DIR} \
    awslambdaric

# Copy function code
COPY src/* ${FUNCTION_DIR}

ENTRYPOINT [ "sh", "entry_script.sh" ]
CMD [ "lambda.handler" ]