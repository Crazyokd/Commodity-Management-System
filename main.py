import dearpygui.dearpygui as dpg
from view.main_view import show_main_view
from util.set_font import set_font

def start_up_system():
    dpg.create_context()
    set_font()  # set the font of dpg

    dpg.create_viewport(title='SHOP', width=400, height=500)
    dpg.set_viewport_resizable(False) # 设置窗口无法缩放

    show_main_view()
    
    dpg.set_viewport_pos([300,100])
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()

    dpg.destroy_context()


if __name__ == '__main__':
    start_up_system()
