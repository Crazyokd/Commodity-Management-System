import dearpygui.dearpygui as dpg
from util.set_font import set_font


def create_common_window():
    # set three window on primary window
    with dpg.window(tag="w1",width=300):
        dpg.add_text("This is window1")

    print("The width of w1 is %d" % dpg.get_item_width("w1"))

    with dpg.window(tag="w2"):
        dpg.add_text("This is window2")

    with dpg.window(tag="w3"):
        dpg.add_text("This is window3")


def create_child_window():
    with dpg.child_window(tag="child_window"): # 29
        dpg.add_text("This is child window.") # 30
        with dpg.group(tag="group"): # 31
            dpg.add_text("this is a group") # 32
        dpg.add_text("This is child window") # 33
        print("The width of the group is %d" % dpg.get_item_width("group")) # 0
        print(dpg.get_item_children("group"))

    print("The width of child window is %d" % dpg.get_item_width("child_window")) # 0
    print(dpg.get_item_children("child_window"))


def create_table():
    with dpg.table(tag="table"):
        # use add_table_column to add columns to the table,
        # table columns use child slot 0
        dpg.add_table_column(label="header1")
        dpg.add_table_column(label="header2")
        dpg.add_table_column(label="header3")

        # add_table_next_column will jump to the next row
        # once it reaches the end of the columns
        # table next column use slot 1
        for i in range(0, 4):
            with dpg.table_row():
                for j in range(0, 3):
                    dpg.add_text(f"Row{i} Column{j}")


dpg.create_context()
set_font() # set font
dpg.create_viewport(title="test",width=1000,height=800)

with dpg.window(tag="pw"):
    dpg.add_text("hello,world") # 27
    dpg.add_text("中国") # 28
    # create_child_window()
    # create_table()


print(dpg.get_item_children("pw"))

print("The height of viewport is %d " % dpg.get_viewport_height())
print("The width of primary window is %d" % dpg.get_item_width("pw")) # 0


dpg.setup_dearpygui()
dpg.set_primary_window("pw",True)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()