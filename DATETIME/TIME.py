from time import sleep
import datetime

NIGHT_STARTS = 17


def main():
    current_time = datetime.datetime.now()
    while True:
        sleep(1)
        current_time += datetime.timedelta(hours=1)
        print("La hora actual es {}".format(current_time))

if __name__=="__main__":
    main()