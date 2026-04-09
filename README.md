# KIND-LM Style Experiment Design: Clean & Efficient Language Learning
This project outlines a cognitively inspired, sample-efficient language modeling experiment aligned with the KIND-LM project.

## Corpus
This project uses a subset of the CHILDES Demetras Corpus, which contains natural spontaneous interactions between a parent and a 2-year-old child named Trevor. The corpus consists of real-life recorded conversations, making it highly suitable for modeling early child language acquisition.
Raw utterances were cleaned in two processing steps:

1. Only utterances produced by the child (marked as *CHI:) were extracted.

2. Annotation symbols, timestamps, fillers, and irrelevant markers were removed to retain clean, natural child speech for model training.

All utterances are short, repetitive, semantically simple, and structurally aligned with real parental input to young children. This design supports modeling implicit learning, recasting, and gradual, natural language acquisition patterns.

## Core Idea
- Clean, well-formed child-directed linguistic input
- Implicit naturalistic feedback (recasting & expansion)
- Small, sustainable model architectures
- Evaluation focused on robustness and interpretability

## Experiment Design
1. Corpus Construction: Small, curated, grammatically consistent text
2. Training Setup: Minimal and efficient training
3. Learning Signals: Imitate caregiver–child interaction
4. Evaluation: Perplexity, stability, consistency

## Relevance
- Cognitively plausible language modelling
- Human-centred, sustainable NLP
- Robust, safe, auditable model behaviour
## Usage
Run the training script with Python or on Google Colab GPU for accelerated experimentation.
