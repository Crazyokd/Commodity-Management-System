# Commodity Management System
一个十分简单的商品管理系统
## 为什么会有这个系统
别问，问就是Python大作业。

以下三点原因使我有兴趣完成该系统。
- 回顾SQL语法
- 尝尝pymysql
- 简单上手一款第三方Python GUI库
## 使用/二次开发
### 安装依赖
```shell
pip install -r requirements.txt
```

### 数据库
在数据库中直接执行[**shop.sql**](shop.sql)文件即可完成本系统与数据库相关的操作。

另外请读者注意以下三点：
- 笔者使用的数据库管理系统是mysql。
- 若需使用其他类型的数据库管理系统，可能需要修改[**shop.sql**](shop.sql)文件
- 若对库名或表名甚至是字段名不满意，请适当修改[**shop.sql**](shop.sql)文件

### 选择字体
请修改[set_font.py](util/set_font.py)文件中的字体路径。

### 启动系统
```shell
python3 main.py
```

## 其他目录
- [test_dpg](test_dpg)：当本系统需要用到dearpygui时，将会对涉及到的相关功能进行测试，该文件夹中存放的就是这样一类代码。

## 第三方参考
- [DearPyGui](https://github.com/hoffstadt/DearPyGui)
