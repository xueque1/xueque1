import msvcrt
import os
import csv


def ywfilezm(dic):
    filename = r'user.csv'
    csvf = open(filename, 'w', newline='')
    writer = csv.writer(csvf)
    writer.writerow(['账号', '密码'])
    for i in dic:
        writer.writerow([i, user.dic[i]])
    csvf.close()


def yrfilezm(dic):
    filename = r'user.csv'
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        try:
            next(reader)
        except StopIteration:
            pass
        for row in reader:
            dic[row[0]] = row[1]


def gwfilezm(dic):
    filename = r'admin.csv'
    csvf = open(filename, 'w', newline='')
    writer = csv.writer(csvf)
    writer.writerow(['账号', '密码'])
    for i in dic:
        writer.writerow([i, Admin.ad_dic[i]])
    csvf.close()


def grfilezm(dic):
    filename = r'admin.csv'
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        try:
            next(reader)
        except StopIteration:
            pass
        for row in reader:
            dic[row[0]] = row[1]

def bdwfile(dic):
    filename = r'book.csv'
    csvf = open(filename, 'w', newline='')
    writer = csv.writer(csvf)
    writer.writerow(['编号', '书名', '价格', '数量'])
    for i in dic:
        writer.writerow([i.book_id, i.book_name, i.book_price, i.book_num])
    csvf.close()

def bdrfile(dic):
    filename = r'book.csv'
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        try:
            next(reader)
        except StopIteration:
            pass
        for row in reader:
            book = Book_data(row[0], row[1], float(row[2]), int(row[3]))
            dic.append(book)

def blwfile(dic):
    filename = r'blend.csv'
    csvf = open(filename, 'w', newline='')
    writer = csv.writer(csvf)
    writer.writerow(['编号', '书名', '价格', '借出数量'])
    for i in dic:
        writer.writerow([i.book_id, i.book_name, i.book_price, i.book_num])
    csvf.close()

def blrfile(dic):
    filename = r'blend.csv'
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        try:
            next(reader)
        except StopIteration:
            pass
        for row in reader:
            userd = user_data(row[0], row[1], row[2], row[3])
            dic.append(userd)

def infowfile(dic):
    filename = r'use_info.csv'
    csvf = open(filename, 'w', newline='')
    writer = csv.writer(csvf)
    writer.writerow(['用户名', '姓名', '性别', '手机号'])
    for i in dic:
        writer.writerow([i.user, i.user_name, i.user_sex, i.user_tel])
    csvf.close()

def inforfile(dic):
    filename = r'user_info.csv'
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        try:
            next(reader)
        except StopIteration:
            pass
        for row in reader:
            book = Book_data(row[0], row[1], float(row[2]), int(row[3]))
            dic.append(book)

def show_id():
    yrfilezm(user.dic)
    bdrfile(book_Manage.book_data)
    blrfile(book_Manage.book_bor)
    while True:
        print("\t-----选择 身份-----")
        print("\t\t1、用户")
        print("\t\t2、管理员")
        print("\t\t0、返回")
        a = int(input("请选择："))
        if a == 0:
            break
        elif a == 2:
            mishi = input("请输入密匙：    （输入exit可退出）")  # 密匙为：11110000
            if mishi == "11110000":
                print("欢迎你，管理员！")
                grfilezm(Admin.ad_dic)
                os.system("pause")
                admin = Admin()
                admin.ad_menu()
            elif mishi == "exit":
                print("退出成功！")
                exit()
            else:
                print("密匙错误！")
                os.system("pause")
        elif a == 1:
            print("欢迎你，用户！")
            u = user()
            u.show_menu()
            os.system("pause")
        else:
            print("error")
            os.system("pause")


def hide_paswod():
    li = []
    while 1:
        ch = msvcrt.getch()
        # 回车
        if ch == b'\r':
            msvcrt.putch(b'\n')
            break
        # 退格
        elif ch == b'\x08':
            if li:
                li.pop()
                msvcrt.putch(b'\b')
                msvcrt.putch(b' ')
                msvcrt.putch(b'\b')
        else:
            li.append(ch)
            msvcrt.putch(b'*')
    return b''.join(li).decode()


class user:
    dic = {}

    def show_menu(self):
        while True:
            print("\t-----请选择如下功能-----")
            print("\t\t1、登录")
            print("\t\t2、注册")
            print("\t\t0、退出")
            num = int(input("请输入序号："))
            if num == 0:
                exit()
            elif num == 1:
                n = 0
                self.login(n)
                break
            elif num == 2:
                self.logon()
            else:
                print("error!")

    def login(self, n):
        print("用户登陆")
        name = input("账号：")
        if not user.dic.get(name, False):
            print("该账户不存在！")
            return
        print(f"请输入账号为{name}的密码：", end='')
        password = hide_paswod()
        if user.dic[name] != password:
            n += 1
            print(f"账号或者密码有误，请重试！({n})")
            self.login(n)
            if n == 3:
                print("密码输错次数过多！")
                exit()
        else:
            print("登录成功！")
            os.system("pause")
            book_manage = book_Manage()
            book_manage.run(0)

    def logon(self):
        name = input("请输入你要注册的账号：")
        while True:
            name = name.replace("傻", '*').replace("蠢", '*').replace("笨", '*').replace("呆", '*').replace("愚", '*')
            if '*' in name:
                print(f"用户{name}用户名不可注册！请重新设置账号。")
                name = input("请输入你要注册的账号：")
            elif user.dic.get(name, False):
                print("该用户已经存在！请重新设置账号。")
                os.system("pause")
                name = input("请输入你要注册的账号：")
            else:
                break
        print("请输入你要设置的密码：（字母、数字混合）", end='')
        password = hide_paswod()
        while True:
            if len(password) < 6:
                print("密码过短，请重新设置！")
                password = input("请输入你要设置的密码：（字母、数字混合）")
            elif password.isdigit():
                print("密码过于简单，请重新设置！")
                print(1)
                password = input("请输入你要设置的密码：（字母、数字混合）")

            elif password.isalpha():
                print(2)
                print("密码过于简单，请重新设置！")
                password = input("请输入你要设置的密码：（字母、数字混合）")

            else:
                break
        print("注册成功！")
        user.dic[name] = password
        ywfilezm(user.dic)
        os.system("pause")


class Admin:
    ad_dic = {}

    def ad_menu(self):
        while True:
            print("\t-----请选择如下功能-----")
            print("\t\t1、登录")
            print("\t\t2、注册")
            print("\t\t0、退出")
            num = int(input("请输入序号："))
            if num == 0:
                exit()
            elif num == 1:
                i = 0
                self.ad_login(i)
            elif num == 2:
                self.ad_logon()
            else:
                print("error!")
                os.system("pause")

    def ad_login(self, i):
        print("管理员登陆")
        name = input("账号：")
        if not Admin.ad_dic.get(name, False):
            print("该不存在！")
            return
        print(f"请输入账号为{name}的密码：", end='')
        password = hide_paswod()
        if Admin.ad_dic[name] != password:
            i += 1
            print(f"账号或者密码有误，请重试！({i})")
            if i == 3:
                print("密码输错次数过多！")
                exit()
            self.ad_login(i)
        else:
            print("登录成功！")
            self.choose_menu()
            os.system("pause")

    def ad_logon(self):
        name = input("请输入你要注册的账号：")
        while True:
            name = name.replace("傻", '*').replace("蠢", '*').replace("笨", '*').replace("呆", '*').replace("愚", '*')
            if '*' in name:
                print(f"用户{name}用户名不可注册！请重新设置账号。")
                name = input("请输入你要注册的账号：")
            elif Admin.ad_dic.get(name, False):
                print("该用户已经存在！请重新设置账号。")
                os.system("pause")
                name = input("请输入你要注册的账号：")
            else:
                break
        print("请输入你要设置的密码：（字母、数字混合）", end='')
        password = hide_paswod()
        while True:
            if len(password) < 6:
                print("密码过短，请重新设置！")
                password = input("请输入你要设置的密码：（字母、数字混合）")
            elif password.isdigit():
                print("密码过于简单，请重新设置！")
                print(1)
                password = input("请输入你要设置的密码：（字母、数字混合）")

            elif password.isalpha():
                print(2)
                print("密码过于简单，请重新设置！")
                password = input("请输入你要设置的密码：（字母、数字混合）")

            else:
                break
        print("注册成功！")
        Admin.ad_dic[name] = password
        gwfilezm(Admin.ad_dic)
        os.system("pause")

    def choose_menu(self):
        while True:
            print('''
        1、用户信息维护页面
        2、图书借阅页面
        0、退出系统
                    ''')
            num = int(input("请输入序号："))
            if num == 0:
                exit()
            elif num == 1:
                ad_func = Ad_func()
                ad_func.menu()
            elif num == 2:
                book_manage = book_Manage()
                book_manage.run(1)


class user_data:
    def __init__(self, userid: str, user_name: str, user_sex: str, user_tel: str):
        self.user = userid
        self.user_name = user_name
        self.user_sex = user_sex
        self.user_tel = user_tel

    def __str__(self):
        return f'{self.user_name}, {self.user_sex}, {self.user_tel}'


class Ad_func:
    user_lis = []

    def menu(self):
        inforfile(Ad_func.user_lis)
        while True:
            print('''
| ------------------------ |
|欢迎使用图书馆借阅管理系统V 2.0 |
|  ————用户信息维护页————     |
|    1、添加用户信息          |
|    2、删除用户信息          |
|    3、修改用户信息          |
|    4、显示用户信息          |
|    0、退出系统             |
|------------------------- |
                ''')
            num = int(input("请输入序号："))
            if num == 0:
                infowfile(Ad_func.user_lis)
                exit()
            elif num == 1:
                self.Ad_info()
            elif num == 2:
                self.Del_info()
            elif num == 3:
                self.Mod_info()
            elif num == 4:
                self.Pri_info()
            else:
                print("error!")
                os.system("pause")

    def Ad_info(self):
        use = input("请输入要添加的用户名：")
        if not user.dic.get(use, False):
            print("该用户不存在！")
            os.system("pause")
            return
        user_name = input("请输入用户姓名：")
        user_sex = input("请输入用户性别：")
        user_tel = input("请输入用户手机号：")
        userdata = user_data(use, user_name, user_sex, user_tel)
        Ad_func.user_lis.append(userdata)
        print("添加成功！")
        os.system("pause")

    def Del_info(self):
        use = input("请输入要删除用户的用户名：")
        for i in Ad_func.user_lis:
            if use == i.user:
                print("找到用户信息！")
                Ad_func.user_lis.remove(i)
                print("删除成功！")
                break
        else:
            print("该用户不存在！")
        os.system("pause")

    def Mod_info(self):
        if user.dic == {}:
            print("信息表为空！")
            os.system("pause")
            return
        use = input("请输入要修改用户的用户名：")
        for i in Ad_func.user_lis:
            if use == i.user:
                print("找到用户信息！")
                print(f"用户名：{i.user}，姓名：{i.user_name}，性别：{i.user_sex}，手机号：{i.user_tel}")
                choose = input("是否修改用户姓名？(y/other)")
                if choose == 'y' or choose == 'Y':
                    i.user_name = input("请输入修改的用户姓名：")
                choose = input("是否修改用户性别？(y/other)")
                if choose == 'y' or choose == 'Y':
                    i.user_sex = input("请输入修改的用户性别：")
                choose = input("是否修改用户手机号？(y/other)")
                if choose == 'y' or choose == 'Y':
                    i.user_name = input("请输入修改的用户手机号：")
                print("修改成功！")
                print("修改后的结果：")
                print(f"用户名：{i.user}，姓名：{i.user_name}，性别：{i.user_sex}，手机号：{i.user_tel}")
                break
        else:
            print("该用户不存在！")
        os.system("pause")

    def Pri_info(self):
        while True:
            print('''
1、单用户查询
2、全部用户
0、返回
            ''')
            num = int(input("请输入序号："))
            if num == 0:
                break
            elif num == 1:
                use = input("请输入要查询的用户名：")
                for i in Ad_func.user_lis:
                    if use == i.user:
                        print("找到用户信息！")
                        print(
                            f"用户名：{i.user}，姓名：{i.user_name}，性别：{i.user_sex}，手机号：{i.user_tel}")
                else:
                    print("该用户不存在！")
                    os.system("pause")
            elif num == 2:
                if user.dic == {}:
                    print("信息表为空！")
                    os.system("pause")
                    return
                for i in Ad_func.user_lis:
                    print(f"用户名：{i.user}，姓名：{i.user_name}，性别：{i.user_sex}，手机号：{i.user_tel}")
                else:
                    break


class Book_data:
    def __init__(self, book_id: str, book_name: str, book_price: float, book_num: int):
        self.book_id = book_id
        self.book_name = book_name
        self.book_price = book_price
        self.book_num = book_num

    def __str__(self):
        return f'编号：{self.book_id}, 书名：{self.book_name}, 价格：{self.book_price}, 数量：{self.book_num}'


class book_Manage:

    book_data = []
    book_bor = []

    def run(self, Rt: int):
        if Rt == 1:
            while True:
                self.Menu_vip()
                sel = int(input("请选择："))
                if sel == 0:
                    print("退出成功！")
                    bdwfile(book_Manage.book_data)
                    blwfile(book_Manage.book_bor)
                    exit()
                elif sel == 1:
                    self.add_book()
                elif sel == 2:
                    self.del_book()
                elif sel == 3:
                    self.modify_book()
                elif sel == 4:
                    self.search_book()
                elif sel == 5:
                    self.show_book()
                elif sel == 6:
                    self.show_lend()
                elif sel == 7:
                    bdwfile(book_Manage.book_data)
                    blwfile(book_Manage.book_bor)
                    show_id()
                else:
                    print("error")
        else:
            while True:
                self.Menu_people()
                sel = int(input("请选择："))
                if sel == 0:
                    print("退出成功！")
                    bdwfile(book_Manage.book_data)
                    blwfile(book_Manage.book_bor)
                    exit()
                elif sel == 1:
                    self.show_book()
                elif sel == 2:
                    self.lend_book()
                elif sel == 3:
                    self.retu_book()
                elif sel == 4:
                    self.search_book()
                elif sel == 5:
                    self.show_lend()
                elif sel == 6:
                    bdwfile(book_Manage.book_data)
                    blwfile(book_Manage.book_bor)
                    show_id()
                    break
                else:
                    print("error")

    def Menu_vip(self):
        print("\t-------管理员界面-------")
        print("\t\t1、添加书籍")
        print("\t\t2、删除书籍")
        print("\t\t3、修改图书信息")
        print("\t\t4、查找图书")
        print("\t\t5、总览图书")
        print("\t\t6、展示已借出图书信息")
        print("\t\t7、返回主登陆页面")
        print("\t\t0、退出系统")

    def Menu_people(self):
        print("\t-------用户界面-------")
        print("\t\t1、总览书籍")
        print("\t\t2、借阅图书")
        print("\t\t3、归还图书")
        print("\t\t4、查询图书")
        print("\t\t5、展示已借出图书信息")
        print("\t\t6、返回登录页面")
        print("\t\t0、退出系统")

    def add_book(self):
        book_id = input("请输入要添加的图书编号：")
        for i in book_Manage.book_data:
            if i.book_id == book_id:
                print("该图书已经存在！将会为该图书增加数量！")
                n = int(input("请输入要添加的图书数量："))
                if n >= 0:
                    i.book_num += n
                    print(book_Manage.book_data)
                else:
                    print("error,添加失败！")
        book_name = input("请输入要添加的图书名：")
        for i in book_Manage.book_data:
            if i.book_name == book_name:
                print("该图书已经存在！将会为该图书增加数量！")
                n = int(input("请输入要添加的图书数量："))
                if n >= 0:
                    i.book_num += n
                    print(book_Manage.book_data)
                else:
                    print("error,添加失败！")
        book_price = float(input("请输入要添加的图书价格："))
        book_num = int(input("请输入要添加的图书数量："))
        book = Book_data(book_id, book_name, book_price, book_num)
        book_Manage.book_data.append(book)
        print(book)  # 打印信息
        print("添加成功！")
        os.system("pause")

    def del_book(self):  # 删除图书
        del_name = input('请输⼊要删除的书籍名称：')  # 用户输入目标图书名
        # 如果用户输入的目标存在则删除，否则提示目标不存在
        for i in book_Manage.book_data:  # 遍历图书信息列表
            if i.book_name == del_name:  # 查找图书是否存在
                book_Manage.book_data.remove(i)  # 删除图书信息
                print("成功删除该图书信息！")
                print("\n")
                break
        else:
            print("查无此书！")
            print("\n")
        print(book_Manage.book_data)  # 打印图书列表，验证删除功能

    def modify_book(self):  # 修改图书信息
        name = input('请输⼊要修改的书籍名称：')  # 用户输入目标名称

        # 如果用户输入的目标存在，则修改信息，否则提示图书不存在
        for i in book_Manage.book_data:  # 遍历图书信息列表
            if i.book_name == name:  # 查找图书是否存在
                print("找到图书！")
                print(f'编号：{i.book_id}, 书名：{i.book_name}, 价格：{i.book_price}, 数量：{i.book_num}')
                # 更改学员信息
                choose = input("是否修改书籍编码？(y/other)")
                if choose == 'y' or choose == 'Y':
                    i.book_id = input('请输⼊修改的书籍编码：')
                choose = input("是否修改书籍名称？(y/other)")
                if choose == 'y' or choose == 'Y':
                    i.book_name = input('请输⼊修改的书籍名称：')
                choose = input("是否修改书籍价格？(y/other)")
                if choose == 'y' or choose == 'Y':
                    i.book_price = float(input('请输⼊修改的书籍价格：'))
                choose = input("是否修改书籍数量？(y/other)")
                if choose == 'y' or choose == 'Y':
                    i.book_num = int(input('请输入修改的书籍数量：'))
                print("修改成功！")
                print("修改后的结果：")
                print("成功修改该图书信息！")
                print(
                    f'编号：{i.book_id}, 书名：{i.book_name}, 价格：{i.book_price}, 数量：{i.book_num}')  # 打印图书信息，验证是否更改成功
                os.system("pause")
                break
        else:
            print('查无此书！')
            os.system("pause")

    def search_book(self):
        search_name = input("请输入要查询的书名：")
        for i in book_Manage.book_data:
            if search_name == i.book_name:
                print("找到图书！")
                print(f'编号：{i.book_id}, 书名：{i.book_name}, 价格：{i.book_price}, 数量：{i.book_num}')
                os.system("pause")
                break
        else:
            print("查无此书！")
            os.system("pause")

    def show_book(self):  # 显示所有图书信息
        print('[编号,书名,价格,数量]')  # 打印信息名称
        for i in book_Manage.book_data:  # 遍历信息列表
            print(f'[{i.book_id},{i.book_name},{i.book_price},{i.book_num}]')  # 打印图书信息

    def show_lend(self):  # 显示所有借出图书信息
        print('[编号,书名,价格,已经借出数量]')  # 打印信息名称
        for i in book_Manage.book_bor:
            print(f'[{i.book_id},{i.book_name},{i.book_price},{i.book_num}]')
            # 遍历信息列表
            # 打印图书信息
            os.system("pause")
            break
        else:
            print("暂时没有图书借出！\n")
            os.system("pause")

    def lend_book(self):
        name = input("请输入你要借的书名：")
        for i in book_Manage.book_data:
            if i.book_name == name:
                print("找到图书！")
                print(f'编号：{i.book_id}, 书名：{i.book_name}, 价格：{i.book_price}, 数量：{i.book_num}')
                if i.book_num == 0:
                    print("该书已经被借走完！")
                    print("输入任意键返回\n")
                    os.system("pause")
                    return
                while True:
                    num = int(input("请输入你要借的图书数量："))
                    if i.book_num > num:
                        i.book_num -= num
                        for j in self.book_bor:
                            if j.book_name == name:
                                j.book_num += num
                                break
                        else:
                            book = Book_data(i.book_id, i.book_name, i.book_price, num)
                            book_Manage.book_bor.append(book)
                        print("借用成功！")
                        return
                    elif i.book_num < num:
                        print("数量不够!")
                        os.system("pause")
                    else:
                        print("error")
                        os.system("pause")

    def retu_book(self):
        name = input("请输入要归还的图书名：")
        for i in book_Manage.book_bor:
            if i.book_name == name:
                num = int(input("请输入要归还的数量："))
                if i.book_num < num:
                    print(f"借的书不足{num}本！")
                    os.system("pause")
                    return
                elif i.book_num > num:
                    for k in book_Manage.book_data:
                        if k.book_name == name:
                            k.book_num += num
                            print("归还成功！")
                            os.system("pause")
        else:
            print(f"书名为{name}的书未被借用！")
            os.system("pause")


if __name__ == '__main__':
    with open('user.csv', 'a') as us1:
        pass
    with open('admin.csv', 'a') as us2:
        pass
    with open('book.csv', 'a') as us3:
        pass
    with open('blend.csv', 'a') as us4:
        pass
    with open('user_info.csv', 'a') as us5:
        pass
    show_id()
