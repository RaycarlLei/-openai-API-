README
简介
这个Python脚本主要用于读取文本文件中的代码，并将其分割成多个部分以应对OpenAI API的token长度限制。然后，利用OpenAI的GPT-3模型，为每一部分的代码生成相应的中文注释。最后，将生成的注释保存到一个新的文本文件中。

使用步骤
安装依赖
首先，你需要安装以下Python库：

bash
Copy code
pip install openai
设置API密钥
请将下面的代码行中的 'sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' 替换为你自己的OpenAI API密钥：

python
Copy code
openai.api_key = 'sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
输入文件
该脚本默认读取的文件名为 code_in.txt。将你想要添加注释的代码文件命名为 code_in.txt，然后放在与脚本相同的目录下。

该脚本尝试使用utf-8，latin-1和cp1252三种编码打开文件，如果文件不能用这三种编码打开，代码将会被设置为空字符串。

执行脚本
在终端中，使用以下命令来执行脚本：

bash
Copy code
python <你的脚本名称>.py
脚本首先将会尝试以不同的编码格式打开输入文件，并读取其中的代码。然后，脚本会创建一个新的文件夹，并将代码按照每个部分最多包含1000个字符的规则进行分割，将每个部分保存到新文件夹中的一个新的文本文件中。默认的文件夹名称为 splitted_code_后面跟着当前的时间戳。

然后，脚本会使用OpenAI的GPT-3模型为每一部分的代码生成相应的中文注释。这一过程可能需要一些时间，具体取决于代码的长度和模型的响应速度。

最后，将生成的所有注释拼接起来，并保存到一个新的文本文件中。默认的输出文件名称为 code_out_后面跟着当前的时间戳。

注意事项
确保你的代码文件是用utf-8，latin-1或cp1252编码的。如果不是，可能会导致脚本无法正确打开和读取文件。
由于OpenAI API的token长度限制，如果你的代码过长，可能需要将其分割成多个部分。这个脚本默认的分割规则是每个部分最多包含1500个字符，但你可以根据需要进行调整。
