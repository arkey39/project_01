# Соединение с БД

class Connection:
    '''Соединение с базой данных'''

    def __init__(self, ip):
        self.host = ip
        print('Соединение с:', self.host)

    def send_query(self, query):
            print(f'Запрос {query} отправлен') # Заглушка

    def __del__(self):
        self.host = None
        print('Соединение разорвано!') # Деструктор срабатывает только после
                                       # выполнения всех команд
        
conn = Connection('127.0.0.1')
conn.send_query('SELECT * FROM table;')