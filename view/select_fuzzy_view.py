import dearpygui.dearpygui as dpg
from dao.productDao import select_by_key_word
from view.bg_main_view import show_bgmain_view


def show_select_fuzzy_goods_view():
    def submit():
        try:
            dpg.delete_item("table")
        except:
            pass
        print("模糊查询")
        try:
            keyword = str(dpg.get_value("keyword"))
        except:
            print("类型转换异常")
        with dpg.table(tag="table",parent="sf"):
            # use add_table_column to add columns to the table,
            # table columns use child slot 0
            dpg.add_table_column(label="pro_id")
            dpg.add_table_column(label="pro_name")
            dpg.add_table_column(label="pro_num")
            dpg.add_table_column(label="pro_price")

            t = select_by_key_word(keyword)
            # add_table_next_column will jump to the next row
            # once it reaches the end of the columns
            # table next column use slot 1
            for i in range(0, len(t)):
                with dpg.table_row():
                    for j in range(0, len(t[i])):
                        print(i,j)
                        dpg.add_text(t[i][j])

    def return_pre_view():
        print("返回上一层")
        dpg.delete_item("sf")
        from view.items_view import items_main_view
        items_main_view()

    with dpg.window(label="sf_view",tag="sf"):
        with dpg.group(label="ct",tag="ct"):
            dpg.add_text("模糊查询")
            with dpg.group(label="key_word",tag="key_word"):
                dpg.add_text("关键字：")
                dpg.add_input_text(tag="keyword")
            
            dpg.add_button(label="查询",callback=submit)
            dpg.add_button(label="返回上一层",callback=return_pre_view)
        # width = dpg.get_viewport_width()
        # height =  dpg.get_viewport_height()
        # dpg.set_item_pos("ct",[(width-75)/2,(height-200)/2])
    dpg.set_primary_window("sf",True)