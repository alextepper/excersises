import psycopg2


def get_by_name(search):
    connection = psycopg2.connect(host='localhost', user='postgres', password='password', dbname='pyMenu')
    try:
        with connection:
            with connection.cursor() as curs:
                query = f"""select * from menu_items where item_name ilike '%{search}%'"""
                curs.execute(query)
                results = curs.fetchall()
                list_of_objects = []
                for item in results:
                    list_of_objects.append(MenuItem(item[1], item[2]))
                return list_of_objects
                # return results
    except Exception as err:
        print(err)


class MenuManager:
    def __init__(self):
        self.menu_list = []

    def update(self):
        connection = psycopg2.connect(host='localhost', user='postgres', password='password', dbname='pyMenu')
        try:
            with connection:
                with connection.cursor() as curs:
                    query = 'select * from menu_items'
                    curs.execute(query)
                    results = curs.fetchall()
                    self.menu_list = results
        except Exception as err:
            print(err)

    @staticmethod
    def all_items():
        connection = psycopg2.connect(host='localhost', user='postgres', password='password', dbname='pyMenu')
        try:
            with connection:
                with connection.cursor() as curs:
                    query = f"""select * from menu_items"""
                    curs.execute(query)
                    results = curs.fetchall()
                    list_of_objects = []
                    for item in results:
                        list_of_objects.append(MenuItem(item[1], item[2]))
                    return list_of_objects
        except Exception as err:
            print(err)


class MenuItem:
    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price

    def __str__(self):
        return self.item_name + " " + str(self.item_price)

    def delete(self):
        connection = psycopg2.connect(host='localhost', user='postgres', password='password', dbname='pyMenu')
        try:
            with connection:
                with connection.cursor() as curs:
                    query = f"""delete from menu_items where item_name = '{self.item_name}' and item_price = {self.item_price}"""
                    curs.execute(query)
        except Exception as err:
                print(err)

    def save(self):
        connection = psycopg2.connect(host='localhost', user='postgres', password='password', dbname='pyMenu')
        try:
            with connection:
                with connection.cursor() as curs:
                    query = f"""insert into menu_items(item_name, item_price) values ('{self.item_name}', {self.item_price})"""
                    curs.execute(query)
        except Exception as err:
                print(err)

    def update(self, new_name, new_price):
        connection = psycopg2.connect(host='localhost', user='postgres', password='password', dbname='pyMenu')
        try:
            with connection:
                with connection.cursor() as curs:
                    query = f"""update menu_items set item_name = '{new_name}', item_price = {new_price} where item_name = '{self.item_name}'"""
                    curs.execute(query)
        except Exception as err:
                print(err)

# burger = MenuItem("hamburger", 50)
#
# menu = MenuManager()
# menu.update()
#
# for item in menu.all_items():
#     print(item)

