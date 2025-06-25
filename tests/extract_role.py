
# tests/test_extract_role.py
# extract_role.py

import re
import pandas as pd

def extract_role(title):
    if pd.isnull(title):
        return None

    title = title.strip().lower()

    patterns = patterns = {
        'Clinical Data Analyst': r'clinical.*data.*analyst',
        'Digital Data Analyst': r'(digital|content).*data.*analyst',
        'Cyber Security Analyst': r'(cyber\s*security|security).*analyst',
        'Financial Analyst': r'financial.*analyst',
        'Fraud Analyst': r'fraud.*analyst',
        'Risk Analyst': r'risk.*analyst',
        'Operations Research Analyst': r'research.*analyst',
        'Procurement Analyst': r'procurement.*analyst',
        'Product Analyst': r'product.*analyst',
        'Supply Chain Analyst': r'supply\s*chain.*analyst',
        'Transportation Analyst': r'transportation.*analyst',
        'Human Resources Analyst': r'(human\s*resources|hr|workforce).*analyst',
        'Healthcare Analyst': r'(healthcare|health).*analyst',
        'Marketing Analyst': r'marketing.*analyst',
        'Business Analyst': r'business.*analyst',
        'Operations Data Analyst': r'operations.*analyst',
        'Data Governance Analyst': r'data\s*governance.*analyst',
        'Data Governance Analyst':r'(steward|stewardship).*analyst',
        'Data Scientist': r'data\s*scientist',
        'Data Engineer': r'data\s*engineer',
        'Data Analyst': r'data.*analyst',
        'Actuarial Analyst': r'actuarial.*analyst',
        'Environmental Analyst': r'environmental.*analyst'
        
    }

    for role, pattern in patterns.items():
        if re.search(pattern, title):
            return role

    return title  
