import os
import datetime
import tkinter as tk
from tkinter import messagebox

def save_diary(content):
    now = datetime.datetime.now()
    date_str = now.strftime('%Y-%m-%d')
    time_str = now.strftime('%H:%M:%S')
    filename = fr'your\path\to\{date_str}.md'
    entry = f'{date_str} {time_str}\n{content}\n\n'
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(entry)

def on_ctrl_enter(event=None):
    content = text.get('1.0', tk.END).strip()
    if content:
        save_diary(content)
        text.delete('1.0', tk.END)
        messagebox.showinfo('保存成功', '心情已保存到日记！')
    else:
        messagebox.showwarning('内容为空', '请输入内容后再保存。')

def on_close():
    if messagebox.askokcancel('退出', '确定要退出吗?'):
        root.destroy()

root = tk.Tk()
root.title('心情日记')
root.geometry('500x300')

label = tk.Label(root, text='请输入你的心情（按 Ctrl+Enter 保存）：')
label.pack(pady=5)

text = tk.Text(root, height=12, width=60)
text.pack(padx=10, pady=10)

text.bind('<Control-Return>', on_ctrl_enter)
root.protocol('WM_DELETE_WINDOW', on_close)

root.mainloop()
