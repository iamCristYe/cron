import requests
from datetime import datetime, timedelta

# 日期范围
start_date = datetime(2025, 3, 30)
end_date = datetime(2025, 4, 12)
dates = [
    (start_date + timedelta(days=i)).strftime("%m%d")
    for i in range((end_date - start_date).days + 1)
]

base_url = "https://cdn.hinatazaka46.com/files/14/H46%20NEWS/"

# 文件名模板（无日期）
templates_without_date = [
    "hnt46_14th_asya_FIX_s.jpg",
    "14th_Acmyk.jpg",
    "14th_asya.jpg",
    "14th.jpg",
    "_14th.jpg",
    "_asya_FIX.jpg",
    "_asya.jpg",
    "_Acmyk.jpg",
    "_アー写.jpg",
    "_アー写_FIX.jpg",
    "アー写.jpg",
    "アー写_FIX.jpg",
    "hnt46_アー写.jpg",
    "hnt46_アー写_FIX.jpg",
    "hnt46_asya_FIX.jpg",
    "hnt46_14.jpg",
    "hnt46_14th.jpg",
    "hnt46_14th_main.jpg",
    "hnt46_アー写_14th.jpg",
    "アー写_14th.jpg",
    "HNT_14th.jpg",
]

# 带日期模板
templates_with_date = [
    "_アー写_{date}.jpg",
    "アー写_14th_{date}.jpg",
    "14th_asya_{date}.jpg",
    "14th_Asya_FIX_{date}.jpg",
    "14th_Acmyk_{date}.jpg",
    "14th_{date}.jpg",
    "_14th_{date}.jpg",
    "hnt46_14th_{date}.jpg",
    "hnt46_14th_main_{date}.jpg",
    "{date}_14th_asya.jpg",
    "{date}_14th_main.jpg",
    "hnt46_アー写_14th_{date}.jpg",
    "hnt46_アー写_FIX_{date}.jpg",
    "HNT_14th_{date}.jpg",
]


def check_url(url):
    try:
        response = requests.head(url, timeout=15)
        return response.status_code == 200
    except Exception as e:
        print(f"⚠️ 请求失败: {url} -> {e}")
        return False


print("🔍 [Step 1] 尝试不含日期的文件名...")
for filename in templates_without_date:
    full_url = base_url + filename
    print(f"尝试中: {full_url}")
    if check_url(full_url):
        print(f"\n✅ 找到有效链接: {full_url}")
        exit(0)

print("🔍 [Step 2] 尝试含日期的文件名...")
for date in dates:
    for tpl in templates_with_date:
        filename = tpl.format(date=date)
        full_url = base_url + filename
        print(f"尝试中: {full_url}")
        if check_url(full_url):
            print(f"\n✅ 找到有效链接: {full_url}")
            exit(0)

print("\n🛑 全部尝试完毕，未找到有效链接。")
