import oracledb
from .config import Config

pool = oracledb.SessionPool(
    user=Config.USER,
    password=Config.PASSWORD,
    host=Config.HOST,
    port=Config.PORT,
    service_name=Config.SERVICE_NAME,
    min=Config.MIN,
    max=Config.MAX,
    increment=Config.INCREMENT,
    encoding=Config.ENCODING)


def personal_ac_obj(personal_ac_id):
    with pool.acquire() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT pa.id, TO_CHAR(pa.date_op, 'YYYY-MM-DD') as date_op, h.street_name, "
                           "h.house_num, fl.flat_num, fl.lodgers, fl.id as FLAT_ID, pa.communics, cl.class_id, "
                           "cl.id as CLIENT_ID, h.WALL, fl.sort, pa.OWN_TYPE, pa.ROOMS_COUNT, pas.DATE_BEGIN, "
                           "pas.TOTAL_SQUARE, pas.LIVING_SQUARE, "
                           "NVL(h.PSLIFT_CNT,0) + NVL(h.FRLIFT_CNT, 0) as LIFT_COUNT, h.POST_IDX, fl.SRVS "
                           "FROM R#PERSONAL_AC pa "
                           "join R#FLATS fl on pa.flat = fl.id "
                           "join R#HOUSE h on fl.house = h.id "
                           "join R#FLT_OWNER fo on pa.id = fo.PERSONAL_AC "
                           "join R#CLIENT cl on fo.client = cl.id "
                           "join R#PERSONAl_AC_SQUARE pas on pas.personal_ac = pa.id "
                           "where pa.id = :id", id = personal_ac_id)
            columns = [col[0] for col in cursor.description]
            cursor.rowfactory = lambda *args: dict(zip(columns, args))
            data = cursor.fetchone()
            data = pa_class(data)

    lodger_columns, lodger_data = flat_lodger(data["LODGERS"])
    fl_srvs_columns, fl_srvs_data = flat_services(data["SRVS"])
    accarc_columns, accarc_data = pa_accarc(data["ID"])
    communics_columns, communics_data = pa_communics(data["COMMUNICS"])
    pa_c_columns, pa_c_data = pa_counters(data["ID"])
    f_с_columns, f_c_data = flat_counters(data["FLAT_ID"])
    return (data, lodger_columns, lodger_data, fl_srvs_columns, fl_srvs_data,
            accarc_columns, accarc_data, communics_columns, communics_data,
            pa_c_columns, pa_c_data, f_с_columns, f_c_data)

def pa_class(data):
    with pool.acquire() as connection:
        with connection.cursor() as cursor:
            if data["CLASS_ID"] == "CL_PRIV":
                cursor.execute("select last_name || ' ' ||first_name ||' '|| middle_name as NAME "
                               "from R#CL_PRIV "
                               "where id = :id", id=data["CLIENT_ID"])
                name_columns = [col[0] for col in cursor.description]
                cursor.rowfactory = lambda *args: dict(zip(name_columns, args))
                name_data = cursor.fetchone()
                data["CLASS_ID"] = "Физ.лицо"

            elif data["CLASS_ID"] == "COMPANY":
                cursor.execute("select ORG_name "
                               "from R#CL_CORP "
                               "where id = :id", id=data["CLIENT_ID"])
                name_columns = [col[0] for col in cursor.description]
                cursor.rowfactory = lambda *args: dict(zip(name_columns, args))
                name_data = cursor.fetchone()
                data["CLASS_ID"] = "Юр.лицо"

            data.update(name_data)
    return data

def flat_lodger(flat_lodgers):
    with pool.acquire() as connection:
        with connection.cursor() as cursor:
            cursor.execute("select TO_CHAR(l.DATE_IN, 'YYYY-MM-DD') as С, "
                           "TO_CHAR(l.DATE_OUT, 'YYYY-MM-DD') as ПО, "
                           "cp.last_name || ' ' || cp.first_name || ' ' || cp.middle_name as ФИО "
                           "from r#lodger l "
                           "join r#cl_priv cp on l.person = cp.id "
                           "where l.flat= :flat_lodgers", flat_lodgers = flat_lodgers)
            columns = [col[0] for col in cursor.description]
            data = cursor.fetchall()

    return columns, data

def flat_services(fl_srvs_id):
    with pool.acquire() as connection:
        with connection.cursor() as cursor:
            cursor.execute("select distinct s.id as Код, s.name as Услуга, "
                           "TO_CHAR(n.date_begin, 'YYYY-MM-DD') as С, TO_CHAR(n.date_end, 'YYYY-MM-DD') as ПО, "
                           "n.value as Тариф, n.id as Норматив, n.measure as Алгоритм "
                           "from r#flat_srv fs "
                           "join r#services s on fs.SERVICE = s.id "
                           "join r#norms n on s.id = n.service "
                           "where fs.COLLECTION_ID = :fl_srvs_id", fl_srvs_id = fl_srvs_id)
            columns = [col[0] for col in cursor.description]
            data = cursor.fetchall()

    return columns, data

def pa_accarc(pa_id):
    with pool.acquire() as connection:
        with connection.cursor() as cursor:
            cursor.execute("select id as КОД, service as УСЛУГА, TO_CHAR(opdate, 'YYYY-MM-DD') as МЕСЯЦ, "
                           "saldo as \"Входящий остаток\" , dt as \"Оборот ДТ\", ct as \"Оборот КТ\" , "
                           "charge as Начисление , maket as Макет, repays as Возврат, pays as Оплата, "
                           "subsidy as Субсидии "
                           "from r#accarc "
                           "where personal_ac = :pa_id", pa_id = pa_id)
            columns = [col[0] for col in cursor.description]
            data = cursor.fetchall()

    return columns, data

def pa_communics(pa_communics):
    with pool.acquire() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT SORT ||' '|| SUBSORT as Вид, NOMER as Значение, DESCR as Описание "
                           "FROM R#COMMUNICS where collection_id = :pa_communics ",
                           pa_communics = pa_communics)
            columns = [col[0] for col in cursor.description]
            data = cursor.fetchall()

    return columns, data

def pa_counters(pa_id):
    with pool.acquire() as connection:
        with connection.cursor() as cursor:
            cursor.execute("select c.id as Код, c.service as Услуга, c.NUM as Номер, TO_CHAR(c.set_date, 'YYYY-MM-DD') as \"Начало учета\", c.readings as Показания "
                           "from r#ls_distrib ld "
                           "join r#counter c on ld.collection_id = c.ls_distrib "
                           "where ld.personal_ac = :pa_id ",
                           pa_id = pa_id)
            columns = [col[0] for col in cursor.description]
            data = cursor.fetchall()

    return columns, data

def flat_counters(flat_id):
    with pool.acquire() as connection:
        with connection.cursor() as cursor:
            cursor.execute("select c.id as Код, c.service as Услуга, c.NUM as Номер, TO_CHAR(c.set_date, 'YYYY-MM-DD') as \"Начало учета\", c.readings as Показания "
                           "from r#flats f "
                           "join r#counter c on f.counters = c.collection_id "
                           "where f.id  = :flat_id ",
                           flat_id = flat_id)
            columns = [col[0] for col in cursor.description]
            data = cursor.fetchall()

    return columns, data

# def house_counters(flat_id):
#     with pool.acquire() as connection:
#         with connection.cursor() as cursor:
#             cursor.execute("select c.id as Код, c.service as Услуга, c.NUM as Номер, TO_CHAR(c.set_date, 'YYYY-MM-DD') as \"Начало учета\", c.readings as Показания "
#                            "from r#flats f "
#                            "join r#counter c on f.counters = c.collection_id "
#                            "where f.id  = :flat_id ",
#                            flat_id = flat_id)
#             columns = [col[0] for col in cursor.description]
#             data = cursor.fetchall()
#
#     return columns, data

def сounter_readings(c_reading_id):
    with pool.acquire() as connection:
        with connection.cursor() as cursor:
            cursor.execute("select TO_CHAR(c_date, 'YYYY-MM-DD') as \"Дата учета\", reading as Показание, "
                           "TO_CHAR(date_ctrl, 'YYYY-MM-DD')  as \"Дата контрольного показания\" "
                           "from r#reading "
                           "where collection_id  = :c_reading_id ",
                           c_reading_id = c_reading_id)
            columns = [col[0] for col in cursor.description]
            data = cursor.fetchall()

    return columns, data