import schedule
import time

def job():
    print("Hello World!")

#schedule.every(0.1).minutes.do(job)
#schedule.every().hour.do(job)
schedule.every().day.at("17:30").do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)

def auto_run():
    while True:
        schedule.run_pending()
        time.sleep(1)



auto_run()
