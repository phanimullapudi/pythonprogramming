import psutil
import time
import logging

# Set up logging
logging.basicConfig(filename='system_monitor.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def monitor_system():
    """
    Monitors CPU and memory usage and logs the information at regular intervals.
    """
    while True:
        try:
            cpu_usage: float = psutil.cpu_percent(interval=1)
            memory_info: psutil._common.svmem = psutil.virtual_memory()
            memory_usage: float = memory_info.percent
            logging.info(f'CPU Usage: {cpu_usage}%, Memory Usage: {memory_usage}%')
            time.sleep(10)


        except Exception as e:
            logging.error(f'Error occurred while monitoring system: {e}')
            time.sleep(10)

if __name__ == '__main__':
    monitor_system()