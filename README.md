# cmdb

本cmdb基于salt，zabbix，ELK和标准化的机器名，部署路径等完成自动化运维。

## cmdb功能测试
### app.opmanage
1. 登录
2. 退出
3. 添加用户
4. 删除用户
5. 用户自助修改密码
6. 修改用户信息

邮件如果发给一个不存在的人会返回成功吗？

## 依赖包
- djang-1.11.5
- pymysql-0.7.11
- pyzabbix-0.7.4
- elasticsearch-6.0.0

## 配置文件
- global.config
- cmdb.config
- zabbix.config
- elasticsearch.config

## 生成数据库并启动服务

python manage.py makemigrations
python manage.py migrate
python manage.py runserver


