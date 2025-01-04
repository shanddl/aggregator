import yaml
import requests
import os

# 从 Gist URL 下载订阅配置文件
def download_subscription_config(url):
    response = requests.get(url)
    response.raise_for_status()
    return yaml.safe_load(response.text)

# 保存订阅配置文件
def save_subscription_config(config, file_path):
    # 创建目录（如果不存在的话）
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as file:
        yaml.dump(config, file, allow_unicode=True, default_flow_style=False)

# 筛选节点，只保留亚太地区的节点，去除其他节点包括俄罗斯的节点
def filter_nodes(config):
    asia_pacific_countries = [
        "China", "Japan", "South Korea", "Taiwan", "Hong Kong", "Singapore",
        "Malaysia", "Thailand", "Vietnam", "Philippines", "Indonesia", "Australia", "New Zealand"
    ]
    filtered_proxies = [proxy for proxy in config['proxies'] if any(country in proxy['name'] for country in asia_pacific_countries)]
    config['proxies'] = filtered_proxies
    return config

def main():
    gist_url = 'https://gist.githubusercontent.com/shanddl/47ba583ea5b4f5f0e3c5a719d0c01c29/raw/clash.yaml'
    output_file = 'D:/GitHub/aggregator/config/filtered_subscription_config.yaml'

    config = download_subscription_config(gist_url)
    filtered_config = filter_nodes(config)
    save_subscription_config(filtered_config, output_file)

if __name__ == "__main__":
    main()
