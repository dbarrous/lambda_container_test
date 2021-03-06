"""
This Module contains the FileProcessor class that will distinguish the appropriate
HERMES intrument library to use when processing the file based off which bucket the
file is located in.

TODO: Skeleton Code for initial repo, class still needs to be implemented including
logging to DynamoDB + S3 log file and docstrings expanded
"""

import logging


class FileProcessor:
    """
    Main FileProcessor class which initializes an object with the data file and the
    bucket event which triggered the lambda function to be called.
    """

    def __init__(self, bucket, file_key):
        """
        FileProcessor Constructor
        """
        # Initialize Logger
        logging.basicConfig()
        self.logger = logging.getLogger(__name__)

        # Initialize Class Variables
        self.bucket = bucket
        self.file_key = file_key
        self.file = self._download_file_from_s3()



    def process_file(self):
        """
        Function that chooses calls correct processing function
        based off file bucket.
        """

        if self.bucket == "spani":
            self._process_spani_file()

        elif self.bucket == "nemesis":
            self._process_nemesis_file()

        elif self.bucket == "eea":
            self._process_eea_file()

        elif self.bucket == "merit":
            self._process_merit_file()

        else:
            self.logger.error("ERROR: Not a valid bucket event")

    def _download_file_from_s3(self):
        """
        Function to download file from S3 using bucket key
        """
        self.logger.info("Downloading File: %s", self.file_key)
        try:
            # TODO: Add downloading logic
            self.logger.info("File Downloaded Successfully: %s", self.file_key)
            return True

        except:
            self.logger.error("Error when Downloading File: %s", self.file_key)
            return None

    def _log_status_in_dynamo_db(self):
        """
        This function logs the if the file was processed successfully/unsuccessfully
        in a DynamoDB table
        TODO: Add logging logic
        """

    def _log_status_in_s3(self):
        """
        This function logs the if the file was processed successfully/unsuccessfully
        in a logfile in an S3 Bucket
        TODO: Add logging logic
        """

    def _process_spani_file(self):
        """
        This function processes files from the SPAN-i Instrument
        The repo for this package can be found: https://github.com/HERMES-SOC/hermes_spani
        TODO: Add processing logic
        """
        # import hermes_spani
        self.logger.info("Processing SPAN-i Instrument File: %s", self.file_key)
        try:
            self.logger.info("File Processed Successfully: %s", self.file_key)

        except:
            self.logger.error("Error when Processing File: %s", self.file_key)

    def _process_nemesis_file(self):
        """
        This function processes files from the NEMESIS Instrument
        The repo for this package can be found: https://github.com/HERMES-SOC/hermes_nemesis
        TODO: Add processing logic
        """
        # import hermes_nemesis
        self.logger.info("Processing NEMESIS Instrument File: %s", self.file_key)
        try:
            self.logger.info("File Processed Successfully: %s", self.file_key)

        except:
            self.logger.error("Error when Processing File: %s", self.file_key)

    def _process_eea_file(self):
        """
        This function processes files from the EEA Instrument
        The repo for this package can be found: https://github.com/HERMES-SOC/hermes_eea
        TODO: Add processing logic
        """
        # import hermes_eea
        self.logger.info("Processing EEA Instrument File: %s", self.file_key)
        try:
            self.logger.info("File Processed Successfully: %s", self.file_key)

        except:
            self.logger.error("Error when Processing File: %s", self.file_key)

    def _process_merit_file(self):
        """
        This function processes files from the MERIT Instrument
        The repo for this package can be found: https://github.com/HERMES-SOC/hermes_merit
        TODO: Add processing logic
        """
        # import hermes_merit
        self.logger.info("Processing MERIT Instrument File: %s", self.file_key)
        try:
            self.logger.info("File Processed Successfully: %s", self.file_key)

        except:
            self.logger.error("Error when Processing File: %s", self.file_key)
