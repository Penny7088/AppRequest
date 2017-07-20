# -*- coding: utf8 -*-
import time
from uiautomator import device as d


class app_meituan:
    def __init__(self):
        print('====')

    def lunch_app(self):
        print('=lunch=')
        d(text="美团").click()
        self.cate()

    def cate(self):
        print('cate:all')
        time.sleep(5)
        if d(resourceId='com.sankuai.meituan:id/icon', className='android.widget.ImageView').exists:
            print('true')
            time.sleep(6)
            d(resourceId='com.sankuai.meituan:id/icon', className='android.widget.ImageView').click()
            time.sleep(6)
            d.wait.update()
            self.list_click()

    def list_click(self):
        d(text='全部', className='android.widget.TextView').click()
        d.press.back()
        d.dump("hierarchy.xml")
        info = d(className="android.widget.ListView", resourceId="android:id/list").info
        # print(info)
        conunt_ = info['childCount']
        for view in range(conunt_):
            self.check_pkg(view + 1)

    def check_pkg(self, positon):
        print(positon)
        index_positon_info = d(className="android.widget.ListView", resourceId="android:id/list") \
            .child_by_instance(positon).info
        print(index_positon_info)
        # class_name_ = index_positon_info['className']
        # if not class_name_ == 'android.widget.ListView':
        #     d(className="android.widget.ListView", resourceId="android:id/list") \
        #         .child_by_instance(positon).click()
        #     if class_name_ == 'android.widget.LinearLayout':
        #         print(class_name_)
        # info = d(className=class_name_).info()
        #         print(info)
        # d.wait(5)
        # d.press.back()


if __name__ == '__main__':
        app_meituan().list_click()
