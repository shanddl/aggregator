import requests
import json
import base64
import os

# 定义亚太地区国家代码列表
ASIA_PACIFIC_COUNTRIES = [
    'CN', 'JP', 'KR', 'SG', 'HK', 'TW', 'AU', 'NZ', 'IN', 'ID', 'MY', 'TH', 'PH', 'VN'
]

# Gist 配置
GIST_ID = '47ba583ea5b4f5f0e3c5a719d0c01c29'
GIST_FILENAME = 'clash.yaml'
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

def fetch_nodes():
    # 拉取节点的逻辑，根据您的需求实现
    # 例如，从订阅链接获取 base64 编码的节点列表
    response = requests.get('您的订阅链接')
    if response.status_code == 200:
        return base64.b64decode(response.text).decode('utf-8')
    else:
        raise Exception('Failed to fetch nodes')

def filter_nodes(nodes):
    # 筛选仅保留亚太地区的节点
    filtered_nodes = []
    for node in nodes:
        # 假设节点信息包含国家代码，您需要根据实际情况解析节点信息
        country_code = node.get('country_code')
        if country_code in ASIA_PACIFIC_COUNTRIES:
            filtered_nodes.append(node)
    return filtered_nodes

def update_gist(content):
    # 更新指定的 Gist
    url = f'https://api.github.com/gists/{GIST_ID}'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        'files': {
            GIST_FILENAME: {
                'content': content
            }
        }
    }
    response = requests.patch(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print('Gist updated successfully')
    else:
        raise Exception('Failed to update Gist')

def main():
    nodes = fetch_nodes()
    filtered_nodes = filter_nodes(nodes)
    # 将筛选后的节点转换为 Clash 配置格式
    clash_config = {
        'proxies': filtered_nodes,
        # 其他必要的配置
    }
    config_content = json.dumps(clash_config, indent=2)
    update_gist(config_content)

if __name__ == '__main__':
    main()
