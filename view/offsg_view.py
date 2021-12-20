import dearpygui.dearpygui as dpg

from dao.productDao import delete_pro


def show_off_shelf_goods_view():
    def submit():
        print("off shelf goods")
        try:
            id = int(dpg.get_value("id"))
            delete_pro(id)
        except:
            print("数值转换异常")

    def return_pre_view():
        print("返回上一层")
        dpg.delete_item("offsg")
        from view.items_view import items_main_view
        items_main_view()

    with dpg.window(label="offsg_view",tag="offsg"):
        with dpg.group(label="ct",tag="ct"):
            dpg.add_text("商品下架")
            with dpg.group(label="goods_name",tag="goods_name"):
                dpg.add_text("商品ID：")
                dpg.add_input_text(tag="id")
        
            dpg.add_button(label="下架商品",callback=submit)
            dpg.add_button(label="返回上一层",callback=return_pre_view)
        # width = dpg.get_viewport_width()
        # height =  dpg.get_viewport_height()
        # dpg.set_item_pos("ct",[(width-75)/2,(height-200)/2])
    dpg.set_primary_window("offsg",True)