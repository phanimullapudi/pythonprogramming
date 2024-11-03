import logging
import shutil
import time
import signal
import sys

# Set up logging
logging.basicConfig(filename='disk_monitor.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def monitor_disk_usage(path='/'):
    def signal_handler(sig, frame):
        logging.info('Terminating disk usage monitoring.')
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    while True:
        try:
            # Get disk usage statistics
            total, used, free = shutil.disk_usage(path)
            
            # Log the information
            logging.info(f"Disk Usage: Total: {total // (2**30)} GB, Used: {used // (2**30)} GB, Free: {free // (2**30)} GB")
            
            # Wait for 10 seconds before the next check
            time.sleep(10)
        except Exception as e:
            logging.error(f'Error occurred: {e}')
            time.sleep(10)

if __name__ == '__main__':
    monitor_disk_usage()
