from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import datetime
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/'

FILENAME_WEATHER = 'allWeather.txt'
API_KEY = '3e6a65d3cf77158db5aae1cfd2401629'
latitude = '76.26'
longitude = '9.94'

current_weather_api = 'https://api.openweathermap.org/data/2.5/weather?lat=' + latitude +'&lon='+ longitude + '&appid=' + API_KEY

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
    response = requests.get(current_weather_api)
    fout = open(BASE_DIR+FILENAME_WEATHER,"a")
    fout.write(response.text + '\n')
    fout.close()
    pass

@sched.scheduled_job('interval', minutes=15)
def timed_job():
    # ct stores current time
    ct = datetime.datetime.now()
    print('This job is run every 15 minutes.')
    getAndAppendData(FILENAME_WEATHER)
    print(f"{ct:%Y-%m-%d-%H-%M}")

sched.configure(gconfig=gconfig)
sched.start()