import json
from pprint import pprint
from PIL import ImageColor
from xml.etree import ElementTree as ET

# 讀取投票結果資料
with open("voting_results.json", "r", encoding="utf-8") as file:
    voting_results = json.load(file)

# 以縣市為迭代，找到「某縣市」的「各政黨」得票數
votes = {}
parties = {'dpp', 'kmt', 'tpp'}
for city in voting_results['district_total']:
    party_vote = {party: voting_results[party][city] for party in parties}
    votes.update({city: party_vote})
# print(votes)

# 「某縣市」的「各政黨」的得票率
percentages = {}
for city, total_vote in voting_results['district_total'].items():
    party_percentages = {
        party: (votes[city][party]/total_vote) * 100 for party in parties}
    percentages[city] = party_percentages

# 找到各縣市獲勝者與得票差距
max_vote_diff = 0
max_vote_diff_city = ''
winner_and_diff = {}
for city in percentages:
    percentages_list = list(percentages[city].items())
    sorted_percentages = sorted(
        percentages_list, key=lambda x: x[1], reverse=True)
    # 進行排序，reverse=True為反向排序，key設定取每個元素的第二個值(得票率)來排序
    winner = sorted_percentages[0][0]
    vote_difference = round(
        sorted_percentages[0][1] - sorted_percentages[1][1], 2)
    winner_and_diff[city] = {'獲勝者': winner, '與第二名的得票差距': vote_difference}
    max_vote_diff = 0
    if vote_difference > max_vote_diff:
        max_vote_diff = vote_difference
        max_vote_diff_city = city
        # print(f"{city}:獲勝者 {winner}, 與第二名的得票差距:{max_vote_diff:2f}%")
# print(max_vote_diff)

# HSL 值 → HEX 色碼
colors = {}
for city, value in winner_and_diff.items():
    # print(city, value)
    ratio = value['與第二名的得票差距']/max_vote_diff
    # print(ratio)
    if value['獲勝者'] == 'tpp':
        H, S, L = 177, 61, int(75 - 40 * ratio)
    elif value['獲勝者'] == 'dpp':
        H, S, L = 130, 60, int(75 - 40 * ratio)
    else:
        H, S, L = 212, 100, int(85 - 40 * ratio)
    # print(f"{city}:HSL:hsl({H},{S}%,{L}%)")
    hsl_value = f"hsl({H},{S}%,{L}%)"
    # print(hsl_value)
    rgb_value = ImageColor.getrgb(hsl_value)
    colors[city] = f"#{rgb_value[0]:02x}{rgb_value[1]:02x}{rgb_value[2]:02x}"
# print(colors)

# 開啟 SVG 檔案
file_path = "Blank_Taiwan_map.svg"  # 上傳的檔案路徑
with open(file_path, "r", encoding="UTF-8") as file:
    svg_content = file.read()

# 解析SVG內容
svg_tree = ET.fromstring(svg_content)
print(svg_tree)

# 尋找所有 <path> 元素，檢查其 <title> 子元素是否匹配指定的縣市名稱
for path in svg_tree.iterfind(".//{http://www.w3.org/2000/svg}path"):
    title = path.find("{http://www.w3.org/2000/svg}title")

    if title is not None:
        target = title.text.strip().split(" ")[0]
        path.set("fill", colors[target])

# 如果成功修改，則保存修改後的SVG內容到一個新檔案
modified_svg_path = "Modified_Taiwan_map.svg"
ET.ElementTree(svg_tree).write(modified_svg_path, encoding="utf-8")

# 顯示成功訊息
print(f"修改成功! SVG 檔已存於 {modified_svg_path}")
