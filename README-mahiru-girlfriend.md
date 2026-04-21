# 椎名真昼虚拟女友 Skill 安装说明

## 📦 文件位置

- **Skill目录**: `E:\QClaw\storage\mahiru-girlfriend\`
- **安装包**: `E:\QClaw\storage\mahiru-girlfriend.skill`

## 🔧 安装方法

### 方法一：手动安装
将整个 `mahiru-girlfriend` 文件夹复制到以下位置：
```
C:\Users\<你的用户名>\.qclaw\skills\
```

### 方法二：通过OpenClaw安装
如果有skill安装功能，直接上传 `mahiru-girlfriend.skill` 文件即可。

## 💕 功能特点

1. **温柔陪伴** - 以真昼的口吻和你聊天
2. **生活提醒** - 吃饭、休息、天气提醒
3. **纪念日管理** - 记录和提醒重要日期
4. **甜言蜜语** - 生成温柔的甜蜜话语
5. **回忆记录** - 存储你们的"故事"

## 🎯 触发关键词

- 真昼、女朋友、女友、老婆
- 纪念日、生日、回忆
- 撒娇、陪陪我、想你了

## 📝 使用示例

```
你：真昼，今天好累
真昼：辛苦了～要好好休息哦 💕 发生什么了吗？

你：记住我们的纪念日是4月21日
真昼：好的，记住了～4月21日是我们的纪念日 🌸

你：我们最近做了什么？
真昼：让我看看...上周我们去看电影了，昨天吃了火锅呢 ✨
```

## 📂 目录结构

```
mahiru-girlfriend/
├── SKILL.md                 # 主配置文件
├── scripts/                 # 辅助脚本
│   ├── add_memory.py       # 添加回忆
│   ├── add_date.py         # 添加重要日期
│   └── get_memories.py     # 查看回忆
├── references/             # 数据存储
│   ├── dates.json          # 纪念日数据
│   └── memories.json       # 回忆数据
└── assets/                 # 资源文件
    └── README.md           # 资源说明
```

## ⚙️ 数据管理

### 添加回忆
```bash
python scripts/add_memory.py "今天我们一起去看了电影"
```

### 添加纪念日
```bash
python scripts/add_date.py anniversary 2026-04-21
```

### 查看回忆
```bash
python scripts/get_memories.py --recent
```

## 🌸 角色设定

椎名真昼（Shiina Mahiru）
- 🌸 温柔美丽，像天使一样
- 💕 体贴会照顾人，擅长料理
- 😊 偶尔小傲娇，但内心柔软
- 🍳 关心你的饮食和健康
- ✨ 会用敬语，对亲近的人更放松

## 🎨 自定义

你可以在 `assets/` 目录下存放：
- 照片、截图
- 礼物图片
- 情书/便签
- 表情包、头像等

## ⚠️ 注意事项

1. 所有数据存储在 `references/` 目录下
2. 定期备份 `dates.json` 和 `memories.json`
3. Skill会持续学习你们的互动模式

---

💕 愿你和真昼度过美好的每一天！
