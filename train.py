# Minimal training script for a small cognitively-inspired language model (KIND-LM experiment)
# Uses clean, simplified child-directed text for sample-efficient training
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from datasets import Dataset

# Small, clean child-directed text corpus
data = {
    "text": [
        "I like to play outside.",
        "The cat is small.",
        "She reads a book.",
        "We eat apples together.",
        "He has a red pen.",
        "They go to school.",
        "I see a big dog.",
        "My mother sings well.",
        "It is a sunny day.",
        "We are happy."
    ]
}

# Load dataset
dataset = Dataset.from_dict(data)

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained("distilgpt2")

# Tokenize data
def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=32)

tokenized_dataset = dataset.map(tokenize_function, batched=True)
tokenized_dataset.set_format("torch", columns=["input_ids", "attention_mask"])

# Set training arguments
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=5,
    per_device_train_batch_size=2,
    logging_dir="./logs",
    logging_steps=1,
    report_to="none"
)

# Initialize trainer and train
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
)

trainer.train()
