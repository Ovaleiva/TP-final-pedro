import logging

class CorporateLog:
    def __init__(self):
        logging.basicConfig(filename='corporate_log.log', level=logging.INFO)
    
    def log_activity(self, message):
        logging.info(message)
        print(f"Activity Logged: {message}")
