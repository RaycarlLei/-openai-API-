import openai
import os
import time

# 将sk-xxxxxxxxxxxxxxxxxxxxxx替换为你的 API Key
openai.api_key = 'sk-xxxxxxxxxxxxxxxxxxxxxx'

# 尝试使用不同的编码打开文件
encodings = ['utf-8', 'latin-1', 'cp1252']
for encoding in encodings:
    try:
        with open('code_in.txt', 'r', encoding=encoding) as input_file:
            code = input_file.read()
        print(f'file opened with {encoding} successfully')
        break
    except UnicodeDecodeError:
        print(f'file can`t open with {encoding} ')
else:
    print('failed to indentify file encoding format')
    code = ''

# 为应对openai的token长度限制，将代码文件分成多个部分。默认值为每个部分最多包含1000个字符，可自行修改。
parts = [code[i:i+1000] for i in range(0, len(code), 1000)]
print('file splitted successfully')

annotated_code = ''
model_engine = 'text-davinci-002'
print('model engine selected successfully')

# 逐个处理
for i, part in enumerate(parts):
    #以下prompt可以自行修改，支持注释、debug、重构等等功能
    prompt = f'用中文详细地注释以下代码：\n{part}'
    print('prompt created successfully')

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    print(f'Part {i+1}/{len(parts)} annotated successfully')

    annotated_code += completions.choices[0].text

print('all code annotated successfully')

# 将注释后的代码写入带时间戳的文件
output_filename = f'code_out_{int(time.time())}.txt'
with open(output_filename, 'w') as output_file:
    output_file.write(annotated_code)
print(f'file written successfully to {output_filename}')
