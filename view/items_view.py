import traceback
import dearpygui.dearpygui as dpg

# from dao.productDao import insert_pro, select_all, delete_sku, update_bd, select_by_key_word


def items_main_view():
    def on_shelf_goods():
        dpg.delete_item("goods_management")
        from view.osg_view import show_on_shelf_goods_view
        show_on_shelf_goods_view()

    def off_shelf_goods():
        dpg.delete_item("goods_management")
        from view.offsg_view import show_off_shelf_goods_view
        show_off_shelf_goods_view()

    def modify_goods():
        dpg.delete_item("goods_management")
        from view.mg_view import show_modify_goods_view
        show_modify_goods_view()

    def query_all_goods():
        dpg.delete_item("goods_management")
        from view.select_all_view import show_select_all_goods_view
        show_select_all_goods_view()

    def return_pre_view():
        print("返回上一层")
        dpg.delete_item("goods_management")
        from view.bg_main_view import show_bgmain_view
        show_bgmain_view()

    def query_fuzzy():
        dpg.delete_item("goods_management")
        from view.select_fuzzy_view import show_select_fuzzy_goods_view
        show_select_fuzzy_goods_view()

    def exit_system():
        print("退出系统")
        exit()
    
    with dpg.window(label="goods_management",tag="goods_management"):
        with dpg.group(label="ct",tag="ct"):
            dpg.add_text("商品管理")
            dpg.add_button(label="商品上架",callback=on_shelf_goods)
            dpg.add_button(label="商品下架",callback=off_shelf_goods)
            dpg.add_button(label="商品修改",callback=modify_goods)
            dpg.add_button(label="全部商品查询",callback=query_all_goods)
            dpg.add_button(label="模糊查询",callback=query_fuzzy)
            dpg.add_button(label="退出系统",callback=exit_system)
            dpg.add_button(label="返回上一层",callback=return_pre_view)
        width = dpg.get_viewport_width()
        height = dpg.get_viewport_height()
        dpg.set_item_pos("ct",[(width-75)/2,(height-300)/2])
    dpg.set_primary_window("goods_management",True)

    # if it_oper == 1:
    #     print('商品上架')
    #     try:
    #         pro_name = input('请输入商品名称:')
    #         pro_num = int(input("请输入商品数目："))
    #         pro_price = float(input('请输入商品价格:'))
    #         insert_pro(pro_name, pro_num, pro_price)

    #     except ValueError:
    #         print('输入有误，自动返回上一级：')
    #         items_mian_view()
    #     items_mian_view()

    # if it_oper == 2:
    #     print('商品下架')
    #     sku__id = input('请输入商品ID：')
    #     delete_sku(sku__id)
    #     items_mian_view()

    # if it_oper == 3:
    #     print('商品修改')
    #     try:
    #         sku__id = input('请输入商品ID:')
    #         sku__name = input("请输入新的商品名称：")
    #         pro_num = int(input("请输入新的商品数量："))
    #         raw_price = float(input("请输入新的商品价格："))
    #         update_bd(sku__id, sku__name, pro_num, raw_price)
    #     except ValueError:
    #         print('输入有误，自动返回上一级：')
    #         items_mian_view()
    #     items_mian_view()

    # if it_oper == 4:
    #     print('商品查询')
    #     select_all()
    #     items_mian_view()