import dearpygui.dearpygui as dpg
from view.main_view import show_main_view
from util.set_font import set_font

def _on_main_window_close(sender, app_data, user_data):
    dpg.delete_item(sender)
    dpg.delete_item("main")


def _log(sender, app_data, user_data):
    print(f"sender: {sender}, \t app_data: {app_data}, \t user_data: {user_data}")


def load_main_window():
    # 加载主窗口
    with dpg.window(label="main_view", on_close=_on_main_window_close, tag="main"):
        with dpg.menu_bar():
            with dpg.menu(label="File"):
                # dpg.add_text("File")
                dpg.add_menu_item(label="New")
                dpg.add_menu_item(label="Open")
                with dpg.menu(label="Open Recent"):
                    dpg.add_menu_item(label="test.py")
                dpg.add_menu_item(label="Save")
                dpg.add_menu_item(label="Save As...")
                with dpg.menu(label="Settings"):
                    dpg.add_menu_item(label="Option 1", callback=_log)
                    dpg.add_menu_item(label="Option 2", check=True, callback=_log)
                    dpg.add_menu_item(label="Option 3", check=True, default_value=True, callback=_log)

                    with dpg.child_window(height=60, autosize_x=True, delay_search=True):
                        for i in range(10):
                            dpg.add_text(f"Scolling Text{i}")

                    dpg.add_slider_float(label="Slider Float")
                    dpg.add_input_int(label="Input Int")
                    dpg.add_combo(("Yes", "No", "Maybe"), label="Combo")

            with dpg.menu(label="Tools"):

                dpg.add_menu_item(label="Show About", callback=lambda:dpg.show_tool(dpg.mvTool_About))
                dpg.add_menu_item(label="Show Metrics", callback=lambda:dpg.show_tool(dpg.mvTool_Metrics))
                dpg.add_menu_item(label="Show Documentation", callback=lambda:dpg.show_tool(dpg.mvTool_Doc))
                dpg.add_menu_item(label="Show Debug", callback=lambda:dpg.show_tool(dpg.mvTool_Debug))
                dpg.add_menu_item(label="Show Style Editor", callback=lambda:dpg.show_tool(dpg.mvTool_Style))
                dpg.add_menu_item(label="Show Font Manager", callback=lambda:dpg.show_tool(dpg.mvTool_Font))
                dpg.add_menu_item(label="Show Item Registry", callback=lambda:dpg.show_tool(dpg.mvTool_ItemRegistry))

            with dpg.menu(label="Settings"):

                dpg.add_menu_item(label="Wait For Input", check=True, callback=lambda s, a: dpg.configure_app(wait_for_input=a))
                dpg.add_menu_item(label="Toggle Fullscreen", callback=lambda:dpg.toggle_viewport_fullscreen())


def start_up_system():
    dpg.create_context()
    set_font()  # set the font of dpg

    with dpg.theme(tag="__hover_hyperlinkTheme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 0, 0, 0])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [0, 0, 0, 0])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [29, 151, 236, 25])
            dpg.add_theme_color(dpg.mvThemeCol_Text, [29, 151, 236])

    dpg.create_viewport(title='SHOP', width=650, height=700)
    dpg.set_viewport_resizable(False) # 设置窗口无法缩放
    dpg.set_viewport_pos([300,100])     # 设置窗口位置

    load_main_window()
                                    
    dpg.set_primary_window("main",True)
    show_main_view()
    
    
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()

    dpg.destroy_context()


if __name__ == '__main__':
    start_up_system()
