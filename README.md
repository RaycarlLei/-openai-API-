# README

**注意**：要运行这个脚本，你需要一个OpenAI的API密钥，并将其填入到脚本中的适当位置。

## 使用方法（基于Windows 10）

1. 安装Python（版本3.6或以上)。如果你还没有安装python，请参考[安装python](https://github.com/RaycarlLei/-openai-API-/tree/main#%E5%AE%89%E8%A3%85python)。

2. 打开script.py，将sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx替换为你的OpenAI API密钥。如果你还没有API，你可以在https://platform.openai.com/apps 获取你的API。

3. 将你想要自动注释的代码复制入名为'code_in.txt'的文件中。

4. 运行command.bat。脚本会自动创建一个新的文件夹，并将代码分割成多个部分，每个部分存放在一个单独的.txt文件中。然后，脚本会为每个部分的代码生成注释，并将注释后的代码写入一个新的输出文件中。

5. 查看脚本运行结果。结果会被写入一个带有当前时间的.txt文件中，并且脚本完成时会显示一个消息框，显示脚本运行所花费的时间。

   
## 脚本工作流程

1. 脚本首先设置OpenAI的API密钥，该密钥用于后续的API调用。

2. 获取当前的日期和时间，并将它们格式化为字符串。这个字符串被用于创建新的文件夹名。

3. 创建一个新的文件夹，该文件夹用于存放分割后的代码段。

4. 尝试使用不同的编码（utf-8, latin-1, cp1252）打开输入的代码文件。如果文件不能用某种编码打开，脚本会尝试下一个编码。

5. 脚本将读取的代码分割成多个部分，以便能够满足OpenAI API的token长度限制。默认情况下，每个部分最多包含1000个字符，但这个值可以自行修改。

6. 将每个部分的代码写入到新文件夹中的一个新的.txt文件中。

7. 选择OpenAI的模型引擎。默认的模型引擎是'text-davinci-003'。

8. 针对每一个代码部分，脚本会向OpenAI API发送一个请求，要求生成相应的代码注释。每个请求的结果会被添加到一个叫做`annotated_code`的字符串中。

9. 将添加了注释的代码写入一个新的输出文件中，文件名包含当前的时间。

10. 脚本完成后，会显示一个消息框，显示脚本运行所花费的时间。


## 安装python
1. 打开您的浏览器，访问官方 Python 网站：https://www.python.org/downloads/windows/。

2. 滚动页面并找到适合您的操作系统的最新版本。选择带有 "Windows installer" 标志的版本。
 
3. 下载 Python 安装程序（.exe 文件）后，双击运行它。

4. 在安装向导中，确保选中 "Add Python to PATH"（将 Python 添加到 PATH）选项。这将允许您在命令提示符下全局访问 Python。

5. 点击 "Customize installation"（自定义安装）按钮，以便选择其他安装选项。您可以按照默认设置继续，或者根据自己的需求进行选择。

6. 在可选功能页面上，确保选中 "pip"（Python 包管理器）和 "tcl/tk and IDLE"（Tcl/Tk 和 IDLE）。这些是常用的 Python 工具和库。

7. 在高级选项页面上，您可以选择修改安装路径或者直接使用默认设置。

8. 单击 "Install"（安装）按钮开始安装过程。

9. 安装完成后，打开命令提示符（按下 Win + R，输入 "cmd"，然后按下回车键）。在命令提示符下，输入 "python --version"（不包括引号）并按下回车键。如果安装成功，命令提示符将显示 Python 的版本号，例如 "Python 3.6.8"。
