import os

#parameter
folder=('1start','2stop','3connectdb','4disconnectdb','5connectplc','6disconnectplc','7exit','8nonsense')
index=(0,100,200,300,400,500,600,700)
text=(['启动检测','打开检测','运行检测','可以检测了','检测吧','检测','开始运行','开始吧','可以开始了','开始','开始了','启动吧','启动','可以启动了','运行了','可以运行了','运行','运行吧'],
      ['停止','停止检测','停止运行','停止了','停止吧','可以停止了','终止检测'],
      ['连接数据库','连接到数据库','连数据库','可以连数据库了','连到数据库','开始连数据库','开始连数据库了','开始连接数据库','连接数据库吧'],
      ['断开数据库','断开数据库吧','断开数据库了','断开数据库连接','不要连数据库了','不要连接数据库','数据库不连了','数据库断开了','数据库断开吧','终止数据库连接','中断数据库连接'],
      ['连接PLC','连接到PLC','连PLC','可以连PLC了','连到PLC','开始连PLC','开始连PLC了','开始连接PLC','连接PLC吧'],
      ['断开PLC','断开PLC吧','断开PLC了','断开PLC连接','不要连PLC了','不要连接PLC','PLC不连了','PLC断开了','PLC断开吧','终止PLC连接','中断PLC连接'],
      ['退出语音识别','不要语音识别了','不要语音识别','不要语音识别的功能了','语音识别停了吧','语音识别停止吧','退出语音识别吧','语音识别退出吧','终止语音识别','语音识别终止'],
      ['可以'])

for item in zip(folder,index,text):
      num=item[1]
      for each in item[2]:
            path=os.path.join(item[0],str(num)+'.txt')
            f=open(path,'w')
            f.write(each)
            f.close()
            num+=1