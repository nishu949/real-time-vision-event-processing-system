import logging

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def publish_event(message):

    print(f"[EVENT] {message}")

    logging.info(message)