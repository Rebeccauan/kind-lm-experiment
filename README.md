# KIND-LM Style Experiment Design: Clean & Efficient Language Learning
This project outlines a cognitively inspired, sample-efficient language modeling experiment aligned with the KIND-LM project at the University of Göttingen.

## Corpus
This project uses a subset of the CHILDES Demetras Corpus, which contains natural spontaneous interactions between a parent and a 2-year-old child named Trevor. The corpus consists of real-life recorded conversations, making it highly suitable for modeling early child language acquisition.

Raw utterances were cleaned in two processing steps:
1. Only utterances produced by the child (marked as *CHI:) were extracted.
2. Annotation symbols, timestamps, fillers, and irrelevant markers were removed to retain clean, natural child speech for model training.
3. Held out 10 manually selected reference child utterances as held-out items.
4. Split the remaining corpus into 90% train / 10% validation
   
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
It will map child errors (phonological, morphosyntactic, semantic, pragmatic) to parental strategies (recast, expansion, clarification, ignore) and provide feedback in an interactive learning loop.

## Experiment Design
1. Corpus Construction: Cleaned child-only utterances from CHILDES
2. Training Setup: Lightweight models with small batch size and limited epochs
3. Learning Signals: Imitate caregiver–child interaction patterns
4. Evaluation: Perplexity (PPL), BERTScore,generation consistency, stability
5. Comparative analysis between constrained and less constrained models

## Training Configuration
- Baseline Model: DistilGPT2
- Epochs: 10
- Batch size: 4
- Train/validation split: 90/10
- Evaluation: Perplexity on validation set
- Metrics: Perplexity, BERTScore

## Relevance
- Cognitively plausible language modelling
- Human-centred, sustainable NLP
- Robust, safe, auditable model behaviour

## Usage
Run the training script with Python or on Google Colab GPU for accelerated experimentation.

## Planned Comparative Extension: Constrained Model & Constrained Corpus
### Rationale
This follow-up experiment is based on a dual constraint matching design:
- **Model Constraint**: Use TinyStories‑1M or TinyGPT(1M‑10M), an extremely compact model designed for resource-constrained environments. Its small size reflects the limited cognitive capacity in early childhood language acquisition.
- **Corpus Constraint**: Evaluate on speech data from visually impaired children (CHILDES Peters/Wilson Corpus), whose language development is shaped by restricted perceptual input.

Both the model and the population reflect natural constraints: one in learning capacity, the other in sensory modality. By comparing TinyStories‑1M with DistilGPT2, I aim to identify which setup better aligns with the goals of KIND-LM: building cognitively plausible, sample-efficient, and developmentally realistic language models.

## Project Goals
- Explore lightweight and sustainable modeling for child language simulation
- Test whether matching model constraints to human cognitive/perceptual limits improves plausibility
- Provide a reproducible baseline for the full KIND-LM interaction framework
- Support research in human-centered, robust, and safe language modeling

## Linguistic Observations from CHILDES

### A Corpus Linguist's Reading of the Demetras Transcript

- **Child Language as a Self-Contained System**

A close reading of the interactions between Trevor and his father reveals that the child's speech is not a defective imitation of adult language, but a systematic linguistic system in its own right. At the phonological level, substitutions appear with striking consistency: dental fricatives become alveolar stops, consonant clusters are simplified, liquids are replaced by glides. These are not random misarticulations; they form a stable set of correspondence rules that the child applies productively. Morphologically, irregular forms are regularized, and plural marking is overgeneralized—classic signatures of a creative, rule‑governed grammar. Syntactically, utterances tend toward a telegraphic structure, preserving content words while omitting functional morphemes, yet the communicative intent remains transparent. Pragmatically, the child initiates joint attention, asserts possession, and sustains pretend play scenarios with the same functional richness found in adult conversation. In essence, the child speaks a fluent idiolect of his own—a distinct linguistic system that differs from adult English in its surface forms but shares its underlying communicative architecture.

- **The Father as Interpreter, Not Corrector**

The father's response patterns are equally revealing. Explicit correction—the kind that would label an utterance as "wrong" and demand a revised production—is virtually absent. Instead, the father behaves like an interpreter. He receives a child utterance in one linguistic code, extracts its semantic intent, and then reformulates it in the adult code while continuing the flow of interaction. When the child produces a phonologically altered word, the father echoes the proposition with the adult phonological form, often embedded in a confirming question. When the child's meaning is unclear, the father requests clarification, then supplies the appropriate adult version once the intent is understood. At no point does the father halt the conversation to teach grammar. He is not a pedagogue; he is a conversational partner who happens to speak a different dialect—the dialect of adult English—and he consistently translates the child's contributions into that dialect. This is not error correction; it is code‑switching between two overlapping linguistic systems.

- **Assimilation Is Gradual and Statistical, Not Immediate**

Tracking a single linguistic item across multiple conversational turns reveals the gradual, probabilistic nature of assimilation. The child produces the same variant form repeatedly; the father provides the corresponding adult form with similar consistency. Yet the child does not immediately adopt the adult version. He continues using his own variant for an extended period, occasionally attempting approximations of the adult form, sometimes vacillating within the same episode. The father never insists on repetition, never withholds conversational engagement pending a correct production. He simply persists in using his own code. Over time, the sheer density of adult‑form input appears to exert a statistical pull, nudging the child's productions incrementally toward the adult norm. There is no identifiable teaching moment, only an extended, asymmetric language contact situation in which the stronger form gradually submerges the weaker one. This is the mechanism by which every child eventually leaves their idiolect behind: not through instruction, but through immersion.

- **Child Production Is Not Linear Planning, but Effortful Conversion from Intent**

Trevor's speech is marked by repetitions, self‑corrections, fillers, and hesitations. He often utters a core lexical item first and then retrofits modifiers; a single phrase may be repeated two or three times with minor variation; complex structures are accompanied by audible delays. These features suggest that child language production is not a smoothly linear, left‑to‑right planning process. Rather, it resembles an effortful conversion from a holistic communicative intention into a sequential stream of words. The child knows what he wants to express, but the encoding of that intention into an ordered series of articulatory gestures is cognitively demanding and non‑linear. This observation carries implications for model architecture. The dominant autoregressive paradigm—where each word is conditioned only on previously generated left context—captures the fluency of adult monologue more than the hesitant, recursive, self‑interrupting character of child speech. An architecture that separates intention representation (encoding) from effortful sequentialization (decoding) may offer a cognitively more faithful simulation. The tension between encoder and decoder mirrors the child's struggle to map a rich, parallel conceptual structure onto a strictly serial output channel.

- **Non‑Textual Annotations as Proxies for Multimodal Signals and Interaction Initiative**

The CHAT transcript format contains a wealth of information beyond the words themselves. Situation descriptions document the actions that accompany speech. Gesture annotations mark visual supplements to verbal meaning. Onomatopoeic transcriptions preserve sound effects as a legitimate communicative channel. Filled pauses and hesitations are explicitly marked, offering direct evidence of cognitive load. Emotion tags provide explicit labels for affective and need states. These annotations are rarely exploited in computational modeling, yet they constitute precisely the kind of signal that could indicate a child model's cognitive state. If a model could sense an increase in hesitation markers, a reliance on gesture, or a shift toward whiny affect, it could use these cues to proactively request parental feedback—a technical realization of interaction initiative. Full audiovisual streams may not be required; the existing in‑text annotations already provide a rich substrate for constructing lightweight proxy signals that move the child model from passive recipient to active participant in the learning loop.

- **The Deeper Question: Raising a Model the Way We Raise a Child**

Taken together, these observations converge on a fundamental distinction. Current large language models treat language as a statistical distribution to be fitted, variation as error to be minimized, and learning as unidirectional parameter optimization driven by massive data and a single prediction task. Trevor and his father enact a different paradigm: minimal samples, social interaction, communicative intent prioritized over formal accuracy, variation accepted as a legitimate developmental stage, and learning embedded in bidirectional, asymmetric, affectively rich dialogue. The KIND‑LM project inhabits the space between these two paradigms. It asks not how to make a model more powerful, but a more profound question: if we raise a model the way we raise a child—with limited, multimodal, interactive input; with acceptance rather than correction; with translation rather than instruction—can that model develop the kind of robust generalization and communicative flexibility that human children display? Answering this question matters not only for the technical trajectory of natural language processing, but for our understanding of language, learning, and intelligence itself.

### Note
These observations are based on a qualitative reading of the CHILDES Demetras corpus and are offered as linguistic grounding for the cognitively inspired modeling approach pursued in this project.

## Results

- **Validation Perplexity**: 32.98
- **BERTScore F1**: 0.0906
- **Best eval loss**: 3.161 (Epoch 5)
- **Final eval loss (Epoch 10)**: 3.496

Validation loss decreases at first as the model learns child speech patterns, then increases slightly due to mild overfitting on the small dataset — a typical behavior in low-resource child language modeling. No intervention is needed as the overfitting is minimal and generation quality remains consistent with child-like speech. The mild overfitting observed after Epoch 5 is typical for small-scale experiments with limited child speech data. Increasing the size of the training corpus would help reduce overfitting and improve generalization, which can be explored in future expanded work.
BERTScore F1 is low (0.0906) because the model is trained on phonetically spelled, fragmented, and repetitive child speech, which differs significantly from the standard, well-formed English that BERT is trained on. The low score reflects the non-standard nature of child utterances, not poor generation quality.

Note: The generated utterances appear relatively long due to `max_new_tokens` set during generation. The model tends to produce longer continuations given the generation length configuration, which can be adjusted for shorter, more fragmented child-like utterances.

The model generates natural child-like utterances, including:
- Phonetic spellings: *cweam, dere, dis, inna*
- Repetitive patterns: *Dada, look at*
- Short, fragmented, conversational turns

## Thoughts on the Experiment and Model Design Idea

From this experiment, I observed that even with a very small corpus and a simple decoder-only structure, the model can already generate child-like utterances by mimicking surface-level morphology. This shows that merely imitating children’s speech patterns can be achieved through shallow text pattern matching alone.

By examining the raw, unfiltered corpus, I also noticed many abrupt sentence breaks, fragmented expressions, sudden topic shifts, and special symbols that reflect sudden changes in children’s thinking or internal state. This made me realize that children’s language is driven by factors beyond textual context.

Combined with real-world observations of children’s behavior, I found that children’s speech is not limited to conversational context. They often utter words unrelated to the current dialogue because they see something, hear a sound, feel hungry, sleepy, or experience other physical or attentional changes. These seemingly illogical jumps actually have clear triggers.

Based on the experiment results, analysis of the unprocessed corpus, and real observations of children’s language behavior, I conclude that a decoder-only model cannot capture the logic, motivation, and authenticity of children’s language.

Current mainstream LLMs only take previous text as their single input source and ignore the internal and external triggers behind children’s utterances. In reality, children’s language generation relies on at least three types of input: linguistic input from parents, external sensory input (vision, hearing, etc.), and internal physical and attentional states. Parental speech is only one source.

From this, I plan to explore a multi-Encoder + single-Decoder architecture from an embodied cognition perspective, to better model how children actually produce language:

1. Parent Encoder: processes conversational context between parent and child, capturing dialogue intent and topic.

2. Sensory Encoder: encodes external sensory signals (visual, auditory) and internal physical states such as hunger or sleepiness, converting non-linguistic signals into usable representations.

3. Attention / Memory Encoder: models the child’s attention focus and short-term memory, ensuring that shifts in speech have reasonable triggers.

4. Child Decoder: fuses information from all three encoders to generate meaningful, logical, and developmentally appropriate language, rather than mindless text continuation.


## References
Demetras, M. (1989b). Working parents conversational responses to their two-year-old sons. Working paper. University of Arizona.
