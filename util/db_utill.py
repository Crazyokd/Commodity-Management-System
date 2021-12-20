import pymysql


def get_mysql_conn():
    conn = pymysql.Connect(host='localhost', port=3306, user='root', passwd='011010', database='shop')
    return conn


# def select_items():
#     ccc = get_mysql_conn().cursor()
#     sql = "select sku_name,loc_name,item_num,price,pro_num,raw_price from locations,products,items where " \
#           "locations.loc_id=items.loc_id and products.sku_id=items.sku_id;"

#     rows = ccc.execute(sql)
#     for i in range(0, rows):
#         print(ccc.fetchone())


# if __name__ == '__main__':
#     select_items()
