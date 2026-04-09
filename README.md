# KIND-LM Style Experiment Design: Clean & Efficient Language Learning
This project outlines a cognitively inspired, sample-efficient language modeling experiment aligned with the KIND-LM project.

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
Why child‑only corpus?
This corpus trains the child model only on child‑produced utterances. It captures the starting point of language acquisition: simple, repetitive, sometimes non‑standard speech. This allows the model to later benefit from implicit feedback from a parent model, rather than being directly fed adult‑like correct forms.

Next step – parent model
A separate parent model (trained on clean, adult input or a stronger pre‑trained LM) will be introduced. It will recast the child’s output into correct forms, enabling the child model to self‑correct through comparison – exactly as described in the KIND‑LM project.
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

## Planned Extension: TinyBERT for Visually Impaired Child Language
A follow-up experiment is planned using TinyBERT (4M–6M) — a highly compact model designed specifically for resource-constrained environments. Its extremely small size makes it cognitively plausible for modeling the early stages of language acquisition, where cognitive capacity is naturally limited. This model will be evaluated on speech data from visually impaired children, whose language development follows a distinct, perceptually constrained trajectory. The goal is to explore how small model capacity and restricted input modalities interact to shape linguistic generalization.
