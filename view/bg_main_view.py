import dearpygui.dearpygui as dpg


def show_bgmain_view():
    # 后台管理界面
    def goods_management():
        dpg.delete_item("bg")
        from view.items_view import items_main_view
        items_main_view()

    def users_management():
        print("用户管理")
        
    def order_management():
        print("订单管理")
    
    def return_pre_view():
        from view.main_view import show_main_view
        dpg.delete_item("bg")
        show_main_view()

    def exit_system():
        print("退出系统")
        exit(0)

    with dpg.window(label="bg",tag="bg"):
        with dpg.group(label="ct",tag="ct"):
            dpg.add_text("后台管理界面")
            dpg.add_button(label="商品管理",callback=goods_management)
            dpg.add_button(label="用户管理",callback=users_management)
            dpg.add_button(label="订单管理",callback=order_management)
            dpg.add_button(label="退出系统",callback=exit_system)
            dpg.add_button(label="返回上一层",callback=return_pre_view)
        width = dpg.get_viewport_width()
        height = dpg.get_viewport_height()
        dpg.set_item_pos("ct",[(width-75)/2,(height-300)/2])
    dpg.set_primary_window("bg",True)