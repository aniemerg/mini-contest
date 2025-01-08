# Deep Funding Mini-Contest Submission

This repository contains my submission for the Deep Funding Mini-Contest, currently ranking third on the leaderboard. The approach uses Large Language Models (LLMs) to analyze project documentation and predict relative funding allocations between open source projects.

## Overview

The Deep Funding Mini-Contest aims to create a distilled human judgment mechanism for predicting funding allocations among open source projects. This submission demonstrates an approach that leverages GPT-4 for feature extraction from project documentation, combined with XGBoost for modeling funding preferences.

## Setup Requirements

1. **OpenAI API Key**: Required for the GPT-4 analysis of project documentation
2. **GitHub API Token**: Needed to fetch project README files and documentation
3. **Python Dependencies**: Required packages are listed in the notebook. Key libraries include:
   - XGBoost
   - Pandas
   - NumPy
   - Requests
   - GitPython
   - OpenAI

## Strategy Overview

The approach consists of several key steps:

1. **Documentation Collection**:
   - Fetch README files and documentation from GitHub repositories
   - Use multiple fallback methods (API, cloning) to ensure maximum coverage
   - Cache results to avoid API rate limits and repeated processing

2. **Feature Extraction using LLMs**:
   - Analyze project documentation using GPT-4
   - Extract structured ratings across 40+ dimensions including:
     - Technical complexity
     - Documentation quality
     - Community engagement
     - Enterprise readiness
     - Project maturity
     - Innovation level
   - Generate consistent, numerical ratings (1-5 scale) for each dimension

3. **Model Training**:
   - Create feature vectors from differences between paired projects
   - Apply logit transformation to handle bounded [0,1] target range
   - Train XGBoost model with carefully tuned parameters
   - Use cross-validation to prevent overfitting

4. **Prediction Generation**:
   - Transform predictions back to [0,1] range
   - Ensure predictions sum to 1 for each pair
   - Handle missing data gracefully with default 0.5 weights

## Key Insights

1. **Documentation Signals**: High-quality documentation often correlates with higher funding allocations, particularly when it demonstrates enterprise readiness and community engagement.

2. **Feature Importance**: The most influential features in predicting funding allocation were:
   - Enterprise readiness
   - Project maturity
   - Technical complexity
   - Documentation quality
   - Community size

3. **Transformation Benefits**: Using logit transformation for the target variable significantly improved model performance, particularly for extreme preferences.

## Running the Code

1. Set up environment variables:
   ```bash
   export OPENAI_API_KEY='your-key-here'
   export GITHUB_TOKEN='your-token-here'
   ```

2. Run the notebook cells in order. The process is designed to cache intermediate results, so you can safely interrupt and resume.

3. Key checkpoints are saved after:
   - Documentation collection
   - LLM analysis
   - Model training
   - Prediction generation


## Acknowledgments

Thanks to the Deep Funding teams for organizing this contest and providing the opportunity to contribute to improving public goods funding in the Ethereum ecosystem.

## Contact

For questions or feedback about this submission, please open an issue in this repository.
