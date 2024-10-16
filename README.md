# Description
这是一个`虾米签`小程序自动签到脚本，使用`frida hook 函数`获取微信小程序`code`后直接调用虾米签后端api即可完成签到

# Environment
- 首先装库,建议使用virtualenv
> pip install virtualenv -i https://pypi.tuna.tsinghua.edu.cn/simple

- 创建虚拟环境
> virtualenv .venv

- 运行虚拟环境
> .venv\Scripts\activate

- 安装库
> pip install -r requirements.txt

- wx版本
>wxapk==8.0.49

- 一个能开adb的手机（推荐mumu模拟器）

# Usage
## Parameter
要自动签到，首先你得修改main.py中的相关参数,如下
- Checkout.py里GetCode方法中的`appid`
- Checkout.py里service_record，这是传递的打卡项目的参数，修改为你想要的
- 手机连接电脑或者打开mumu模拟器的adb，在main.py中修改ip和端口
## Run
```
.\.venv\Scripts\activate
python main.py
```

# Preference
[Hook_WeCHat_FaaS](https://github.com/FourTwooo/Hook_WeChat_FaaS)

