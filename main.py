# -*- coding: utf-8 -*-
import json
import requests
# 在下面输入你的cookie
cookie = '你的cookie'
# 在上面输入你的cookie
headers = {
    'authority': 'www.xuetangx.com',
    'accept': 'application/json, text/plain, */*',
    'django-language': 'zh',
    'x-client': 'web',
    'accept-language': 'zh',
    'xtbz': 'xt',
    'user-agent': 'jdapp;android;8.4.2;8.0.0;;network/wifi;model/Mi Note 2;osVer/26;appBuild/71043;psn/|7;psq/1;uid/;adk/;ads/;pap/JA2015_311210|8.4.2|ANDROID 8.0.0;osv/8.0.0;pv/2.23;jdv/;ref/com.jingdong.app.mall.WebActivity;partner/huawei;apprpd/Home_Main;Mozilla/5.0 (Linux; Android 8.0.0; Mi Note 2 Build/OPR1.170623.032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36',
    'x-csrftoken': 'undefined',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.xuetangx.com/learn/HNU03031001055/HNU03031001055/4231538/chapter',
    'cookie': cookie,
}
params = (
    ('cid', '4231538'),
    ('sign', 'HNU03031001055'),
)
response = requests.get('https://www.xuetangx.com/api/v1/lms/learn/course/chapter', headers=headers, params=params)
mJson = json.loads(response.text)
course_chapter = mJson['data'].get('course_chapter')
for i in course_chapter:
    mCourse_chapter = json.dumps(eval(str(i)))
    section_leaf_list = i.get('section_leaf_list')
    for m in range(len(section_leaf_list)):
        eachChapter = section_leaf_list[m]
        leaf_list = eachChapter['leaf_list']
        for j in leaf_list:
            leaf_listReal = j
            courseId = leaf_listReal['id']
            print(j['name'] + ':')
            print('id:' + str(courseId))
            headers = {
                'authority': 'www.xuetangx.com',
                'x-mina-sessid': 'null',
                'django-language': 'zh',
                'accept-language': 'zh',
                'user-agent': 'jdapp;android;8.4.2;8.0.0;;network/wifi;model/Mi Note 2;osVer/26;appBuild/71043;psn/|7;psq/1;uid/;adk/;ads/;pap/JA2015_311210|8.4.2|ANDROID 8.0.0;osv/8.0.0;pv/2.23;jdv/;ref/com.jingdong.app.mall.WebActivity;partner/huawei;apprpd/Home_Main;Mozilla/5.0 (Linux; Android 8.0.0; Mi Note 2 Build/OPR1.170623.032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36',
                'platform-id': '0',
                'accept': 'application/json, text/plain, */*',
                'x-client': 'apph5',
                'xtbz': 'xt',
                'university-id': '0',
                'x-csrftoken': 'undefined',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.xuetangx.com/h5/homework/HNU03031001055/4231538/6325445?avatar=http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2FQLR5aKwLYaNuMIHqZHs53gtEdTW2TjibsdDnjeia2IK1ks8L3q8tibUdmicoWzaoAe5ic29L2Lh94ehlicnthog0tGJS1tDg1icEVLG%2F132&name=Xayah&user_number=null&term=latest&university_id=0&user_role=null&sessionid=null&csrftoken=undefined',
                'cookie': cookie,
            }
            params = (
                ('sign', 'HNU03031001055'),
                ('term', 'latest'),
                ('uv_id', '0'),
            )
            response = requests.get(
                'https://www.xuetangx.com/mooc-api/v1/lms/learn/leaf_info/4231538/' + str(courseId) + '/',
                headers=headers, params=params)
            mJson = json.loads(response.text)
            mLeaf_type_id = mJson['data']['content_info']['leaf_type_id']
            print('leaf_type_id:' + str(mLeaf_type_id))
            print('♥♥♥♥♥♥♥♥')
            try:
                # 正常的操作
                headers = {
                    'authority': 'www.xuetangx.com',
                    'accept': 'application/json, text/plain, */*',
                    'django-language': 'zh',
                    'x-client': 'web',
                    'accept-language': 'zh',
                    'xtbz': 'xt',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
                    'content-type': 'application/json',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://www.xuetangx.com/learn/HNU03031001055/HNU03031001055/4231538/exercise/6325463',
                    'cookie': cookie,
                }
                response = requests.get(
                    'https://www.xuetangx.com/api/v1/lms/exercise/get_exercise_list/' + str(mLeaf_type_id) + '/',
                    headers=headers)
                mJson = json.loads(response.text)
                mDescription = mJson['data']['description']
                mName = mJson['data']['name']
                problems = mJson['data'].get('problems')
                for i in problems:
                    mAnswer = str(i['user']['answer']).replace('[', '').replace(']', '').replace('\'', '')
                    print(mAnswer)
            except:
                # 发生异常，执行这块代码
                print('♥♥♥♥♥♥♥♥')
                print('⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐')
                print('---------------------------------------------------------------')

            else:
                # 如果没有异常执行这块代码
                print('♥♥♥♥♥♥♥♥')
                print('⭐⭐⭐本章答案获取完成⭐⭐⭐')
                print('---------------------------------------------------------------')

'''
D:\anaconda3\python.exe E:/ProgramDesign/PythonProjects/xuetangx/main.py
进入新时代:
id:6325438
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
做时代新人:
id:6325441
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
提升思想道德素质与法治素养:
id:6325443
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
绪论--单元测试:
id:6325445
leaf_type_id:594823
♥♥♥♥♥♥♥♥
B
A
C
C
A
ABCDE
ABCDE
ABCDE
B
B
B
A
B
♥♥♥♥♥♥♥♥
⭐⭐⭐本章答案获取完成⭐⭐⭐
---------------------------------------------------------------
正确认识人的本质:
id:6325453
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
个人与社会的辩证关系:
id:6325455
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
人生目的:
id:6325457
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
积极进取的人生态度:
id:6325458
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
人生价值及其评价:
id:6325460
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
反对错误人生观:
id:6325461
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
第一章--单元测试:
id:6325463
leaf_type_id:594830
♥♥♥♥♥♥♥♥
A
B
A
A
B
A
D
C
ABC
ABDE
ABD
BCD
ABCD
A
A
B
B
B
B
♥♥♥♥♥♥♥♥
⭐⭐⭐本章答案获取完成⭐⭐⭐
---------------------------------------------------------------
什么是理想:
id:6325471
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
什么是信念:
id:6325474
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
中国特色社会主义是我们的共同理想:
id:6325476
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
理想与现实的关系:
id:6325478
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
为实现中国梦注入青春能量:
id:6325480
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
第二章--单元测试:
id:6325481
leaf_type_id:594835
♥♥♥♥♥♥♥♥
C
C
A
D
B
D
D
C
B
D
BCD
ABC
ABC
ABC
ABCD
true
true
true
false
false
♥♥♥♥♥♥♥♥
⭐⭐⭐本章答案获取完成⭐⭐⭐
---------------------------------------------------------------
重精神是中华民族的优秀传统:
id:6325487
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
中国精神的内容构成及其作用:
id:6325489
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
爱国主义的科学内涵:
id:6325492
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
新时代的爱国主义:
id:6325493
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
弘扬改革创新精神:
id:6325495
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
第三章--单元测试:
id:6325496
leaf_type_id:594839
♥♥♥♥♥♥♥♥
A
D
B
C
B
A
A
A
B
C
A
A, B, C, D, E
A, B, C, D, E
A, B, C, D
A, B, C, D, E
true
true
false
true
true
♥♥♥♥♥♥♥♥
⭐⭐⭐本章答案获取完成⭐⭐⭐
---------------------------------------------------------------
社会主义核心价值观的基本内容:
id:6325505
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
当代中国发展进步的精神指引:
id:6325509
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
社会主义核心价值观的历史底蕴:
id:6325511
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
社会主义核心价值观的道义力量:
id:6325515
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
做社会主义核心价值观的积极践行者:
id:6325517
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
第四章--单元测试:
id:6325520
leaf_type_id:594846
♥♥♥♥♥♥♥♥
ABDE
ABC
BCD
ACE
ABD
BCD
ABCD
B
A
B
B
A
A
B
C
B
A
C
D
B
D
ABD
♥♥♥♥♥♥♥♥
⭐⭐⭐本章答案获取完成⭐⭐⭐
---------------------------------------------------------------
道德的内涵、起源、本质:
id:6325532
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
道德的功能、作用、变化发展:
id:6325534
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
社会主义道德的核心和原则:
id:6325536
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
社会主义道德建设的思想资源之中华传统美德:
id:6325540
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
社会主义道德建设的思想资源之中国革命道德和人类文明优秀道德成果:
id:6325544
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
社会公德:
id:6325548
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
职业道德:
id:6325550
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
家庭美德:
id:6325554
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
个人品德:
id:6325556
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
学习道德模范、参与志愿活动、引领社会风尚:
id:6325559
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
第五章--单元测试（一）:
id:6325562
leaf_type_id:594855
♥♥♥♥♥♥♥♥
D
B
A
B
D
C
D
A
♥♥♥♥♥♥♥♥
⭐⭐⭐本章答案获取完成⭐⭐⭐
---------------------------------------------------------------
第五章--单元测试 （二）:
id:6325565
leaf_type_id:594858
♥♥♥♥♥♥♥♥
B
B
D
C
A, B, C, D
A, B, C, D, E
A, B, C, D, E
B, C, D
A, B, C
A, B, D
A, B, C, D, E
A, B, C, D
A, B, C, D
false
true
true
false
♥♥♥♥♥♥♥♥
⭐⭐⭐本章答案获取完成⭐⭐⭐
---------------------------------------------------------------
法律及其历史发展:
id:6325577
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
我国社会主义法律:
id:6325579
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
我国宪法确立的基本原则:
id:6325581
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
我国的国家制度:
id:6325584
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
建设中国特色社会主义法治体系:
id:6325588
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
法律权利及其特征:
id:6325630
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
法律义务及其特征:
id:6325634
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
依法行使权利与履行义务:
id:6325637
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
第六章--单元测试（一）:
id:6325597
leaf_type_id:594871
♥♥♥♥♥♥♥♥
B
D
B
B
A
A
B
A
B, C, D
B, C, D, E
A, D
A, B, C, E
false
true
true
false
true
true
true
false
♥♥♥♥♥♥♥♥
⭐⭐⭐本章答案获取完成⭐⭐⭐
---------------------------------------------------------------
第六章--单元测试（二）:
id:6325616
leaf_type_id:594876
♥♥♥♥♥♥♥♥
B
D
D
D
A
C
B
B
A, B
A, B, C, D, E
A, B, C, D, E
A, B, C, D, E
false
true
true
true
false
false
true
false
♥♥♥♥♥♥♥♥
⭐⭐⭐本章答案获取完成⭐⭐⭐
---------------------------------------------------------------
第六章--单元测试（三）:
id:6325590
leaf_type_id:594866
♥♥♥♥♥♥♥♥
D
A
D
A
B
C
A
A, B, D
A, B, C, D, E
A, B, C
true
false
true
true
true
false
true
♥♥♥♥♥♥♥♥
⭐⭐⭐本章答案获取完成⭐⭐⭐
---------------------------------------------------------------
法治思维的含义:
id:8547012
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
如何理解法治思维的基本内容:
id:8547013
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
怎样培养法治思维:
id:8547014
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
美丽的湖南大学    我们的精神家园 （一）:
id:6325653
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
美丽的湖南大学    我们的精神家园（二）:
id:6325655
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
不屈的文脉:
id:6325659
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------
湖南大学“基础课程”宣讲片:
id:6325662
leaf_type_id:None
♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥
⭐⭐⭐本章没有测试题,跳过!⭐⭐⭐
---------------------------------------------------------------

Process finished with exit code 0

'''
