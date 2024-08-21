要实现这个任务，你可以按照以下步骤进行操作：

### 1. 安装必要的库

你需要安装一些Python库来处理PDF和API调用。你可以使用以下命令来安装这些库：

```bash
pip install PyPDF2 openai
```

### 2. 创建PDF转文本的脚本

你可以使用`PyPDF2`来将PDF文件转换为文本：

```python
import os
import PyPDF2

def pdf_to_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
    return text
```

### 3. 使用OpenAI API进行问答

首先，你需要有一个OpenAI的API密钥。然后可以使用`openai`库来调用ChatGPT-4 Turbo：

```python
import openai

openai.api_key = 'your_openai_api_key'

def ask_question_with_gpt(text, question):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Text: {text}\n\nQuestion: {question}"}
        ]
    )
    return response['choices'][0]['message']['content']
```

### 4. 批量处理PDF文件

你可以遍历目录中的所有PDF文件，提取文本并询问问题，然后将结果保存为JSON格式：

```python
import json

def process_pdfs_in_folder(folder_path, question):
    results = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            text = pdf_to_text(pdf_path)
            answer = ask_question_with_gpt(text, question)
            results[filename] = answer
    
    with open('results.json', 'w', encoding='utf-8') as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=4)

# 运行处理过程
folder_path = 'test_folder'  # 替换为你的文件夹路径
question = "你的问题"  # 替换为你要问的问题
process_pdfs_in_folder(folder_path, question)
```

### 5. 总结结果到JSON文件

这个脚本将每个PDF文件的结果汇总到一个名为`results.json`的文件中。文件的格式如下：

```json
{
    "file1.pdf": "Answer to the question...",
    "file2.pdf": "Answer to the question...",
    ...
}
```

### 6. 运行脚本

将上述脚本保存为一个Python文件（例如`process_pdfs.py`），并运行它：

```bash
python process_pdfs.py
```

这个脚本将遍历指定文件夹中的所有PDF文件，提取它们的文本，向ChatGPT提问，并将答案保存到JSON文件中。
