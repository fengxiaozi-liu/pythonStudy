##### Python生成日志

###### 日志等级

+ 优先级从小到大有五个等级
  1. debug ：调试信息
  2. info: 描述信息
  3. warning：警告信息
  4. error：错误信息
  5. critical：严重错误信息

###### Python中如何生成日志

+ logging模块

  + Python内置模块可以生成日志，包括可以设置日志等级，日志路径，日志文件回滚等

  + logging包括四个组件

    1. logger日志器：提供了应用程序的接口

       + ```python
         logger = logging.getLogger('logger')
         ```

    2. Handler处理器：通过logger在不同位置输出日志

       + ```Python 
         stream_handler = logger.SteamHandler() # 创建一个控制台日志处理器
         file_handler = logger.FileHandler(filename='要保存日志的路径',enconding='utf-8') # 创建一个文件日志处理器
         
         logger.addHandler(steam_handler)
         logger.addHandler(file_handler) # 将处理器加入到日志器中国
         ```

    3. Formator格式器：决定日志以什么样式显示

       + ```python 
         formator = logging.Formatter(fmt='%(asctime)s %(filename)s %(levlename)s %(message)s', datefmt='%Y/%m/%d/%X')  # 创建一个格式器
         steam_handler.setFormatter(formator) # 将格式器加入到处理器中国
         ```

    4. Filter过滤器：过滤哪些需要记录或者需要丢弃

       + 

+ 去除生成日志信息重复的问题

  + `用if`判断解决就好

    + ```python 
      if not logger.handlers:
      	....
      return logger
      ```

      

