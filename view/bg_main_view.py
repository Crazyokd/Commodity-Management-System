import dearpygui.dearpygui as dpg

from dao.productDao import delete_pro, insert_pro, select_all, select_by_id, select_id, update_bd, select_by_key_word



def return_pre_view():
    from view.main_view import show_main_view
    dpg.delete_item("ct")
    show_main_view()

def exit_system():
    print("退出系统")
    exit(0)


def add_goods():
    print("save and add goods")
    try:
        name = str(dpg.get_value("ga_name"))
        price = float(dpg.get_value("ga_price"))
        num = int(dpg.get_value("ga_num"))
        insert_pro(name,num,price)
        update_combo()
    except:
        print("数值类型转换异常")
        

def delete_goods():
    print("save and delete goods")
    try:
        id = int(dpg.get_value("gd_id"))
        delete_pro(id)
        update_combo()
    except:
        print("数值转换异常")
        

def modify_goods():
    print("update goods")
    try:
        id = int(dpg.get_value("gm_id"))
        name = str(dpg.get_value("gm_name"))
        price = float(dpg.get_value("gm_price"))
        num = int(dpg.get_value("gm_num"))
        update_bd(id,name,num,price)
    except:
        print("类型转换异常")


def preview_goods():
    try:
        dpg.delete_item("gpt")
    except:
        pass
    with dpg.table(parent="gp", tag="gpt"):
        # use add_table_column to add columns to the table,
        # table columns use child slot 0
        dpg.add_table_column(label="pro_id")
        dpg.add_table_column(label="pro_name")
        dpg.add_table_column(label="pro_num")
        dpg.add_table_column(label="pro_price")

        t = select_all()
        # add_table_next_column will jump to the next row
        # once it reaches the end of the columns
        # table next column use slot 1
        for i in range(0, len(t)):
            with dpg.table_row():
                for j in range(0, len(t[i])):
                    dpg.add_text(t[i][j])


def query_goods():
    try:
        dpg.delete_item("gqt")
    except:
        pass
    print("模糊查询")
    try:
        keyword = str(dpg.get_value("keyword"))
    except:
        print("类型转换异常")
    with dpg.table(parent="gq", tag="gqt"):

        dpg.add_table_column(label="pro_id")
        dpg.add_table_column(label="pro_name")
        dpg.add_table_column(label="pro_num")
        dpg.add_table_column(label="pro_price")

        t = select_by_key_word(keyword)
        for i in range(0, len(t)):
            with dpg.table_row():
                for j in range(0, len(t[i])):
                    dpg.add_text(t[i][j])


def get_ids():
    t=select_id()
    res = list()
    for i in range(len(t)):
        res.append(t[i][0])
    return res
        

def update_combo():
    update_combo_dg()
    update_combo_mg()

def update_combo_dg():
    try:
        dpg.delete_item("gd_id")
    except:
        pass

    dpg.add_combo(get_ids(), label="商品ID", height_mode=dpg.mvComboHeight_Small, before="delete_goods", tag="gd_id")


def update_combo_mg():
    try:
        dpg.delete_item("gm_id")
        dpg.delete_item("gmg")
    except:
        pass
    
    _before_id="modify_goods"
    # if dpg.get_item_alias("gmg") is not None:
    #     _before_id="gmg"
    dpg.add_combo(get_ids(), label="商品ID", height_mode=dpg.mvComboHeight_Small, before=_before_id, callback=get_info_from_id, tag="gm_id")
    
        

def get_info_from_id(sender, app_data, user_data):
    try:
        dpg.delete_item("gmg")
    except:
        pass

    t=select_by_id(app_data)
    with dpg.group(parent="gm", before="modify_goods", tag="gmg"):
        with dpg.group():
            dpg.add_text("新的商品名称：")
            dpg.add_input_text(tag="gm_name", hint=t[0][0], default_value=t[0][0])
        with dpg.group():
            dpg.add_text("新的商品价格：")
            dpg.add_input_text(tag="gm_price",hint=t[0][2], default_value=t[0][2])
        with dpg.group():
            dpg.add_text("新的商品数量：")
            dpg.add_input_text(tag="gm_num", hint=t[0][1], default_value=t[0][1])
    


def show_bgmain_view():
    is_first_preview = True

    # 后台管理界面
    with dpg.group(tag="ct", parent="main"):
        dpg.add_text("后台管理界面")
        
        with dpg.collapsing_header(label="商品管理", tag="goods_management"):
            with dpg.tree_node(label="商品上架"):
                with dpg.group():
                    # dpg.add_text("商品名称：")
                    dpg.add_input_text(tag="ga_name", hint="商品名称")
                with dpg.group():
                    # dpg.add_text("商品价格：")
                    dpg.add_input_text(tag="ga_price", hint="商品价格")
                with dpg.group():
                    # dpg.add_text("商品数量：")
                    dpg.add_input_text(tag="ga_num", hint="商品数量")
                dpg.add_button(label="上架商品",callback=add_goods)
                
            with dpg.tree_node(label="商品下架"):
                with dpg.group(tag="gdg"):
                    
                    update_combo_dg()
                    dpg.add_button(label="下架商品",callback=delete_goods, tag="delete_goods")

            with dpg.tree_node(label="商品修改"):
                with dpg.group(tag="gm"):
                    with dpg.group():
                        update_combo_mg()
                    dpg.add_button(label="修改商品", callback=modify_goods, tag="modify_goods")
            
            with dpg.tree_node(label="商品预览"):
                with dpg.group(tag="gp"):
                    dpg.add_button(label="刷新", callback=preview_goods)
                    if is_first_preview:
                        preview_goods()
                        is_first_preview = False

            with dpg.tree_node(label="商品查询"):
                with dpg.group(tag="gq"):
                    dpg.add_text("关键字：")
                    dpg.add_input_text(tag="keyword")
            
                dpg.add_button(label="查询商品",callback=query_goods)
        

        with dpg.collapsing_header(label="用户管理", tag="um"):
            with dpg.tooltip(dpg.last_item()):
                dpg.add_text("目前该功能尚未开发")
        with dpg.collapsing_header(label="订单管理", tag="om"):
            with dpg.tooltip(dpg.last_item()):
                dpg.add_text("目前该功能尚未开发")

        dpg.add_button(label="退出系统",callback=exit_system)
        dpg.add_button(label="返回上一层",callback=return_pre_view)

    # width = dpg.get_viewport_width()
    # height = dpg.get_viewport_height()
    # dpg.set_item_pos("ct",[(width-75)/2,(height-300)/2])