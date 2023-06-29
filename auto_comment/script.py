import os
import time
import ctypes
import openai
import datetime


# 将sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx替换为你的 API Key
openai.api_key = 'sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


# 获取当前日期和时间
now = datetime.datetime.now()

# 将日期和时间格式化为字符串
formatted_now = now.strftime("%Y-%m-%d_%H-%M-%S")

# 使用格式化后的日期和时间来创建文件夹名称
folder_name = f"splitted_code_{formatted_now}"

# 创建新文件夹
os.makedirs(folder_name, exist_ok=True)

# 尝试使用不同的编码打开文件
encodings = ['utf-8', 'latin-1', 'cp1252']
for encoding in encodings:
    try:
        with open('code_in.txt', 'r', encoding=encoding) as input_file:
            code = input_file.read()# 读取文件内容
        print(f'file opened with {encoding} successfully')
        break
    except UnicodeDecodeError:
        print(f'file can`t open with {encoding} ')
else:
    print('failed to indentify file encoding format')
    code = ''

# 为应对openai的token长度限制，将代码文件分成多个部分。默认值为每个部分最多包含1000个字符，可自行修改。
parts = []
if len(code) > 0:
    lines = code.split('\n')
    part = ''
    for line in lines:
        if len(part) + len(line) > 1000:# 限制每个部分最多包含1000个字符
            parts.append(part)# 将每个部分添加到parts列表中
            part = line + '\n'
        else:
            part += line + '\n'
    if part:
        parts.append(part)
print(f'file splitted into {len(parts)} parts successfully')

# 将每个部分写入到新文件夹中的一个新.txt文件中
for i, part in enumerate(parts):
    with open(f"{folder_name}/part_{i+1}.txt", 'w', encoding='utf-8') as output_file:
        output_file.write(part)

annotated_code = ''

# model_engine = 'gpt-3.5-turbo-0301'
model_engine = 'text-davinci-003'
print(f'model engine {model_engine} selected successfully')

start_time = time.time()
for i, part in enumerate(parts):
    prompt = f'Please provide appropriate Chinese code comments for the given code snippet. Your reply should only consist of the code with embedded comments, and should not include any explanations outside of the code. If you believe no comments are necessary, respond with the original code input. Here is the code:""{part}""'

    part_time = time.time()

    print(f'Part {i+1}/{len(parts)} started at {time.strftime("%H:%M:%S", time.localtime())}')
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    print(f'Part {i+1}/{len(parts)} annotated successfully')
    print(f'Time taken for this part: {time.time() - part_time:.2f} seconds')
    total_time = time.time() - start_time
    minutes = total_time // 60
    seconds = total_time % 60
    print(f'Total time taken: {minutes:.0f} minutes and {seconds:.2f} seconds\n')

    annotated_code += completions.choices[0].text

print(f'Total time taken: {time.time() - start_time:.2f} seconds')

# 将注释后的代码写入带时间的文件
output_filename = f'code_out_{formatted_now}.txt'
with open(output_filename, 'w', encoding='utf-8') as output_file:
    output_file.write(annotated_code)
print(f'file written successfully to {output_filename}')


# 创建一个消息框来显示完成消息
ctypes.windll.user32.MessageBoxW(0, f"运行用时 {minutes:.0f} 分 {seconds:.2f} 秒", "脚本运行完成", 1)
