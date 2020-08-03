import json
from base64 import b64encode
from requests import Session, cookies


def main():
    session = Session()

    url_tmf_login = "http://xxx.xxx.xxx:30001/login/login"
    url_tmf_push = "http://xxx.xxx.xxx:30012/secApi/manage/api/package/batch-new-all"

    params = {
        'username': 'xxx',
        'password': 'xxx=='
    }

    try:
        # 注意这里没有用json.dumps，和后台服务器的要求有关系
        # 如果从fiddler里看到是JSON形式的，得dumps；如果是a=xx&b=xx&c=xx的，不要dumps
        # 另外, 如果是JSON格式, 除了dumps+data指定, 还可以不dumps, 直接用json=params也可以
        session.post(url_tmf_login, data=params)
        print("登录成功")
    except:
        print("调用失败")
        exit(1)

    with open("turntableNew.zip", "rb") as f:
        package = "data:;base64,"+b64encode(f.read()).decode("utf-8")

    # 文件上传要用到前面接口得到的一个cookie, app_id, 写死就好, 生产上的要先去截报文看
    cookie = cookies.RequestsCookieJar()
    cookie.set("app_id", "app-dcqa7xhy1m")

    header = {
        "Content-Type": "application/json;charset=UTF-8",
    }

    params = {
        "bid_str": "turntableNew",
        "package": package,
        "bid_type": 0,
        "info": "turntableNew",
        "product_id": "1156",
        "success": False,
        "isUpload": False,
        "platform": "[2,3]",
        "verify_type": 0,
        "expire_time": None,
        "frequency": 10,
        "loadmode": 2,
    }
    params = str.replace(str.replace(json.dumps(params), '": ', '":'), ', "', ',"')

    try:
        res = session.post(url_tmf_push, data=params, cookies=cookie, headers=header).json()
        # res自带json方法, 不用再自己loads
        print(res)
    except Exception as e:
        print(e)
        print("上传失败")



if __name__ == "__main__":
    main()




