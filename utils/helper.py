from core.config import CHUNK

# Function to execute SQL queries
def executeSql(cnx, sql, params=None):
    mycursor = cnx.cursor()
    if params:
        mycursor.executemany(sql, params)
    else:
        mycursor.execute(sql)

    return mycursor.fetchall()

def chunk(data):
    for i in range(0, len(data), CHUNK):
        yield data[i:i + CHUNK]


def group_by(data: list[dict], key: str) -> dict:
    items = {}
    for item in data:
        _item = items.setdefault(str(item[key]), [])
        _item.append(item)
    return items


# Function to convert a list to a tuple
def list_to_tuple(list):
    # Convert list to SQL-compatible tuple
    return f"('{list[0]}')" if (len(list) < 2) else f'{tuple(list)}'
