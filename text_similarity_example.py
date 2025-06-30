#!/usr/bin/env python3
"""
文本相似度工具使用示例
"""

from tools.text_similarity_util import TextSimilarityUtil


def simple_example():
    """简单使用示例"""
    print("=== 文本相似度工具简单使用示例 ===")
    
    # 创建文本相似度工具（默认支持中文）
    similarity_util = TextSimilarityUtil()
    
    # 示例文本
    text1 = "人工智能技术正在快速发展"
    text2 = "AI技术发展很快"
    
    print(f"文本1: {text1}")
    print(f"文本2: {text2}")
    
    # 1. 计算余弦相似度
    cosine_sim = similarity_util.cosine_similarity(text1, text2)
    print(f"余弦相似度: {cosine_sim:.4f}")
    
    # 2. 计算Jaccard相似度
    jaccard_sim = similarity_util.jaccard_similarity(text1, text2)
    print(f"Jaccard相似度: {jaccard_sim:.4f}")
    
    # 3. 计算综合相似度（包含所有方法）
    comprehensive_result = similarity_util.comprehensive_similarity(text1, text2)
    print("综合相似度结果:")
    for method, score in comprehensive_result.items():
        print(f"  {method}: {score:.4f}")
    
    # 4. 判断是否相似
    is_similar = similarity_util.is_similar(text1, text2, threshold=0.7)
    print(f"是否相似 (阈值0.7): {is_similar}")


def english_example():
    """英文文本示例"""
    print("\n=== 英文文本相似度示例 ===")
    
    # 创建英文文本相似度工具
    similarity_util = TextSimilarityUtil(language='english')
    
    text1 = "Machine learning is a subset of artificial intelligence"
    text2 = "ML is part of AI"
    
    print(f"Text1: {text1}")
    print(f"Text2: {text2}")
    
    # 计算综合相似度
    result = similarity_util.comprehensive_similarity(text1, text2)
    print("Similarity results:")
    for method, score in result.items():
        print(f"  {method}: {score:.4f}")


def find_similar_example():
    """查找最相似文本示例"""
    print("\n=== 查找最相似文本示例 ===")
    
    similarity_util = TextSimilarityUtil()
    
    target = "Python编程语言"
    candidates = [
        "Python是一种编程语言",
        "Java编程",
        "Python语言学习",
        "JavaScript开发"
    ]
    
    print(f"目标文本: {target}")
    print("候选文本:")
    for i, text in enumerate(candidates, 1):
        print(f"  {i}. {text}")
    
    # 找到最相似的文本
    best_index, similarity = similarity_util.find_most_similar(target, candidates)
    
    print(f"\n最相似的文本: {candidates[best_index]}")
    print(f"相似度: {similarity:.4f}")


if __name__ == "__main__":
    simple_example()
    english_example()
    find_similar_example() 