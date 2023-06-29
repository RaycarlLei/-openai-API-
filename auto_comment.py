import os
import time
import openai

# 将sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 替换成你自己的API key
openai.api_key = 'sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# 创建新文件夹
folder_name = f"splitted_code_{int(time.time())}"
os.makedirs(folder_name, exist_ok=True)

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

# 为应对openai的token长度限制，将代码文件分成多个部分。默认值为每个部分最多包含1500个字符，可自行修改。
parts = []
if len(code) > 0:
    lines = code.split('\n')
    part = ''
    for line in lines:
        if len(part) + len(line) > 1500:
            parts.append(part)
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
model_engine = 'text-davinci-002'
print('model engine selected successfully')

start_time = time.time()
for i, part in enumerate(parts):
    prompt = f'Please provide corresponding Chinese code comments for the following code snippet. Your response should only consist of commented code and should not include any non-code explanations. Here is the code:\n{part}'

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
    print(f'Total time taken: {minutes:.0f} minutes and {seconds:.2f} seconds')

    annotated_code += completions.choices[0].text

print(f'Total time taken: {time.time() - start_time:.2f} seconds')


# 将注释后的代码写入带时间戳的文件

output_filename = f'code_out_{int(time.time())}.txt'
with open(output_filename, 'w', encoding='utf-8') as output_file:
    output_file.write(annotated_code)
print(f'file written successfully to {output_filename}')
