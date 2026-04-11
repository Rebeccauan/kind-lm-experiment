# Experiment Plan

## Research Question
How can developmentally appropriate child speech input and cognitively plausible interaction patterns improve sample efficiency and linguistic consistency in small-scale language models?

## Data
- Cleaned spontaneous utterances from CHILDES Demetras Corpus
- Only child-produced speech (CHI:), filtered for noise and annotations
- Natural, repetitive, early-childhood linguistic patterns
- Held out 10 manually selected reference child utterances as held-out items.

## Model
- Lightweight autoregressive LM: DistilGPT2
- Low-resource, sustainable, cognitively plausible scale

## Training
- Train/validation split: 90/10
- Epochs: 10
- Batch size: 4
- Evaluation: Perplexity (PPL) on validation set

## Generation & Evaluation
- Generate 10 child-like utterances from natural prompts (using the same prefixes as the held-out reference sentences)
- Quantitative evaluation:
  - Perplexity on validation set (core fluency metric)
  - BERTScore against the 10 held-out reference sentences (semantic similarity)
- Qualitative evaluation: manual inspection of generated utterances for child-like style, natural repetition, and grammatical plausibility
