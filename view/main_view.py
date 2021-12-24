import dearpygui.dearpygui as dpg
import webbrowser
from view.bg_main_view import show_bgmain_view
from util.set_font import font_en

# 判断“项目介绍”是否已经存在
is_intro_exists = False

def _hyperlink(text, address):
    b = dpg.add_button(label=text, callback=lambda:webbrowser.open(address))
    dpg.bind_item_theme(b, "__hover_hyperlinkTheme")


def _help(message):
    last_item = dpg.last_item()
    group = dpg.add_group(horizontal=True)
    dpg.move_item(last_item, parent=group)
    dpg.capture_next_item(lambda s: dpg.move_item(s, parent=group))
    t = dpg.add_text("(?)", color=[255, 0, 0])
    with dpg.tooltip(t):
        dpg.add_text(message, tag="message")


def _enter_front_management():
    print("进入前台")

def _enter_back_management():
    print("进入后台")
    dpg.delete_item("My-Mall")
    show_bgmain_view()

def _exit_system():
    print("退出系统")
    exit(0)


def show_main_view():

    global is_intro_exists
    if not is_intro_exists:
        with dpg.group(horizontal=True, parent="main", tag="intro"):
            dpg.add_loading_indicator(circle_count=5)
            with dpg.group():
                dpg.add_text(f'Dear PyGui ({dpg.get_dearpygui_version()}) is used in this project. ', bullet=True, indent=5)
                dpg.add_text("This project has been uploaded to GitHub.", bullet=True, indent=5)
                with dpg.group(horizontal=True):
                    dpg.add_text("The code of this project can be found here:", bullet=True, indent=5)
                    _hyperlink("CMS", "https://github.com/Crazyokd/Commodity-Management-System")

        dpg.bind_item_font("intro",font_en)
        dpg.add_separator(parent="main")
        is_intro_exists = True
   

    with dpg.group(tag="My-Mall", parent="main"):
        dpg.add_text("我的商城")
        dpg.add_button(label="前台管理",callback=_enter_front_management)
        with dpg.tooltip(dpg.last_item()):
            dpg.add_text("目前该功能尚未开发")

        dpg.add_button(label="后台管理",callback=_enter_back_management)
        _help(
                "Click The Button Enter\n"
                "Back-stage Management.\n"
                )
        dpg.add_button(label="退出系统",callback=_exit_system)
    # with dpg.group(parent="main"):
        # dpg.add_color_edit((102, 179, 0, 128), label="color edit 4")


    width = dpg.get_viewport_width()
    height =  dpg.get_viewport_height()
    dpg.set_item_pos("My-Mall",[(width-75)/2,(height-200)/2])