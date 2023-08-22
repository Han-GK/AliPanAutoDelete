import time
from typing import List
from aligo import Aligo
import os
if __name__ == '__main__':
    ali = Aligo()  # 第一次使用，会弹出二维码，供扫描登录
    user = ali.get_user()
    print("--------------------")
    print("用户名：" + user.nick_name)
    print("手机号：" + user.phone)
    time.sleep(1)
    print("登录成功🎉")
    print("请等待3秒...")
    time.sleep(3)
    print("--------------------")
    if __name__ == '__main__':
        ali = Aligo()
    drives = ali.list_my_drives()
    v2_user = ali.v2_user_get()
    resource_drive_id = v2_user.resource_drive_id
    ali.default_drive_id = resource_drive_id
    print("默认操作资源盘")
class CustomAligo(Aligo):
    """自定义 aligo """
    V3_FILE_DELETE = '/v3/file/delete'
    def clear_recyclebin(self, drive_id: str = None):
        """清空回收站"""
        drive_id = resource_drive_id
        response = self.post('/v2/recyclebin/clear', body={
            'drive_id': drive_id
        })
        return response.status_code == 202
ali = CustomAligo()
rr = ali.clear_recyclebin()
if rr : True
print("回收站清理成功")


