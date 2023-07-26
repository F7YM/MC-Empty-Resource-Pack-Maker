import uuid
import os

uuid1 = str(uuid.uuid4())
uuid2 = str(uuid.uuid4())
try:
    os.mkdir("Tutorial_Resource_Pack")
except:
    print("创建Tutorial_Resource_Pack文件夹失败，请检查是否已有重名文件夹")
    exit()

name = input("包名：")
description = input("包描述：")

with open("Tutorial_Resource_Pack/manifest.json","w",encoding="utf-8") as f:
    f.write("")

with open("Tutorial_Resource_Pack/manifest.json","a",encoding="utf-8") as f:
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
    "version": [1, 0, 0],
    "min_engine_version": [1, 13, 0]
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
      "version": [1, 0, 0]
    }
  ]
}''')
os.mkdir("Tutorial_Resource_Pack/textures")
os.mkdir("Tutorial_Resource_Pack/textures/entity")
os.mkdir("Tutorial_Resource_Pack/textures/blocks")
os.mkdir("Tutorial_Resource_Pack/textures/items")
os.mkdir("Tutorial_Resource_Pack/textures/environment")
os.mkdir("Tutorial_Resource_Pack/sounds")
os.mkdir("Tutorial_Resource_Pack/sounds/music")
os.mkdir("Tutorial_Resource_Pack/texts")
os.mkdir("Tutorial_Resource_Pack/animation_controllers")
os.mkdir("Tutorial_Resource_Pack/animations")
os.mkdir("Tutorial_Resource_Pack/animations/models")
os.mkdir("Tutorial_Resource_Pack/attachables")
os.mkdir("Tutorial_Resource_Pack/models")
os.mkdir("Tutorial_Resource_Pack/models/entity")
os.mkdir("Tutorial_Resource_Pack/models/blocks")
os.mkdir("Tutorial_Resource_Pack/render_controllers")
print("Done.")