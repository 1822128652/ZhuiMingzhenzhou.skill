#!/usr/bin/env python3
"""
添加回忆到memories.json

用法:
    python add_memory.py "今天我们一起去看了电影"
    python add_memory.py "第一次牵手" --date 2026-04-20
"""

import json
from datetime import datetime
from pathlib import Path
import sys

def add_memory(content, date=None):
    """添加一条回忆"""
    memories_file = Path(__file__).parent.parent / "references" / "memories.json"
    
    # 读取现有数据
    with open(memories_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 创建新回忆
    memory = {
        "id": len(data["memories"]) + 1,
        "content": content,
        "date": date or datetime.now().strftime("%Y-%m-%d"),
        "created_at": datetime.now().isoformat()
    }
    
    # 添加到列表
    data["memories"].append(memory)
    data["last_updated"] = datetime.now().strftime("%Y-%m-%d")
    
    # 保存
    with open(memories_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 已记录回忆: {content}")
    return memory

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python add_memory.py <回忆内容> [--date YYYY-MM-DD]")
        sys.exit(1)
    
    content = sys.argv[1]
    date = None
    
    if "--date" in sys.argv:
        date_idx = sys.argv.index("--date")
        if date_idx + 1 < len(sys.argv):
            date = sys.argv[date_idx + 1]
    
    add_memory(content, date)
