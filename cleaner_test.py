import postgresql
import os
import datetime 
import codecs

# строка подключения
# CONNECTION_STRING = 'pq://ksvd4:7952-{cac8643d-a614-4eb6-8504-4af7877c1fb3}-14361@10.0.61.73:5432/ksvd4db'
CONNECTION_STRING = input("Ввести строку подключения"'\n')
DETECTOR_ID = input("Ввести ID детектора"'\n') # ID детектора
print("Типы детекторов:\n 1 - Засветка\n 2 - Затемнение\n 3- Перекрытие\n 4 - Срыв кадра\n "
	  "5 - Статичная сцена\n 6 - Расфокусировка\n 7 - Оставленный предмет")
DETECTOR_TYPE = input("Ввести тип детектора"'\n') # тип события

#dirpath = os.getcwd()
#files = os.listdir(dirpath)
#images = filter(lambda x: x.endswith('.jpg'), files)
#jpg = []
#for i in images:
 #   jpg.append(i)


SPAM_FILE = "spam.jpg"

def main():
	N = int(input("Ввести количество срабатываний"'\n'))
	try:
		if not os.path.isfile(os.path.join(os.getcwd(), SPAM_FILE)):
			raise Exception("spam file not found")

		spam_data = None
		with open(os.path.join(os.getcwd(), SPAM_FILE), "rb") as f:
			spam_data = f.read()
		if spam_data is None:
			raise Exception("spam file error")

		with postgresql.open(CONNECTION_STRING) as db:
			with db.xact() as xact:
				detector_checker = "SELECT _id FROM event WHERE _object = %s AND _etype = %s;" % (DETECTOR_ID, DETECTOR_TYPE)
				target_event_record = db.query(detector_checker)
				if len(target_event_record) == 0:
					db.execute("SELECT event_init(%s, %s);" % (DETECTOR_ID, DETECTOR_TYPE))

				target_event_record = db.query(detector_checker)
				if len(target_event_record) == 0:
					raise Exception("could not init event")

				event_id = target_event_record[0][0]
				
				file_rec_query = db.prepare("INSERT INTO files (_object, data) VALUES($1, $2::bytea) RETURNING _id;")
				file_rec = file_rec_query(event_id, spam_data)
				if len(file_rec) == 0:
					raise Exception("file insert error")

				file_id = file_rec[0][0]
				for i in range(N):
					insert_query = db.prepare("INSERT INTO event_log(_event, _file, triggered_time, value) VALUES ($1, $2, $3, $4) RETURNING _id;")
					res = insert_query(event_id, file_id, datetime.datetime.now(), 1)
					print("Inserted %s with id = %s" % (i + 1, res[0][0]))
	except Exception as e:
		print(e)

if __name__ == "__main__":
	main()