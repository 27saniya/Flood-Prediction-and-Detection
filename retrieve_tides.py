from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import datetime
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/'

FILENAME_TIDE = 'allTides.txt'
API_KEY = '3a1639a1-313b-46c4-8da5-b7f577a82be3'
latitude = '76.26'
longitude = '9.94'

current_tide_api = 'https://api.marea.ooo/v2/tides?duration=1440&interval=60&latitude='+ latitude +'&longitude='+ longitude +'&model=FES2014&datum=MSL'

sched = BlockingScheduler()
gconfig = {
    'apscheduler.executors.default': {
        'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
        'max_workers': '20'
    },
    'apscheduler.executors.processpool': {
        'type': 'processpool',
        'max_workers': '5'
    },
    'apscheduler.job_defaults.coalesce': 'false',
    'apscheduler.job_defaults.max_instances': '3',
    'apscheduler.timezone': 'UTC',
}

def getAndAppendData(fileName):
    response = requests.get(current_tide_api, headers={"x-marea-api-token": API_KEY})
    fout = open(BASE_DIR + FILENAME_TIDE,"a")
    fout.write(response.text + '\n')
    fout.close()

@sched.scheduled_job('interval', minutes=15)
def timed_job():
    # ct stores current time
    ct = datetime.datetime.now()
    print('This job is run every 15 minutes.')
    getAndAppendData(FILENAME_TIDE)
    print(f"{ct:%Y-%m-%d-%H-%M}")

sched.configure(gconfig=gconfig)
sched.start()