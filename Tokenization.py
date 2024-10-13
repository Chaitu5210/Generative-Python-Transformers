from tokenizers import ByteLevelBPETokenizer
from transformers import GPT2Config, GPT2LMHeadModel, GPT2Tokenizer, DataCollatorForLanguageModeling
from datasets import load_dataset
from transformers import Trainer, TrainingArguments

paths = ["Python_Data.txt"]
NotTrained = False  # Change to True if you want to train a new tokenizer

# Train the tokenizer if needed
if NotTrained:
    tokenizer = ByteLevelBPETokenizer()
    tokenizer.train(files=paths, vocab_size=52_000, min_frequency=2, special_tokens=[
        "<s>",
        "<pad>",
        "</s>",
        "<unk>",
        "<mask>",
    ])
    tokenizer.save_model("WordTokens")
    print("Tokenizer trained and model saved successfully!")

# Load the tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('WordTokens')

# Add special tokens
tokenizer.add_special_tokens({
    "eos_token": "</s>",
    "bos_token": "<s>",
    "unk_token": "<unk>",
    "pad_token": "<pad>",
    "mask_token": "<mask>"
})

# Sample input to verify the tokenizer
inp = 'print("Hello World!")'
t = tokenizer(inp)
print(t)
decoded_input = tokenizer.decode(t['input_ids'])
print(decoded_input)

# Configure the model
config = GPT2Config(
    vocab_size=tokenizer.vocab_size,
    bos_token_id=tokenizer.bos_token_id,
    eos_token_id=tokenizer.eos_token_id
)
model = GPT2LMHeadModel(config)

# Load and preprocess the dataset
dataset = load_dataset("text", data_files=paths)

# Define the encoding function
def encode(lines):
    return tokenizer(lines['text'], add_special_tokens=True, truncation=True, max_length=512)

# Apply the encoding to the dataset
dataset = dataset.map(encode, batched=True, remove_columns=["text"])

# Set up the data collator
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=True, mlm_probability=0.15)

# Training arguments
training_args = TrainingArguments(
    output_dir="GPyT",
    overwrite_output_dir=True,
    num_train_epochs=1,
    per_device_train_batch_size=10,
    save_steps=100,
    save_total_limit=2,
    prediction_loss_only=True,
    remove_unused_columns=False,
)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset['train'],
)

# Train and save the model
trainer.train()
trainer.save_model("GPyT")
