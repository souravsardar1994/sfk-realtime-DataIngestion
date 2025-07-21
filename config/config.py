# AWS Configuration
AWS_REGION = "us-east-1"
S3_BUCKET = "snowpipe-demo-ss-source"
S3_PREFIX = "transactions/"
AWS_ACCESS_KEY_ID = ""  # In production, use environment variables
AWS_SECRET_ACCESS_KEY = ""

# Snowflake Configuration
SNOWFLAKE_ACCOUNT = ""
SNOWFLAKE_USER = "<sfk-user>"
SNOWFLAKE_PASSWORD = "<sfk-password>"
SNOWFLAKE_WAREHOUSE = "COMPUTE_WH"
SNOWFLAKE_DATABASE = "SNOWPIPE_DEMO"
SNOWFLAKE_SCHEMA = "DATA_INGESTION"
SNOWFLAKE_STAGE = "MY_S3_STAGE"
SNOWFLAKE_PIPE = "CUSTOMER_TRANSACTIONS_PIPE"
FILE_FORMAT = "CSV_FORMAT"

# Application Settings
GENERATION_INTERVAL_MIN = 1  # minutes
GENERATION_INTERVAL_MAX = 5  # minutes
BATCH_SIZE_MIN = 100
BATCH_SIZE_MAX = 1000

# arn:aws:iam::241526746228:role/SnowflakeS3Access_role