-- 创建库 
create database if not exists shop;

-- 删除库
-- drop database if exists shop;

-- 创建products表
use shop;
CREATE TABLE IF NOT EXISTS products(
    pro_id INT(11) auto_increment,
    pro_name VARCHAR(255),
    pro_price decimal(10,2),
    pro_num INT(11),
    primary key (`pro_id`)
    
)ENGINE=InnoDB DEFAULT charset=utf8;

-- 删除products表
-- drop table if exists products;

-- 插入测试数据
-- insert into products(pro_id,pro_name,pro_price,pro_num)
-- values(1,"book1",24,10);
-- insert into products(pro_name,pro_price,pro_num)
-- values("book2",45,12);
-- insert into products(pro_name,pro_price,pro_num)
-- values("book3",23,23);
-- insert into products(pro_name,pro_price,pro_num)
-- values("book4",44,444);



