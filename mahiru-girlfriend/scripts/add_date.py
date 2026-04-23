#!/usr/bin/env python3
"""
添加重要日期到dates.json

用法:
    python add_date.py anniversary 2026-04-21
    python add_date.py birthday --type yours 2026-01-01
    python add_date.py important "第一次约会" 2026-04-15
"""

import json
from datetime import datetime
from pathlib import Path
import sys

def add_date(date_type, value, name=None, description=None):
    """添加重要日期"""
    dates_file = Path(__file__).parent.parent / "references" / "dates.json"
    
    # 读取现有数据
    with open(dates_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 根据类型添加
    if date_type == "anniversary":
        data["anniversary"] = value
        print(f"✅ 已设置纪念日: {value}")
    elif date_type == "birthday":
        # 需要指定 --type yours 或 mine
        if "--type" in sys.argv:
            type_idx = sys.argv.index("--type")
            if type_idx + 1 < len(sys.argv):
                whose = sys.argv[type_idx + 1]
                if whose == "yours":
                    data["your_birthday"] = value
                    print(f"✅ 已设置你的生日: {value}")
                elif whose == "mine":
                    data["my_birthday"] = value
                    print(f"✅ 已设置我的生日: {value}")
    elif date_type == "important":
        important_date = {
            "name": name or "未命名",
            "date": value,
            "description": description or ""
        }
        data["important_dates"].append(important_date)
        print(f"✅ 已添加重要日期: {name} - {value}")
    
    data["last_updated"] = datetime.now().strftime("%Y-%m-%d")
    
    # 保存
    with open(dates_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("用法:")
        print("  python add_date.py anniversary 2026-04-21")
        print("  python add_date.py birthday --type yours 2026-01-01")
        print("  python add_date.py important \"第一次约会\" 2026-04-15")
        sys.exit(1)
    
    date_type = sys.argv[1]
    
    if date_type == "important":
        if len(sys.argv) >= 4:
            name = sys.argv[2]
            value = sys.argv[3]
            add_date(date_type, value, name)
        else:
            print("需要提供日期名称和日期")
            sys.exit(1)
    else:
        value = sys.argv[2]
        add_date(date_type, value)
