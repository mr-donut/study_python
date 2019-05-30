import time
import datetime

now = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

class Logger:


    INFO = "1"
    DEBUG = "2"
    ERROR = "3"
    FATAL = "4"

    def set_log_file(poncho, filename):

        poncho.filename = filename
        with open(poncho.filename, "w") as file:
            file.write("__")

    def log(self, message, level, number):

        self.message = 'message'
        self.level = 'level'
        self.number = number

        with open(self.filename, 'a') as file:
            string_1 = str(now) + " " + str(level) + " " + str(message) + " " + str(number)
            file.write(string_1 + '\n')
        print(string_1)

if __name__ == "__main__":

    x = int(input('веедите переднюю границу числового ряда: '))
    y = int(input('веедите заднюю границу числового ряда: '))
    for number in range(x, y + 1):
        result = number ** 2
    # result = 100
    logger = Logger()
    logger.set_log_file("sample.txt")
        logger.log("Message", Logger.INFO, result)

    print(logger.log("number", Logger.DEBUG, result))