New_UnifiedPhishingFeatures = {
    # 文本相关特征
    "text_features": {
        # 邮件主题特征
        "subject": {
            "urgency_level": "高/中/低",  # 紧急程度    使用Label 打分映射
            "contains_threatening_language": bool,  # 是否包含威胁性语言
            "contains_seductive_language": bool,  # 是否包含诱惑性语言
            "contains_emergency_action_request": bool,  # 是否要求紧急操作
            "sentiment_score": float,  # 主题情感得分（-1 ~ 1）
            "sentiment_label": str,  # 情感标签（积极/消极/中性）
        },
        # 发件人特征
        "sender": {
            "impersonation_type": str,  # 冒充类型（银行/政府/电商等）
            "email_address_anomalies": str,  # 异常类型（非官方域名/拼写错误等）
            "sender_reputation_score": float,  # 发件人信誉分（0~1）
            "domain_similarity_to_known_brands": float,  # 域名与知名品牌的相似度
        },
        # 正文内容特征
        "content": {
            "word_count": int,  # 总词数
            "url_count": int,  # 包含链接数量
            "spelling_errors": int,  # 拼写错误数量
            "grammar_errors": int,  # 语法错误数量
            "suspicious_keywords": list,  # 敏感关键词列表
            "urgency_words_count": int,  # 紧急词汇数量
            "contains_personal_information_request": bool,  # 是否请求个人信息
            "contains_abnormal_financial_request": bool,  # 是否请求异常金融信息
            "text_complexity": float,  # 文本复杂度评分（0~100）
            "text_similarity_to_legitimate_emails": float,  # 与合法邮件相似度
            "language": str,  # 使用语言（中文/英文/混合等）
            "contains_obfuscated_text": bool,  # 是否存在模糊化文本（如替换字母为符号）
            "requests_otp_or_mfa": bool,  # 是否请求一次性密码或MFA
            "contains_phishing_call_to_action": bool,  # 是否存在钓鱼式引导点击
            "text_sentiment": str,  # 情感分类
            "text_sentiment_score": float,
        }
    },

    # URL情报特征
    "url_intelligence_features": {
        "basic": {
            "domain_length": int,  # 域名长度
            "dot_count": int,  # 点号数量
            "contains_ip_address": bool,  # 是否包含IP地址
            "contains_at_symbol": bool,  # 是否包含@符号
            "contains_hyphen": bool,  # 是否包含连字符
            "path_length": int,  # 路径长度
            "subdomains_count": int,  # 子域名数量
            "tld": str,  # 顶级域
            "query_params_count": int,  # 查询参数个数
            "has_suspicious_query_params": bool,  # 是否存在可疑查询参数
            "suspicious_query_params": list,  # 可疑参数列表
        },
        "reputation_and_risk": {
            "is_blacklisted": bool,  # 是否在黑名单中
            "risk_score": int,  # 风险评分（0~100）
            "redirect_count": int,  # 重定向次数
            "domain_age_days": int,  # 域名注册天数
            "whois_hidden": bool,  # WHOIS是否隐藏
            "domain_similarity_score": float,  # 与合法域名相似度
            "contains_suspicious_keywords": bool,  # 是否包含可疑关键词
            "brand_similarity_score": float,  # 与品牌域名相似度
            "ssl_https": bool,  # 是否使用HTTPS
            "ssl_certificate_status": str,  # SSL证书状态（有效/无效/不存在）
            "ca_trust_score": float,  # CA信任评分（0~100）
            "suspicious_subdomains": list,  # 可疑子域名列表
        }
    },

    # 截图图像特征
    "image_features": {
        "layout": {
            "contains_login_form": bool,  # 是否包含登录表单
            "contains_bank_card_input": bool,  # 是否包含银行卡输入框
            "form_present": bool,  # 是否存在表单
            "login_form_detected": bool,  # 是否检测到登录表单
            "element_complexity": float,  # 页面元素复杂度（0~100）
        },
        "visual_similarity": {
            "logo_similarity_to_known_brands": float,  # 与知名品牌Logo相似度
            "favicon_matches_brand": bool,  # Favicon是否匹配品牌
            "brand_visual_similarity": float,  # 与品牌视觉相似度
            "visual_similarity_score": float,  # 图像整体相似度评分
            "brand_mismatch": bool,  # 视觉与品牌不一致
            "suspicious_ui_layout": bool,  # 是否存在可疑UI布局
        },
        "risk_elements": {
            "suspicious_links": int,  # 可疑链接数量
            "contains_suspicious_popup": bool,  # 是否存在可疑弹窗
            "suspicious_visual_elements": int,  # 可疑视觉元素数量
            "visual_phishing_risk": float,  # 视觉钓鱼风险评分（0~100）
            "image_text_keywords": list,  # 图像中识别出的敏感文本关键词
        }
    },

    # 网站结构与内容特征
    "website_features": {
        "structure": {
            "form_count": int,  # 表单数量
            "external_link_count": int,  # 外部链接数量
            "script_count": int,  # JS脚本数量
            "iframe_count": int,  # iframe数量
            "input_form_count": int,  # 输入表单数量
            "hidden_inputs_count": int,  # 隐藏输入字段数量
            "contains_iframe": bool,  # 是否存在iframe
            "meta_redirect": bool,  # 是否存在Meta重定向
        },
        "content": {
            "title_url_relevance": float,  # 标题与URL相关性评分（0~1）
            "content_similarity_to_legitimate_site": float,  # 与合法网站内容相似度
            "contains_abnormal_redirect": bool,  # 是否存在异常跳转
            "contains_hidden_elements": bool,  # 是否存在隐藏元素
            "privacy_policy_valid": bool,  # 隐私政策是否有效
            "dynamic_script_behavior": str,  # 动态脚本行为描述
        },
        "security": {
            "uses_https": bool,  # 是否使用HTTPS
            "ssl_certificate_status": str,  # SSL证书状态
            "ca_trust_score": float,  # CA信任评分
            "server_location": str,  # 服务器地理位置
            "domain_registration_country": str,  # 注册国家
            "server_country_match_domain": bool,  # 服务器位置是否与域名注册地一致
        }
    }
}