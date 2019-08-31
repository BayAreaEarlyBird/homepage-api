import multiprocessing

# ip and port
bind = '0.0.0.0:8000'
# gevent mode
worker_class = 'gevent'
# number of processes
workers = multiprocessing.cpu_count() * 2
# timeout 10 minutes
timeout = 10 * 60
