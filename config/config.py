# =============================================
# Configuration globale du projet
# =============================================

KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
KAFKA_TOPIC = "transport_events"

DATA_RAW_PATH       = "data/raw/"
DATA_CLEANED_PATH   = "data/cleaned/"
DATA_PROCESSED_PATH = "data/processed/"
DATA_FINAL_PATH     = "data/final/"

SPARK_APP_NAME = "TransportDataEngineering"
SPARK_MASTER   = "local[*]"

TARGET_COLUMN  = "is_delayed"
TEST_SIZE      = 0.15
VAL_SIZE       = 0.15
RANDOM_STATE   = 42
