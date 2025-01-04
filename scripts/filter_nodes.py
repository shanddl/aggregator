import json

# 假设你有一个函数来加载订阅配置
def load_subscription_config(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# 假设你有一个函数来保存订阅配置
def save_subscription_config(config, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(config, file, ensure_ascii=False, indent=4)

# 筛选节点，只保留亚太地区的节点，去除其他节点包括俄罗斯的节点
def filter_nodes(config):
    asia_pacific_countries = [
        "China", "Japan", "South Korea", "Taiwan", "Hong Kong", "Singapore",
        "Malaysia", "Thailand", "Vietnam", "Philippines", "Indonesia", "Australia", "New Zealand"
    ]
    filtered_nodes = [node for node in config['proxies'] if any(country in node['name'] for country in asia_pacific_countries)]
    config['proxies'] = filtered_nodes
    return config

def main():
    input_file = 'path/to/your/subscription_config.json'
    output_file = 'path/to/your/filtered_subscription_config.json'

    config = load_subscription_config(input_file)
    filtered_config = filter_nodes(config)
    save_subscription_config(filtered_config, output_file)

if __name__ == "__main__":
    main()