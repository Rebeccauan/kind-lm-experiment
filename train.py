# Minimal training script for KIND-LM pilot experiment
# Cognitively-inspired, sample-efficient language modeling on child speech data

from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from datasets import Dataset
import math

# ------------------------------------------------------------------------------
# Child speech corpus (cleaned CHILDES Demetras, child-only utterances)
# ------------------------------------------------------------------------------
data = """that's my water
I'm gonna uh reek it
put it in duh boat
yeah
cars go in there
cars go in there
dere's water in dere Dada
dere's water in dere Dada
look at dis water Dada
uh ah
go sit down on duh padwo
yeah
don't tuuk my water
no I um
I gotta say cheese
uh eh
I gotta say cheese
oh dere's duh aiwpwane comin
beeuo
I'm kwert duh aiwpwane
kwert dee airplane
kwer duh airplane
yeah
Dada look at dis one
look look look
look at my tick inna h
look at my tick in here
ah it's driving away
yeah
look at dis Dada
whoo whoo whoo whoo whoo
and a dwiveway
in duh driveway
oooo eeso
and a dwiveway
it's a dwiveway
it's a dwiveway
it's nos a bwes dwiveway
no I don't want my car back out
it's a dwiveway Dad
it's a dwiveway
yeah
it it's my driveway
das dwiveway Dad
dat a dwiveway Daddy
dere's my car
i's i's got a howe in it
aap dere's di airplane
me ap
I hafta kwert it
bee beeuo beeuo beeuo beeuo
yeah
no no
I show I show you my gun
das my gun
dere's my gun
beeuo
I kwert duh airplane
no I kwert dee airplane
kwert dee airplane
kwert dee airplane
yeah
like like with zis gun
yeah
sshee my gun
sshee my gun
can't get it out
beeuo beeuo beeuo
I kwert de airplane
beeuo beeuo
yeah
beeuo beeuo beeuo beeuo beeuo beeuo beeuo beeuo
I fink dat a heocopter
beeuo beeuo
beeuo beeuo
dat an airplane an za on nere
um nothing
cowboy
der gotta go in duh right way
wike my car
wike wike dis car
wike dis car Dada
is inna water
ee ee eann gave me dis
ee eann gave me
gave dis
yeah eann gave me dis car
cars in duh water
dere's cars in duh water
and dere's my peoples in duh water
dere gun weep in duh water
dat make habwa egada weep
dat make habwa iguna weep
put duh cars in dere
there's nothing in here
Daddy Daddy dere's nothing in dere
oh dere's nothing in dere
get them
duh cowboys outta dere
yeah every everything goes in duh water
um zebra
it's it's uh carry it
yeah
suitcase with me
suitcase
yeah
everybody gotta go in duh water
yeah just like at Helen's house
soomo
soomo
soomo
zoom
zoom
whee
stick
yeah
from my flower
how bout my coffee pot
um put some water in nere
yeah
sssso
sssso
not post too pill it
I did
cowboy dat alright
cowboy dat alright
yeah
cowboy alright in
cowboy's alright
he's alright
yeah
he's still weepin o here
he's still sleeping
uh more water
pu more water
uh more water
water here
water here
nuh we hafta put peoples in here
I hafta make ie_cweam
I hafta make ie_cweam
um on your bottom
dat uh badder on your bottom
no no dat a fader
yeah
see my fatterf right here
das not a bwenner
um sa fatterc
more ie_cweam
yeah yeah you get fwe
um wed ie_cweam
yeah
it's just chwakit
this orange
yeah
yeah deez guys want ice cream
these guys
deez guys want some ie cweam
way down
der gonna get ie cweam
have lotsa cow cowboy give ice cream
dere ants er chair
he gots his own chair
yeah
yeah eat ie cweam
yeah dis wike a miok shake
dis wike a miok shake
dis wike a miok shake
look it this
deez guys both
both
both
deez guys boht Dada
day bohs horn
day bohs horn Dada
day day bohs gotta horn
day bohs gotta horn
he fall on his head
he fell on his head
his head too
day bohs gotta horn
yeah dat a horn
no dat a horn
no dat a horn
that's a horn
that's a horn
its not cor a car horn
it's a car horn
dat dat your waio there
just a little
yeah
now d now der eat chwakit
yeah
oops
uuuo
day both fall over
das your waio
move
bohs peoples falled down
bohs peoples falled down
bohs horns falled down
da horn oops
mm one horn
one horn fall over
yeah
tsame here
Kay now der eat ice cream
becaud hoonac turn laho eat ie cweam
yeah
dat a cwown Dada
that's a clown
yeah
um cowboy
yeah
dat mehder cowmboy
he's a cowboy too
he's a cowboy too
he's got a hat
he's got a hat
he's got a hat
he's got a hat Dada
he's got a hat
not me
not me
I have a hat
yeah
in in Tucson
I have a hat in Tucson
yeah many hats in Tucson
he fall over
he tur ah
more ie cweam Dada
yeah
what's that
das your watch
day want more ie cweam
way over
"""

# Prepare dataset
lines = [line.strip() for line in data.splitlines() if line.strip()]
# ============================================================
# Approach 2: Remove reference sentences (all occurrences) before splitting
# ============================================================

# 1. Define the list of reference sentences (the 10 you manually selected)
reference_sentences = [
    "uh more water",
    "dere's my car",
    "look at dis Dada",
    "it's a dwiveway",
    "he's still sleeping",
    "yeah eat ie cweam",
    "no dat a horn",
    "bohs peoples falled down",
    "he's got a hat",
    "put it in duh boat"
]

# 2. Convert to a set for fast lookup
ref_set = set(reference_sentences)

# 3. Filter out all sentences that appear in the reference set (including duplicates)
filtered_lines = [line for line in lines if line not in ref_set]

# 4. Report how many sentences were removed
removed_count = len(lines) - len(filtered_lines)
print(f"Removed {removed_count} sentences (including duplicates) from the corpus.")

# 5. Create a Dataset from the filtered data
dataset = Dataset.from_dict({"text": filtered_lines})

# 6. Then proceed with the 90/10 split as usual
dataset_split = dataset.train_test_split(test_size=0.1, seed=42)
train_dataset = dataset_split["train"]
eval_dataset = dataset_split["test"]
# ------------------------------------------------------------------------------
# Model & Tokenizer: DistilGPT2 (lightweight, sustainable LM)
# ------------------------------------------------------------------------------
tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained("distilgpt2")

# Tokenization
def tokenize_fn(examples):
    return tokenizer(examples["text"], truncation=True, padding="longest", max_length=64)
outputs["labels"] = outputs["input_ids"].copy()
tokenized_train = train_dataset.map(tokenize_fn, batched=True)
tokenized_eval = eval_dataset.map(tokenize_fn, batched=True)

tokenized_train.set_format("torch", columns=["input_ids", "attention_mask"])
tokenized_eval.set_format("torch", columns=["input_ids", "attention_mask"])

# ------------------------------------------------------------------------------
# Training configuration (matches experiment plan)
# ------------------------------------------------------------------------------
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=10,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    learning_rate=5e-5,
    eval_strategy="epoch",
    save_strategy="epoch",
    logging_dir="./logs",
    logging_steps=10,
    report_to="none",
    seed=42
)

# Train
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_train,
    eval_dataset=tokenized_eval
)
trainer.train()

# ------------------------------------------------------------------------------
# Evaluation: Perplexity (core metric)
# ------------------------------------------------------------------------------
eval_results = trainer.evaluate()
perplexity = math.exp(eval_results["eval_loss"])
print("\n==========================================")
print(f"Validation Perplexity: {perplexity:.2f}")
print("==========================================\n")

# ------------------------------------------------------------------------------
# Generate 10 child-like utterances (matched to reference set)
# ------------------------------------------------------------------------------
from transformers import pipeline
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

prompts = [
    "uh more",
    "dere's",
    "look at",
    "it's",
    "he's",
    "yeah eat",
    "no dat",
    "bohs",
    "he's got",
    "put it"
]


print("--- Generated Child Utterances ---")
generated = []
for i, prompt in enumerate(prompts):
    output = generator(prompt, max_new_tokens=15, do_sample=True, temperature=0.4, pad_token_id=tokenizer.eos_token_id)[0]["generated_text"]
    generated.append(output)
    print(f"{i+1:2d}. {output}")

# ------------------------------------------------------------------------------
# Evaluation metrics: BERTScore
# ------------------------------------------------------------------------------

from bert_score import BERTScorer

# Generated sentences are already in `generated` list

# BERTScore
scorer = BERTScorer(lang="en", rescale_with_baseline=True)
P, R, F1 = scorer.score(generated, reference_sentences)
print(f"BERTScore F1: {F1.mean():.4f}")
