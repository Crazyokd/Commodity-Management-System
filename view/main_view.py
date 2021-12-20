import dearpygui.dearpygui as dpg
from view.bg_main_view import show_bgmain_view

def show_main_view():
    
    def enter_front_management():
        print("进入前台")

    def enter_back_management():
        print("进入后台")
        dpg.delete_item("main")
        show_bgmain_view()

    def exit_system():
        print("退出系统")
        exit(0)


    with dpg.window(label="main_view",tag="main"):
        with dpg.group(label="ct",tag="ct"):
            dpg.add_text("我的商城")
            dpg.add_button(label="前台管理",callback=enter_front_management)
            dpg.add_button(label="后台管理",callback=enter_back_management)
            dpg.add_button(label="退出系统",callback=exit_system)
        width = dpg.get_viewport_width()
        height =  dpg.get_viewport_height()
        dpg.set_item_pos("ct",[(width-75)/2,(height-200)/2])
    dpg.set_primary_window("main",True)