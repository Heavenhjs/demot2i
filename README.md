
# 一、Configure Project Code
Use git：`git clone https://github.com/Heavenhjs/demot2i.git` 
or [download package](https://github.com/Heavenhjs/demot2i.git)
The downloaded code structure is as follows:
![在这里插入图片描述](https://img-blog.csdnimg.cn/366f31b2de6644bb81f74e6d124a7157.png)
The code folder places the main code of the model, the data folder places the data set (such as bird and coco), and the damcoders place the trained text encoder and image encoder.

# 二、Configure Virtual Environment
Download the packaged virtual environment：[demoEnv](%28https://1drv.ms/u/s!AlLisU6CMruCkFMZhgtuEb4iDvOy?e=2nFYdW%29)，Put it into envs under the anaconda installation directory, and there is no need to extract it,such as D:\Anaconda3\envs：
![在这里插入图片描述](https://img-blog.csdnimg.cn/68b3ae9d2d7f443c91b444eddfc15e9e.png)
After putting it in, you can enter it in the anaconda prompt or pycharm terminal:`conda info --envs`，If demoEnv is displayed, the virtual environment is successfully imported:
![在这里插入图片描述](https://img-blog.csdnimg.cn/823853c2ac2c48d1b617a4a9ae25e58c.png)

# 三、Configure Dataset
The dataset has been packaged and uploaded to OneDrive. Download the dataset:[CUB-Bird](https://1drv.ms/u/s!AlLisU6CMruC0QKvjjmNjXzC9wRj?e=h0PC6y)，replace the data folder of the code project:
![在这里插入图片描述](https://img-blog.csdnimg.cn/8d160ba7c9db4d4da011fd76d0513e85.png)
# 四、Start Training
The final configured project structure is as follows:
![在这里插入图片描述](https://img-blog.csdnimg.cn/5008aced3da4433188e51b86e325db17.png)
The yml file in code/cfg stores some parameters of the model, the code/miscc folder stores options and tool functions of the model, DAMSM is a multi-modal similarity module for deep attention, dataset is used to process data and load dataloader, main is the entry file of the project, and model is the model file.

Run：
1、Activate demoEnv virtual environment:`conda activate demoEnv`
2、Enter the code directory, start running, and the model enters the training：`python main.py --cfg cfg/bird.yml`
3、After training，change B_VALIDATION to True in the bird.yml and then run `python main.py --cfg cfg/bird.yml` , the model enters the sampling.


