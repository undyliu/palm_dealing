Scipalmist的作品简介
===================
#### 点击[这里](http://www.lihao7086.com:8001)查看我们的`官方主页`,里面有最详细的说明  
#### 点击[这里](https://github.com/KiyomiHan/palm_dealing)查看我们的`github`,里面有我们的所有代码 


## 我们的目的 ##
慢性病不可怕，可怕的是防治不及。  
根据手诊理论，我们身体某些特征会在手掌上有所体现，譬如色泽，纹路等。  
对于慢性病来说，在患者感觉不适之前，手掌上就已经有所体现。  
如果能够了解我们手掌所暗示的信息，我们就能够提前去医院诊断，避免小病拖成大病。  
中医手诊体系在这方面成果颇丰，我们希望能够将手诊理论借助现代工具进入寻常百姓家。  
虽然手诊预测不能完全准确，但是能够提供一种低沉本的概率预测慢性病的方法也是极有价值的。  


## 我们做了什么 ##
基于Azure云平台，我们做了一套自动诊断系统，能够根据一张手的图片给出预测结果。  
本着方便大众的目的，我们的客户端采用微信的小程序，尽可能少占用用户资源且跨平台。  
我们有两种模式：
* 大众模式。用户上传自己的数据得到诊断结果。面向的是普通群众。
* 专家模式。用户可以上传带有标签的数据，比如已经确诊冠心病患者的手掌。这将完善我们的神经网络。面向的是研究相关方面的学者及医护人员。

我们的项目是完全[开源](https://github.com/KiyomiHan/palm_dealing)的，任何人可以将我们的代码进行改进用作别的用处，也欢迎任何有价值的反馈，更期望得到相关部门所提供的数据。  

## 如何使用我们的作品 ##

打开微信扫描下面的二维码或者搜索小程序“Scipalmist”  
<div align = "center"><img src="readme_static/2dcode.png" width = "200" height = "200" alt="图片名称" align=center /> </div> 
进入程序后点击上传然后选择图片（照相或相册）。  
<div align = "center"><img src="readme_static/ui.png" width = "250" height = "400" alt="图片名称" align=center /> </div>
点击完成后就会上传，由于上传原图，所以需要一些上传时间。  
上传完毕后会自动显示两张图片（左右拖动），一张是手掌与各个roi的拼图，一张是诊断报告。  
<div align = "center"><img src="readme_static/hand.jpg" width = "700" height = "500" alt="图片名称" align=center /></div>
<div align = "center"><img src="readme_static/report.jpg" width = "300" height = "600" alt="图片名称" align=center /></div>
长按图片可保存，单击图片退出。  
