import requests
def get_sessionid():
    global headers_mi8
    data_mi8={
              "deviceUuid":"自己抓包",
              "appVersion":"8.5.3",
              "j_password":"   ",                    #md5加密
              "devicePlatform":"Android" ,                                       
              "deviceVersion":"8",                          
              "j_username":"学号",
              "deviceName":"MI6"
              }
    url="http://course-proxy2-mobile.buct.edu.cn/mobile/getSessionId.do"
    r=requests.post(url,headers=headers_mi8,data=data_mi8,allow_redirects=False)
    url="http://course-proxy2-mobile.buct.edu.cn/mobile/login_check.do"
    r=requests.post(url,headers=headers_mi8,data=data_mi8,allow_redirects=False)
    return (r.cookies)

def get_personal():
    global session_mi8
    global headers_mi8
    url="http://course-proxy2-mobile.buct.edu.cn/mobile/loginSuccess.do?callback=null"
    r=requests.get(url,headers=headers_mi8,cookies=session_mi8)
    cookies=dict(eval(r.text))
    session_mi8=cookies['sessionid']
    print("JSESSIONID="+session_mi8)
    return(r.text)

def work_info():
    global session_mi8
    global headers_mi8
    url="http://course-proxy2-mobile.buct.edu.cn/mobile/courseList.do"
    data_mi8={"context":""}
    headers1_mi8=headers_mi8
    headers1_mi8['Cookie']='JSESSIONID='+session_mi8
    r=requests.post(url,headers=headers1_mi8,data=data_mi8)
    return(r.text)

def work_windowssystem():
    pass
    global session_mi8
    global headers_mi8
    url="https://course-proxy2.buct.edu.cn/meol/jpk/course/layout/newpage/index.jsp?courseId=19566"
    data_mi8={"context":""}
    r=requests.post(url,headers=headers_mi8,data=data_mi8)
    r.encoding=r.apparent_encoding
    return (r.text)

headers_mi8={"User-Agent":"Dalvik/2.1.0 (Linux; U; Android 9; MI 8 MIUI/V11.0.4.0.PEACNXM)"}
session_mi8=get_sessionid()
get_personal()
subject_raw=dict(eval(work_info()))
subject=subject_raw['datas']  
f=open("任课老师工号与姓名.txt","wb+")
f.write(('{realname:^10}   {username:^20}   {coursename:^30}\n'.format(realname='姓名',username='工号',coursename='课程')).encode())

for i in subject:
     s=dict(i['tutor'])
     f.write(('{realname:^10}   {username:^20}   {coursename:^30}\n'.format(realname=s['realname'],username=s['username'],coursename=i['coursename'])).encode())
f.close()

#print(work_windowssystem())




