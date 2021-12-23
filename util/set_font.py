import dearpygui.dearpygui as dpg

def set_font():
    with dpg.font_registry(): #注册字体，自选字体
        with dpg.font("fonts/STKAITI.ttf", 30) as font_cn:	#增加中文编码范围，防止问号
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Simplified_Common)
            # dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
    dpg.bind_font(font_cn)

font_en = dpg.font("fonts/DEJAVUSANSMONO_0.ttf", 20)