import traceback
from random import random

from util.db_utill import get_mysql_conn


def insert_pro(pro_name="undefined", pro_num=1, pro_price=1.1):
    conn = get_mysql_conn()
    cur = conn.cursor()

    sql = "insert into products(pro_name,pro_num,pro_price) values('%s',%d,%f)" % (
        pro_name, pro_num, pro_price)
    try:
        rows = cur.execute(sql)
        if rows > 0:
            print('商品插入成功')
            conn.commit()
            # print("插入后的货架：")
            # select_all()
        else:
            return False

    except:
        print(traceback.format_exc())
        conn.rollback()
        return False
    finally:
        cur.close()
        conn.close()


def select_all():
    conn = get_mysql_conn()
    cur = conn.cursor()
    sql = "select pro_id,pro_name,pro_num,pro_price from products order by pro_num desc"
    try:
        rows = cur.execute(sql)
        if rows > 0:
            print('查询成功')
            t = cur.fetchall()
            conn.commit()
            return t
            # tu = ('商品ID', '商品名称', '商品数量', '商品价格')
            # print_tuple(tu)
            # for i in range(0, rows):
            #     t = cur.fetchone()
            #     print_tuple(t)
            #     conn.commit()
        else:
            return False

    except:
        print(traceback.format_exc())
        conn.rollback()
        return False
    finally:
        cur.close()
        conn.close()


def delete_pro(pro_id):
    if not is_pro_exist(pro_id):
        print('该商品ID不存在!')
        return False
    conn = get_mysql_conn()
    cur = conn.cursor()
    sql = "delete from products where pro_id='%s'" % pro_id
    try:
        rows = cur.execute(sql)
        if rows > 0:
            print('删除成功')
            conn.commit()
        else:
            return False

    except:
        print(traceback.format_exc())
        conn.rollback()
        return False
    finally:
        cur.close()
        conn.close()


def update_bd(pro_id="00001", pro_name="undefined", pro_num=3, pro_price=3.159):
    if not is_pro_exist(pro_id):
        print('ID ', pro_id, '不存在')
        return False
    conn = get_mysql_conn()
    cur = conn.cursor()
    sql = "update products set pro_name='%s',pro_num=%d, pro_price=%f where pro_id='%s'; " % (
        pro_name, pro_num, pro_price, pro_id)
    try:
        rows = cur.execute(sql)
        if rows > 0:
            print('修改成功')
            conn.commit()
        else:
            return False

    except:
        print(traceback.format_exc())
        conn.rollback()
        return False
    finally:
        cur.close()
        conn.close()


def print_tuple(t):
    for i in range(0, len(t)):
        temp = str(t[i])[0:15]
        print("{:15}\t".format(temp), end=' ')
    print('')


def is_pro_exist(pro_id):
    conn = get_mysql_conn()
    cur = conn.cursor()
    sql = "select count(*) from products where pro_id='%s'" % pro_id
    try:
        cur.execute(sql)
        re = cur.fetchone()
        if re[0] > 0:
            conn.commit()
            return True
        else:
            return False
    except:
        print(traceback.format_exc())
        conn.rollback()
        return False
    finally:
        cur.close()
        conn.close()


def select_by_key_word(keyword='0'):
    conn = get_mysql_conn()
    cur = conn.cursor()
    sql = "select* from products where pro_id like'%s' or pro_name like '%s' or pro_price like '%s' order " \
          "by pro_price desc;" % ("%"+keyword+"%", "%"+keyword+"%","%"+keyword+"%")
    try:
        rows = cur.execute(sql)
        re = cur.fetchall()
        if rows > 0:
            print("模糊查询结果：")
            conn.commit()
            return re
            # tu = ('商品ID', '商品名称', '商品数量', '商品价格')
            # print_tuple(tu)
            # for i in range(0, len(re)):
            #     print_tuple(re[i])
            # conn.commit()
        else:
            return False

    except:
        print(traceback.format_exc())
        conn.rollback()
        return False
    finally:
        cur.close()
        conn.close()

