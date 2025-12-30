# PhishMMF数据集说明
我们的原始数据集使用了钓鱼数据集和非钓鱼各6000条，其中钓鱼邮件来自datacon2023和PhishPot，各3000条；正常邮件来自CEAS_08和SpamAssasin数据集中的正常邮件各3000条，每条数据以经过我们预处理的json格式存放致jsonl文件中。其中，所上传的文件中CEAS_08_0.zip和SpamAssasin_0.zip是非钓鱼邮件的原始数据集，phishing_pot.zip 、datacon2023_1.zip 、datacon2023_2.zip 是原始钓鱼邮件数据集。
1、该项目包含的内容是钓鱼邮件相关的多模态特征数据集，共涉及到了四个模态数据，分别是邮件文本，邮件中关键URL相关的OSINT、网站截图和网站html\javascript代码；
2、json_schema.py文件中是我们设计的结构化多模态特征提取模板，all.zip中文件的内容就是我们使用LLM所提取到的钓鱼邮件多模态特征数据集phishMMF；
3、all.csv是对phishMMF数据集中特征的提取情况和取值范围的统计；
4、email_phishing_feature_228d.npy是all.zip中文件向量化后生成的数据，共232维，其中前228位对应特征数据，后4位是各模态特征掩码，可直接供机器学习模型训练识别钓鱼邮件使用；
5、email_phishing_labels.npy是email_phishing_feature_228d.npy数据对应的标签，钓鱼为1，正常为0；
6、该多模态特征数据集共包含11672条数据，其中钓鱼和正常邮件数据各5836条。

# PhishMMF Dataset Description
Our raw dataset consists of 6,000 phishing emails and 6,000 benign emails respectively. Specifically, the phishing emails are sourced from two datasets (3,000 from Datacon2023 and 3,000 from PhishPot), while the benign emails are obtained from the legitimate subsets of CEAS_08 and SpamAssassin (3,000 each). Note that CEAS_08_0.zip and SpamAssassin_0.zip are the raw datasets of benign emails, and phishing_pot.zip, datacon2023_1.zip, and datacon2023_2.zip are the raw datasets of phishing emails. All samples are preprocessed and stored in JSON format within a jsonl file.
1. This project contains a multimodal feature dataset related to phishing emails, involving four types of modal data: email text, OSINT (Open-Source Intelligence) related to key URLs in emails, website screenshots, and website HTML/JavaScript code.
2. The file json_schema.py contains the structured multimodal feature extraction template designed by us. The content in the file all.zip is PhishMMF, the multimodal feature dataset of phishing emails extracted by us using LLMs (Large Language Models).
3. all.csv provides statistics on the extraction status and value ranges of features in the PhishMMF dataset.
4. email_phishing_feature_228d.npy is the vectorized data generated from the files in all.zip, with a total of 232 dimensions. Among them, the first 228 dimensions correspond to feature data, and the last 4 dimensions are feature masks for each modality. This file can be directly used for training machine learning models to identify phishing emails.
5. email_phishing_labels.npy contains the labels corresponding to the data in email_phishing_feature_228d.npy, where 1 represents phishing emails and 0 represents benign emails.
6. The multimodal feature dataset includes a total of 11,672 pieces of data, with 5,836 phishing emails and 5,836 benign emails respectively.
Preprocessing includes noise removal, duplicate elimination, and structured feature alignment, ensuring each JSON entry contains consistent fields for downstream tasks.<br/><br/>Each line in the jsonl file corresponds to one email sample, with complete metadata and raw content retained.
