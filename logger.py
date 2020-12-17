from datetime import datetime

now = datetime.now()
timestamp = now.strftime('%Y/%m/%d %H:%M:%S')
timestamp_file = now.strftime('%Y-%m-%d_%H-%M-%S')
log_file = f'imagefilter-{timestamp_file}.log'.strip()

def log(msg):
    f"""
    Saves the msg in a log file {log_file} in log directory and prints it in the console.
    :param msg: the message to be append in the log file
    """
    formatted = f'{timestamp} - {msg}'
    print(formatted)
    with open(f'log/{log_file}', 'a') as f:
        f.write(formatted + '\n')