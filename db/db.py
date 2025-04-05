import oracledb
import config

pool = oracledb.SessionPool(
    user=config.USER,
    password=config.PASSWORD,
    host=config.HOST,
    port=config.PORT,
    service_name=config.SERVICE_NAME,
    min=config.MIN,
    max=config.MAX,
    increment=config.INCREMENT,
    encoding=config.ENCODING)


# @app.route("/")
def hello_world():
    conn = pool.acquire()
    # use conn
    pool.release(conn)
    return "<p>Hellooooooooooo, World!</p>"


def get_CLIENT():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#CLIENT FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]

                # # Формируем данные для шаблона
                # table = [dict(zip(columns, row)) for row in rows]

        return columns, data

def get_CL_PRIV():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#CL_PRIV FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]
        return columns, data

def get_CL_CORP():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#CL_CORP FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]
        return columns, data


def get_BANK_PROP():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#BANK_PROP FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]
        return columns, data


def get_COMMUNICS():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#COMMUNICS FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]
        return columns, data

def get_IDENTITY_CARD():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#IDENTITY_CARD FETCH FIRST 7 ROWS ONLY;")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]
        return columns, data

def get_HOUSE():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#HOUSE FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]
        return columns, data

def get_FLATS():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#FLATS FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]
        return columns, data

def get_PERSONAL_AC():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#PERSONAL_AC FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]
        return columns, data

def get_FLT_OWNER():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#FLT_OWNER FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]
        return columns, data

def get_LODGER():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#LODGER FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]
        return columns, data

def get_PROVIDER_CORP():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#PROVIDER_CORP FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]
        return columns, data

def get_PROV_LS():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#PROV_LS FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]
        return columns, data

def get_SERVICES():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#SERVICES FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]
        return columns, data

def get_NORMS():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#NORMS FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]
        return columns, data

def get_FLAT_SRV():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#FLAT_SRV FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]
        return columns, data

def get_COUNTER():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#COUNTER FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]
        return columns, data

def get_READING():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#READING FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]
        return columns, data

def get_LS_DISTRIB():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#LS_DISTRIB FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]
        return columns, data

def get_DOCUMENT():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#DOCUMENT FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]
        return columns, data

def get_ACCARC():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#ACCARC FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]
        return columns, data

def get_HM_COUNTER():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#HM_COUNTER FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]
        return columns, data

def get_HM_CHARGE():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#HM_CHARGE FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]
        return columns, data

def get_HM_FOLDERS():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#HM_FOLDERS FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]
        return columns, data

def get_HM_CHARGE_DOCS():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#HM_CHARGE_DOCS FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]
        return columns, data

def get_PERSONAL_AC_SQUARE():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#PERSONAL_AC_SQUARE FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]
        return columns, data

def get_PERSONAL_AC_():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#PERSONAL_AC# FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]

        return columns, data

def get_COUNTER_():
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM R#COUNTER# FETCH FIRST 7 ROWS ONLY")
                data = cursor.fetchall()
                # Получаем названия колонок
                columns = [col.name for col in cursor.description]
        return columns, data

def default():
    return

def personal_ac_obj(personal_ac_id):
    with pool.acquire() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT pa.id, pa.date_op, h.street_name, h.house_num, fl.flat_num, fl.id as FLAT_ID, cl.class_id, "
                           "cl.id as CLIENT_ID, h.WALL, fl.sort, pa.OWN_TYPE, pa.ROOMS_COUNT, pa.TOTAL_SQUARE, "
                           "NVL(h.PSLIFT_CNT,0) + NVL(h.FRLIFT_CNT, 0) as LIFT_COUNT, h.POST_IDX "
                           "FROM R#PERSONAL_AC pa "
                           "join R#FLATS fl on pa.flat = fl.id "
                           "join R#HOUSE h on fl.house = h.id "
                           "join R#FLT_OWNER fo on pa.id = fo.PERSONAL_AC "
                           "join R#CLIENT cl on fo.client = cl.id "
                           "where pa.id = :id", id = personal_ac_id)
            columns = [col[0] for col in cursor.description]
            cursor.rowfactory = lambda *args: dict(zip(columns, args))
            data = cursor.fetchone()

            if data["CLASS_ID"] == "CL_PRIV":
                cursor.execute("select last_name || ' ' ||first_name ||' '|| middle_name as NAME "
                    "from R#CL_PRIV "
                    "where id = :id", id=data["CLIENT_ID"])
                name_columns = [col[0] for col in cursor.description]
                cursor.rowfactory = lambda *args: dict(zip(name_columns, args))
                name_data = cursor.fetchone()

            elif data["CLASS_ID"] == "COMPANY":
                cursor.execute("select ORG_name "
                    "from R#CL_CORP "
                    "where id = :id", id=data["CLIENT_ID"])
                name_columns = [col[0] for col in cursor.description]
                cursor.rowfactory = lambda *args: dict(zip(name_columns, args))
                name_data = cursor.fetchone()

            data.update(name_data)

    lodger_columns, lodger_data = flat_lodger(data["FLAT_ID"])
    return data, lodger_columns, lodger_data

def flat_lodger(flat_id):
    with pool.acquire() as connection:
        with connection.cursor() as cursor:
            cursor.execute("select l.DATE_IN, l.DATE_OUT, "
                           "cp.last_name || ' ' || cp.first_name || ' ' || cp.middle_name as NAME "
                           "from r#lodger l "
                           "join r#cl_priv cp on l.person = cp.id "
                           "where l.flat= :flat_id", flat_id = flat_id)
            lodger_columns = [col[0] for col in cursor.description]
            lodger_data = cursor.fetchall()

    return lodger_columns, lodger_data

def personal_ac_accarc(personal_ac_id):
    with pool.acquire() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM R#ACCARC where personal_ac = :id", id = personal_ac_id)
            columns = [col[0] for col in cursor.description]
            cursor.rowfactory = lambda *args: dict(zip(columns, args))
            data = cursor.fetchone()

    return columns, data

def personal_ac_client(personal_ac_id):
    with pool.acquire() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM R#CLIENT where personal_ac = :id", id = personal_ac_id)
            columns = [col[0] for col in cursor.description]
            cursor.rowfactory = lambda *args: dict(zip(columns, args))
            # data = cursor.fetchone()
            data = cursor.fetchall()

    return columns, data

def client_communics(id):
    with pool.acquire() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM R#COMMUNICS where id = :id", id = id)
            columns = [col[0] for col in cursor.description]
            cursor.rowfactory = lambda *args: dict(zip(columns, args))
            # data = cursor.fetchone()
            data = cursor.fetchall()

    return columns, data

def client_flat(id):
    with pool.acquire() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM R#FLAT where id = :id", id = id)
            columns = [col[0] for col in cursor.description]
            cursor.rowfactory = lambda *args: dict(zip(columns, args))
            # data = cursor.fetchone()
            data = cursor.fetchall()

    return columns, data

tables_functions = {
"R#CLIENT": get_CLIENT,
"R#CL_PRIV": get_CL_PRIV,
"R#CL_CORP": get_CL_CORP,
"R#BANK_PROP": get_BANK_PROP,
"R#COMMUNICS": get_COMMUNICS,
"R#IDENTITY_CARD": get_IDENTITY_CARD,
"R#HOUSE": get_HOUSE,
"R#FLATS": get_FLATS,
"R#PERSONAL_AC": get_PERSONAL_AC,
"R#FLT_OWNER": get_FLT_OWNER,
"R#LODGER": get_LODGER,
"R#PROVIDER_CORP": get_PROVIDER_CORP,
"R#PROV_LS": get_PROV_LS,
"R#SERVICES": get_SERVICES,
"R#NORMS":get_NORMS,
"R#FLAT_SRV": get_FLAT_SRV,
"R#COUNTER": get_COUNTER,
"R#READING": get_READING,
"R#LS_DISTRIB": get_LS_DISTRIB,
"R#DOCUMENT": get_DOCUMENT,
"R#ACCARC": get_ACCARC,
"R#HM_COUNTER": get_HM_COUNTER,
"R#HM_CHARGE": get_HM_CHARGE,
"R#HM_FOLDERS": get_HM_FOLDERS,
"R#HM_CHARGE_DOCS": get_HM_CHARGE_DOCS,
"R#PERSONAL_AC_SQUARE": get_PERSONAL_AC_SQUARE,
"R#PERSONAL_AC#": get_PERSONAL_AC_,
"R#COUNTER#": get_COUNTER_
}

tables_names = {
"Клиент": "R#CLIENT",
"Физ.лицо": "R#CL_PRIV",
"Юр.лицо": "R#CL_CORP",
"Клиенты: банковские реквизиты": "R#BANK_PROP",
"Клиенты: средства связи": "R#COMMUNICS",
"Удостоверяющие документы": "R#IDENTITY_CARD",
"Дом": "R#HOUSE",
"Квартира": "R#FLATS",
"Лицевой счет": "R#PERSONAL_AC",
"Собственник": "R#FLT_OWNER",
"Проживающий": "R#LODGER",
"Договор теплоснабжения": "R#PROVIDER_CORP",
"Договора с юр.лицами: лицевые счета": "R#PROV_LS",
"Вид услуги": "R#SERVICES",
"Нормативы": "R#NORMS",
"Услуги квартиры": "R#FLAT_SRV",
"Счетчик": "R#COUNTER",
"Показание счетчка": "R#READING",
"Счетчик: распределение ЛС": "R#LS_DISTRIB",
"Документ": "R#DOCUMENT",
"Оборот": "R#ACCARC",
"ОПУ: физический прибор": "R#HM_COUNTER",
"Начисление ОПУ": "R#HM_CHARGE",
"Документы начисления": "R#HM_FOLDERS",
"Учтенные документы инд.начисления": "R#HM_CHARGE_DOCS",
"Площадь лицевого счета": "R#PERSONAL_AC_SQUARE",
"R#PERSONAL_AC#": "R#PERSONAL_AC#",
"R#COUNTER#": "R#COUNTER#"
}

def get_tables_names():
    # with pool.acquire() as connection:
    #     with connection.cursor() as cursor:
    #         cursor.execute("SELECT table_name FROM user_tables where table_name like '%R#%'")
    #         t_names = [tables_names.get(row[0]) for row in cursor.fetchall()]
    return tables_names.keys()


def get_table(table_name):
    return tables_functions.get(tables_names.get(table_name), default)()