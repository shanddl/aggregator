import json

def filter_nodes(nodes, exclude_countries=None, exclude_protocols=None):
    if exclude_countries is None:
        exclude_countries = []
    if exclude_protocols is None:
        exclude_protocols = []

    filtered_nodes = []
    for node in nodes:
        country = node.get('country', '').lower()
        protocol = node.get('protocol', '').lower()
        if country not in exclude_countries and protocol not in exclude_protocols:
            filtered_nodes.append(node)
    
    return filtered_nodes

def main():
    # 从文件中读取节点数据
    with open('nodes.json', 'r') as file:
        nodes = json.load(file)

    # 过滤条件
    exclude_countries = ['russia']
    exclude_protocols = ['http']

    # 过滤节点
    filtered_nodes = filter_nodes(nodes, exclude_countries, exclude_protocols)

    # 将过滤后的节点数据保存回文件
    with open('filtered_nodes.json', 'w') as file:
        json.dump(filtered_nodes, file, indent=4)

    print("过滤完成，结果保存在 filtered_nodes.json 文件中")

if __name__ == "__main__":
    main()
