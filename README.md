
# 一、配置项目代码
`git clone https://github.com/Heavenhjs/demot2i.git`或者[下载压缩包](https://github.com/Heavenhjs/demot2i.git)
下载后的代码结构如下：
![在这里插入图片描述](https://img-blog.csdnimg.cn/366f31b2de6644bb81f74e6d124a7157.png)
其中：code文件夹放置模型主要代码，data放置数据集（如bird、coco），DAMSMencoders放置已经训练好的文本编码器和图像编码器。

# 二、配置虚拟环境
点击下载已经打包好的虚拟环境[demoEnv](%28https://1drv.ms/u/s!AlLisU6CMruCkFMZhgtuEb4iDvOy?e=2nFYdW%29)，将其放到Anaconda安装目录下的envs中，无需解压。比如D:\Anaconda3\envs：
![在这里插入图片描述](https://img-blog.csdnimg.cn/68b3ae9d2d7f443c91b444eddfc15e9e.png)
放入之后可以在anaconda prompt或者pycharm终端中输入：`conda info --envs`，如果显示有demoEnv则成功导入虚拟环境：
![在这里插入图片描述](https://img-blog.csdnimg.cn/823853c2ac2c48d1b617a4a9ae25e58c.png)

# 三、配置数据集
数据集已经打包上传至OneDrive，下载数据集[CUB-Bird](https://1drv.ms/u/s!AlLisU6CMruC0QKvjjmNjXzC9wRj?e=h0PC6y)，替换代码项目的data文件夹：
![在这里插入图片描述](https://img-blog.csdnimg.cn/8d160ba7c9db4d4da011fd76d0513e85.png)
# 四、开始运行
最终配置好的项目结构如下：
![在这里插入图片描述](https://img-blog.csdnimg.cn/5008aced3da4433188e51b86e325db17.png)
其中code/cfg里的yml文件存放模型的一些参数，code/miscc文件夹存放模型的选项和工具函数，DAMSM是深度注意多模态相似模块，dataset用于处理数据和加载dataloader，main是项目的入口文件，model是模型文件。

运行：
1、激活demoEnv环境:`conda activate demoEnv`
2、进入code目录，开始运行，模型进入训练：`python main.py --cfg cfg/bird.yml`
3、训练好了之后，将code/cfg/bird.yml中的B_VALIDATION 改为True，然后进入采样：`python main.py --cfg cfg/bird.yml`


