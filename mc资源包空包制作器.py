try:
    import uuid
    import os
    import zipfile
except:
    print("请检查您是否有uuid/os/zipfile库")
    exit()

def zipdir(path, zipname, compression=zipfile.ZIP_DEFLATED):
    with zipfile.ZipFile(zipname, mode='w', compression=compression) as ziph:
        for root, dirs, files in os.walk(path):
            for file in files:
                relative_path = os.path.relpath(os.path.join(root, file), path)
                ziph.write(os.path.join(root, file), arcname=relative_path)
            for dir in dirs:
                relative_path = os.path.relpath(os.path.join(root, dir), path)
                ziph.write(os.path.join(root, dir), arcname=relative_path)

uuid1 = str(uuid.uuid4())
uuid2 = str(uuid.uuid4())

try:
    os.mkdir('Tutorial_Resource_Pack')
except:
    print('创建Tutorial_Resource_Pack文件夹失败，请检查是否已有重名文件夹')
    exit()

name = input('包名：')
description = input('包描述：')
easytocreate = input('[非正式包可不设置]是否设置包版本号(y/n)：')

if easytocreate == 'y':
    version1 = input('[必填整数数字,不可为空]大版本号(格式为 大.中.小 版本号，如1.0.0)：')
    version2 = input('[必填整数数字,不可为空]中版本号(格式为 大.中.小 版本号，如1.0.0)：')
    version3 = input('[必填整数数字,不可为空]小版本号(格式为 大.中.小 版本号，如1.0.0)：')
else:
    version1 = '0'
    version2 = '0'
    version3 = '0'

with open('Tutorial_Resource_Pack/manifest.json','w',encoding='utf-8') as f:
    f.write('')

with open('Tutorial_Resource_Pack/manifest.json','a',encoding='utf-8') as f:
    f.write('''{
  "format_version": 2,
  "header": {
    "description": "''')
    f.write(description)
    f.write('''",
    "name": "''')
    f.write(name)
    f.write('''",
    "uuid": "''')
    f.write(uuid1)
    f.write('''",
    "version": [''')
    f.write(version1)
    f.write(', ')
    f.write(version2)
    f.write(', ')
    f.write(version3)
    f.write('''],
    ''')
    f.write('''"min_engine_version": [1, 13, 0]
  },
  "modules": [
    {
      "description": "''')
    f.write(description)
    f.write('''",
      "type": "resources",
      "uuid": "''')
    f.write(uuid2)
    f.write('''",
      "version": [''')
    f.write(version1)
    f.write(''', ''')
    f.write(version2)
    f.write(''', ''')
    f.write(version3)
    f.write(''']''')
    f.write('''}
  ]
}''')
os.mkdir('Tutorial_Resource_Pack/textures')
os.mkdir('Tutorial_Resource_Pack/textures/entity')
os.mkdir('Tutorial_Resource_Pack/textures/blocks')
os.mkdir('Tutorial_Resource_Pack/textures/items')
os.mkdir('Tutorial_Resource_Pack/textures/environment')
os.mkdir('Tutorial_Resource_Pack/sounds')
os.mkdir('Tutorial_Resource_Pack/sounds/music')
os.mkdir('Tutorial_Resource_Pack/texts')
os.mkdir('Tutorial_Resource_Pack/animation_controllers')
os.mkdir('Tutorial_Resource_Pack/animations')
os.mkdir('Tutorial_Resource_Pack/animations/models')
os.mkdir('Tutorial_Resource_Pack/attachables')
os.mkdir('Tutorial_Resource_Pack/models')
os.mkdir('Tutorial_Resource_Pack/models/entity')
os.mkdir('Tutorial_Resource_Pack/models/blocks')
os.mkdir('Tutorial_Resource_Pack/render_controllers')
pack = input('是否直接打包为.mcpack格式(y/n)：')
if pack == 'y':
    zipdir('Tutorial_Resource_Pack','Tutorial_Resource_Pack.mcpack')
print("None.")