import postgresql
import uuid

CONNECTION_STRING = input("Ввести строку подключения"'\n')


def main():
	try:
		with postgresql.open(CONNECTION_STRING) as db:
			SERVER_ID = 'NULL'
			camera_name = "Камера %s"
			camera_inserter = "INSERT INTO object \
				(_otype, _parent, guid, name, descr, version, revision, uri, status) \
						VALUES (2, %s, '%s', '%s', '', '', 0, 'tcp::', 0) RETURNING _id"
			
			start_id = int(input("С какого id начать создавать камеры?"'\n')) # ID детектора
			quantity = int(input("количество камер?"'\n')) # количество
			rtsp = str('rtsp://172.18.102.119:8888/' + str(input("id камеры ретранслятора: ")))   #ссылка
			end_id = (start_id + quantity)
			name_counter = 1
			
			for i in range(start_id, end_id):
				base_rtsp = rtsp   # base_rtsp = 'rtsp://172.18.102.119:8888/' +str(i)
				camera_params = {
					'Uri': base_rtsp,
					'Login': 'admin',
					'Password': 'admin',
					'Module': 0,
					'Transport': 0,
					'PoolLimit': 40,
					'Decode': 1,
					'Uri2': '',
					'Audio': 1, 
					'Uri3': ''
				}
				with db.xact() as xact:
					new_id = db.query(camera_inserter % (SERVER_ID, str(uuid.uuid4()), camera_name % str(name_counter)))[0][0]
					tail = []
					for param in camera_params:
						tail.append("(%s, '%s', '%s')" % (new_id, param, camera_params[param]))
					db.query("INSERT INTO object_settings (_object, key, value) VALUES" + ','.join(tail))
					
				name_counter += 1
	except Exception as e:
		print(e)
		print("FUCK!")
		
	print("FINISHED!")
	
if __name__ == "__main__":
	main()