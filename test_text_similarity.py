#!/usr/bin/env python3
"""
文本相似度工具测试和演示
"""

from tools.text_similarity_util import TextSimilarityUtil


def test_chinese_text_similarity():
    """测试中文文本相似度"""
    print("=== 中文文本相似度测试 ===")
    
    # 创建中文文本相似度工具
    similarity_util = TextSimilarityUtil(language='chinese')
    
    # 测试用例
    test_cases = [
        {
            "text1": "人工智能是计算机科学的一个分支",
            "text2": "AI是计算机科学的一个分支",
            "description": "相似的中文文本"
        },
        {
            "text1": "今天天气很好，阳光明媚",
            "text2": "今天天气不错，阳光灿烂",
            "description": "表达相同意思的不同表达"
        },
        {
            "text1": "Python是一种编程语言",
            "text2": "Java是另一种编程语言",
            "description": "部分相似的内容"
        },
        {
            "text1": "完全不同的内容",
            "text2": "这是另一个完全不同的内容",
            "description": "不相似的内容"
        }
    ]
    
    for i, case in enumerate(test_cases, 1):
        print(f"\n测试用例 {i}: {case['description']}")
        print(f"文本1: {case['text1']}")
        print(f"文本2: {case['text2']}")
        
        # 计算各种相似度
        results = similarity_util.comprehensive_similarity(case['text1'], case['text2'])
        
        print("相似度结果:")
        for method, score in results.items():
            print(f"  {method}: {score:.4f}")
        
        # 判断是否相似
        is_similar = similarity_util.is_similar(case['text1'], case['text2'], threshold=0.6)
        print(f"  是否相似 (阈值0.6): {is_similar}")


def test_english_text_similarity():
    """测试英文文本相似度"""
    print("\n=== 英文文本相似度测试 ===")
    
    # 创建英文文本相似度工具
    similarity_util = TextSimilarityUtil(language='english')
    
    # 测试用例
    test_cases = [
        {
            "text1": "Artificial Intelligence is a branch of computer science",
            "text2": "AI is a branch of computer science",
            "description": "Similar English texts"
        },
        {
            "text1": "The weather is nice today",
            "text2": "It's a beautiful day today",
            "description": "Same meaning, different expression"
        },
        {
            "text1": "Python is a programming language",
            "text2": "Java is another programming language",
            "description": "Partially similar content"
        },
        {
            "text1": "Completely different content",
            "text2": "This is another completely different content",
            "description": "Dissimilar content"
        }
    ]
    
    for i, case in enumerate(test_cases, 1):
        print(f"\n测试用例 {i}: {case['description']}")
        print(f"Text1: {case['text1']}")
        print(f"Text2: {case['text2']}")
        
        # 计算各种相似度
        results = similarity_util.comprehensive_similarity(case['text1'], case['text2'])
        
        print("Similarity results:")
        for method, score in results.items():
            print(f"  {method}: {score:.4f}")
        
        # 判断是否相似
        is_similar = similarity_util.is_similar(case['text1'], case['text2'], threshold=0.6)
        print(f"  Is similar (threshold 0.6): {is_similar}")


def test_find_most_similar():
    """测试查找最相似文本"""
    print("\n=== 查找最相似文本测试 ===")
    
    similarity_util = TextSimilarityUtil(language='chinese')
    
    target_text = "人工智能技术发展迅速"
    candidate_texts = [
        "AI技术发展很快",
        "机器学习是人工智能的一个分支",
        "今天天气很好",
        "人工智能技术正在快速发展",
        "计算机科学很重要"
    ]
    
    print(f"目标文本: {target_text}")
    print("候选文本:")
    for i, text in enumerate(candidate_texts):
        print(f"  {i+1}. {text}")
    
    # 使用不同方法查找最相似的文本
    methods = ['cosine', 'jaccard', 'weighted_average']
    
    for method in methods:
        best_index, similarity = similarity_util.find_most_similar(
            target_text, candidate_texts, method=method
        )
        print(f"\n{method}方法:")
        print(f"  最相似文本索引: {best_index + 1}")
        print(f"  最相似文本: {candidate_texts[best_index]}")
        print(f"  相似度: {similarity:.4f}")


def test_individual_methods():
    """测试各种相似度计算方法"""
    print("\n=== 各种相似度计算方法测试 ===")
    
    similarity_util = TextSimilarityUtil(language='chinese')
    
    text1 = "人工智能和机器学习技术"
    text2 = "AI和ML技术"
    
    print(f"文本1: {text1}")
    print(f"文本2: {text2}")
    
    methods = [
        ('cosine', similarity_util.cosine_similarity),
        ('jaccard', similarity_util.jaccard_similarity),
        ('edit_distance', similarity_util.edit_distance_similarity),
        ('sequence_matcher', similarity_util.sequence_matcher_similarity),
        ('word_overlap', similarity_util.word_overlap_similarity)
    ]
    
    for method_name, method_func in methods:
        similarity = method_func(text1, text2)
        print(f"{method_name}: {similarity:.4f}")


if __name__ == "__main__":
    # 运行所有测试
    test_chinese_text_similarity()
    test_english_text_similarity()
    test_find_most_similar()
    test_individual_methods()
    
    print("\n=== 测试完成 ===") 