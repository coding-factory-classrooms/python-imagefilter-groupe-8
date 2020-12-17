from datetime import datetime

def log(msg):
    now = datetime.now()
    timestamp = now.strftime('%Y/%m/%d %H:%M:%S')
    timestamp_file = now.strftime('%Y-%m-%d_%H-%M-%S')
    formatted = f'{timestamp} - {msg}'
    log_file = f'imagefilter-{timestamp_file}.log'.strip()
    print(formatted)
    with open(f'log/{log_file}', 'a') as f:
        f.write(formatted + '\n')

# def dump_log():
#     try:
#         with open(f'log/{log_file}', 'r') as f:
#             print(f.read())
#     except FileNotFoundError as e:
#         print(f'Cannot open {log_file}. error={e}')