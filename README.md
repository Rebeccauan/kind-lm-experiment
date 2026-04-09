# KIND-LM Style Experiment Design: Clean & Efficient Language Learning
This project outlines a cognitively inspired, sample-efficient language modeling experiment aligned with the KIND-LM project at the University of Göttingen.

## Corpus
This project uses a subset of the CHILDES Demetras Corpus, which contains natural spontaneous interactions between a parent and a 2-year-old child named Trevor. The corpus consists of real-life recorded conversations, making it highly suitable for modeling early child language acquisition.

Raw utterances were cleaned in two processing steps:
1. Only utterances produced by the child (marked as *CHI:) were extracted.
2. Annotation symbols, timestamps, fillers, and irrelevant markers were removed to retain clean, natural child speech for model training.

All utterances are short, repetitive, semantically simple, and reflect the kind of language a child actually produces – which is the natural starting point before any adult-like input.

## Core Idea
- Clean, well-formed child-directed linguistic input
- Implicit naturalistic feedback (recasting & expansion)
- Small, sustainable model architectures
- Evaluation focused on robustness and interpretability
- Constraint-aligned modeling: matching model capacity with cognitive and perceptual constraints

## Why Child-only Corpus?
This corpus trains the child model only on child-produced utterances. It captures the starting point of language acquisition: simple, repetitive, sometimes non-standard speech. This allows the model to later benefit from implicit feedback from a parent model, rather than being directly fed adult-like correct forms.

## Next Step – Parent Model
A separate parent model (trained on clean, adult input or a stronger pre-trained LM) will be introduced. It will recast the child’s output into correct forms, enabling the child model to self-correct through comparison – exactly as described in the KIND-LM project.

## Experiment Design
1. Corpus Construction: Cleaned child-only utterances from CHILDES
2. Training Setup: Lightweight models with small batch size and limited epochs
3. Learning Signals: Imitate caregiver–child interaction patterns
4. Evaluation: Perplexity (PPL), generation consistency, stability
5. Comparative analysis between constrained and less constrained models

## Training Configuration
- Baseline Model: DistilGPT2
- Epochs: 10
- Batch size: 4
- Train/validation split: 90/10
- Evaluation: Perplexity on validation set

## Relevance
- Cognitively plausible language modelling
- Human-centred, sustainable NLP
- Robust, safe, auditable model behaviour

## Usage
Run the training script with Python or on Google Colab GPU for accelerated experimentation.

## Planned Comparative Extension: Constrained Model & Constrained Corpus
### Rationale
This follow-up experiment is based on a dual constraint matching design:
- Model Constraint: Use TinyBERT (4M–6M), an extremely compact model designed for resource-constrained environments. Its small size reflects the limited cognitive capacity in early childhood language acquisition.
- Corpus Constraint: Evaluate on speech data from visually impaired children (CHILDES Peters/Wilson Corpus), whose language development is shaped by restricted perceptual input.

Both the model and the population reflect natural constraints: one in learning capacity, the other in sensory modality. By comparing TinyBERT with DistilGPT2, we aim to identify which setup better aligns with the goals of KIND-LM: building cognitively plausible, sample-efficient, and developmentally realistic language models.

## Project Goals
- Explore lightweight and sustainable modeling for child language simulation
- Test whether matching model constraints to human cognitive/perceptual limits improves plausibility
- Provide a reproducible baseline for the full KIND-LM interaction framework
- Support research in human-centered, robust, and safe language modeling
