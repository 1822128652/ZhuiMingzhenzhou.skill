#!/usr/bin/env python3
"""
获取回忆列表

用法:
    python get_memories.py           # 获取所有回忆
    python get_memories.py --recent  # 获取最近10条
    python get_memories.py --search "电影"  # 搜索回忆
"""

import json
from pathlib import Path
import sys

def get_memories(limit=None, search=None):
    """获取回忆列表"""
    memories_file = Path(__file__).parent.parent / "references" / "memories.json"
    
    with open(memories_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    memories = data["memories"]
    
    # 搜索过滤
    if search:
        memories = [m for m in memories if search in m["content"]]
    
    # 限制数量
    if limit:
        memories = memories[-limit:]
    
    return memories

def print_memories(memories):
    """打印回忆列表"""
    if not memories:
        print("暂无回忆记录")
        return
    
    print(f"\n共有 {len(memories)} 条回忆:\n")
    for m in memories:
        print(f"📅 {m['date']} - {m['content']}")

if __name__ == "__main__":
    limit = None
    search = None
    
    if "--recent" in sys.argv:
        limit = 10
    elif "--search" in sys.argv:
        search_idx = sys.argv.index("--search")
        if search_idx + 1 < len(sys.argv):
            search = sys.argv[search_idx + 1]
    
    memories = get_memories(limit, search)
    print_memories(memories)
