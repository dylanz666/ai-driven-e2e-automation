"""
文本相似度计算工具类
提供多种文本相似度计算方法，包括余弦相似度、编辑距离、Jaccard相似度等
"""

import re
import math
from typing import List, Dict, Tuple, Union, Optional
from collections import Counter
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import jieba
import numpy as np


class TextSimilarityUtil:
    """文本相似度计算工具类"""
    
    def __init__(self, language: str = 'chinese'):
        """
        初始化文本相似度工具
        
        Args:
            language: 语言类型，支持 'chinese' 和 'english'
        """
        self.language = language
        self._vectorizer = None
    
    def preprocess_text(self, text: str) -> str:
        """
        预处理文本
        
        Args:
            text: 原始文本
            
        Returns:
            预处理后的文本
        """
        if not text:
            return ""
        
        # 转换为小写
        text = text.lower()
        
        # 移除特殊字符，保留中文、英文、数字和空格
        if self.language == 'chinese':
            # 保留中文、英文、数字和空格
            text = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9\s]', '', text)
        else:
            # 只保留英文、数字和空格
            text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        
        # 移除多余空格
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    def tokenize_text(self, text: str) -> List[str]:
        """
        分词处理
        
        Args:
            text: 文本
            
        Returns:
            分词结果列表
        """
        if not text:
            return []
        
        if self.language == 'chinese':
            # 使用jieba进行中文分词
            return [word for word in jieba.cut(text) if word.strip()]
        else:
            # 英文按空格分词
            return text.split()
    
    def cosine_similarity(self, text1: str, text2: str) -> float:
        """
        计算余弦相似度
        
        Args:
            text1: 第一段文本
            text2: 第二段文本
            
        Returns:
            相似度值 (0-1之间，1表示完全相同)
        """
        if not text1 or not text2:
            return 0.0
        
        # 预处理文本
        processed_text1 = self.preprocess_text(text1)
        processed_text2 = self.preprocess_text(text2)
        
        if not processed_text1 or not processed_text2:
            return 0.0
        
        # 使用TF-IDF向量化
        vectorizer = TfidfVectorizer(
            tokenizer=self.tokenize_text,
            stop_words=None,
            lowercase=False
        )
        
        try:
            tfidf_matrix = vectorizer.fit_transform([processed_text1, processed_text2])
            similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
            return float(similarity)
        except Exception:
            return 0.0
    
    def jaccard_similarity(self, text1: str, text2: str) -> float:
        """
        计算Jaccard相似度
        
        Args:
            text1: 第一段文本
            text2: 第二段文本
            
        Returns:
            相似度值 (0-1之间，1表示完全相同)
        """
        if not text1 or not text2:
            return 0.0
        
        # 预处理和分词
        tokens1 = set(self.tokenize_text(self.preprocess_text(text1)))
        tokens2 = set(self.tokenize_text(self.preprocess_text(text2)))
        
        if not tokens1 and not tokens2:
            return 1.0  # 两个空文本视为相同
        
        if not tokens1 or not tokens2:
            return 0.0
        
        # 计算交集和并集
        intersection = len(tokens1.intersection(tokens2))
        union = len(tokens1.union(tokens2))
        
        return intersection / union if union > 0 else 0.0
    
    def edit_distance_similarity(self, text1: str, text2: str) -> float:
        """
        基于编辑距离的相似度计算
        
        Args:
            text1: 第一段文本
            text2: 第二段文本
            
        Returns:
            相似度值 (0-1之间，1表示完全相同)
        """
        if not text1 and not text2:
            return 1.0
        
        if not text1 or not text2:
            return 0.0
        
        # 预处理文本
        processed_text1 = self.preprocess_text(text1)
        processed_text2 = self.preprocess_text(text2)
        
        # 计算编辑距离
        distance = self._levenshtein_distance(processed_text1, processed_text2)
        max_length = max(len(processed_text1), len(processed_text2))
        
        # 转换为相似度
        return 1 - (distance / max_length) if max_length > 0 else 1.0
    
    def _levenshtein_distance(self, str1: str, str2: str) -> int:
        """
        计算Levenshtein编辑距离
        
        Args:
            str1: 字符串1
            str2: 字符串2
            
        Returns:
            编辑距离
        """
        if len(str1) < len(str2):
            return self._levenshtein_distance(str2, str1)
        
        if len(str2) == 0:
            return len(str1)
        
        previous_row = list(range(len(str2) + 1))
        for i, c1 in enumerate(str1):
            current_row = [i + 1]
            for j, c2 in enumerate(str2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        
        return previous_row[-1]
    
    def sequence_matcher_similarity(self, text1: str, text2: str) -> float:
        """
        使用difflib.SequenceMatcher计算相似度
        
        Args:
            text1: 第一段文本
            text2: 第二段文本
            
        Returns:
            相似度值 (0-1之间，1表示完全相同)
        """
        if not text1 and not text2:
            return 1.0
        
        if not text1 or not text2:
            return 0.0
        
        # 预处理文本
        processed_text1 = self.preprocess_text(text1)
        processed_text2 = self.preprocess_text(text2)
        
        return difflib.SequenceMatcher(None, processed_text1, processed_text2).ratio()
    
    def word_overlap_similarity(self, text1: str, text2: str) -> float:
        """
        计算词汇重叠相似度
        
        Args:
            text1: 第一段文本
            text2: 第二段文本
            
        Returns:
            相似度值 (0-1之间，1表示完全相同)
        """
        if not text1 or not text2:
            return 0.0
        
        # 预处理和分词
        tokens1 = self.tokenize_text(self.preprocess_text(text1))
        tokens2 = self.tokenize_text(self.preprocess_text(text2))
        
        if not tokens1 and not tokens2:
            return 1.0
        
        if not tokens1 or not tokens2:
            return 0.0
        
        # 计算重叠词汇
        counter1 = Counter(tokens1)
        counter2 = Counter(tokens2)
        
        # 计算重叠部分
        overlap = sum((counter1 & counter2).values())
        total = sum(counter1.values()) + sum(counter2.values())
        
        return (2 * overlap) / total if total > 0 else 0.0
    
    def comprehensive_similarity(self, text1: str, text2: str, 
                               weights: Optional[Dict[str, float]] = None) -> Dict[str, float]:
        """
        综合相似度计算，返回多种方法的相似度结果
        
        Args:
            text1: 第一段文本
            text2: 第二段文本
            weights: 各方法的权重，默认均等权重
            
        Returns:
            包含各种相似度方法的字典
        """
        if weights is None:
            weights = {
                'cosine': 0.3,
                'jaccard': 0.2,
                'edit_distance': 0.2,
                'sequence_matcher': 0.2,
                'word_overlap': 0.1
            }
        
        results = {
            'cosine': self.cosine_similarity(text1, text2),
            'jaccard': self.jaccard_similarity(text1, text2),
            'edit_distance': self.edit_distance_similarity(text1, text2),
            'sequence_matcher': self.sequence_matcher_similarity(text1, text2),
            'word_overlap': self.word_overlap_similarity(text1, text2)
        }
        
        # 计算加权平均
        weighted_sum = sum(results[method] * weights[method] for method in results)
        results['weighted_average'] = weighted_sum
        
        return results
    
    def is_similar(self, text1: str, text2: str, threshold: float = 0.8, 
                   method: str = 'weighted_average') -> bool:
        """
        判断两段文本是否相似
        
        Args:
            text1: 第一段文本
            text2: 第二段文本
            threshold: 相似度阈值
            method: 使用的相似度方法
            
        Returns:
            是否相似
        """
        if method == 'weighted_average':
            similarity_result = self.comprehensive_similarity(text1, text2)
            return similarity_result['weighted_average'] >= threshold
        elif method == 'cosine':
            return self.cosine_similarity(text1, text2) >= threshold
        elif method == 'jaccard':
            return self.jaccard_similarity(text1, text2) >= threshold
        elif method == 'edit_distance':
            return self.edit_distance_similarity(text1, text2) >= threshold
        elif method == 'sequence_matcher':
            return self.sequence_matcher_similarity(text1, text2) >= threshold
        elif method == 'word_overlap':
            return self.word_overlap_similarity(text1, text2) >= threshold
        else:
            raise ValueError(f"Unsupported method: {method}")
    
    def find_most_similar(self, target_text: str, candidate_texts: List[str], 
                         method: str = 'weighted_average') -> Tuple[int, float]:
        """
        在候选文本列表中找到与目标文本最相似的文本
        
        Args:
            target_text: 目标文本
            candidate_texts: 候选文本列表
            method: 使用的相似度方法
            
        Returns:
            (最相似文本的索引, 相似度值)
        """
        if not candidate_texts:
            return -1, 0.0
        
        max_similarity = 0.0
        best_index = -1
        
        for i, candidate in enumerate(candidate_texts):
            if method == 'weighted_average':
                similarity = self.comprehensive_similarity(target_text, candidate)['weighted_average']
            elif method == 'cosine':
                similarity = self.cosine_similarity(target_text, candidate)
            elif method == 'jaccard':
                similarity = self.jaccard_similarity(target_text, candidate)
            elif method == 'edit_distance':
                similarity = self.edit_distance_similarity(target_text, candidate)
            elif method == 'sequence_matcher':
                similarity = self.sequence_matcher_similarity(target_text, candidate)
            elif method == 'word_overlap':
                similarity = self.word_overlap_similarity(target_text, candidate)
            else:
                raise ValueError(f"Unsupported method: {method}")
            
            if similarity > max_similarity:
                max_similarity = similarity
                best_index = i
        
        return best_index, max_similarity 