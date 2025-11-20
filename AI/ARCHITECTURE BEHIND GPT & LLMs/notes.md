🔹 1. Before Transformers: LSTMs (The Old Way)

LSTM = Long Short-Term Memory networks

They were used before modern LLMs to process sequences like text.

How LSTMs worked

They read text one token at a time, in order.

They remembered some past information using “memory cells”.

Problems
Issue	Why it matters
Slow	Must read text step-by-step
Short memory	Forget long text, weak at long sentences
Hard to train	Gradient issues

🔎 Analogy:
Reading a book one word per second and forgetting what happened in Chapter 1.

🔹 2. Transformers (The New Way)

Paper: "Attention is All You Need" (2017)

Key idea

Instead of reading words one-by-one, transformers look at everything at once using self-attention.

Why transformers are better
Feature	Benefit
Self-Attention	Model knows which words matter
Parallel processing	Much faster
Long context	Better memory
Scales with compute	Bigger models → better performance

🔎 Analogy:
Instead of reading a book slowly, you scan whole pages and instantly notice important parts.

🔹 Evolution Timeline
Era	Architecture	Example
Pre-2017	LSTM, RNN	Siri (early)
2017+	Transformer	GPT-1 onwards
2023+	Hybrid + MoE + Reasoning	GPT-4, Claude 3, Gemini, DeepSeek
🔹 GPT Model Sizes Over Time (Parameters)

Parameters = "knobs in the brain" model learns during training.

Model	Year	Parameters
GPT-1	2018	117M
GPT-2	2019	1.5B
GPT-3	2020	175B
GPT-4 (estimated)	2023	~1.7T (multi-model mixture)

⚠ Note: GPT-4 isn't one single model—likely many smaller models stitched with routing (MoE/hybrid).

Why parameter count matters

More parameters → more knowledge → better reasoning

But:

Costs more

Slower

More energy + hardware required

🔎 Analogy:
Bigger brain = smarter, but requires more food + sleep.

🔹 What Are Tokens? (Very Simple)
Early ML: Character-Level Models

Model predicted next character: "H → e → l → l → o"

Very small vocabulary

But model had to learn too much manually (grammar, spacing, words)

Next: Word-Level Models

Each word = token

Problem: too many words in languages + spelling variations

Breakthrough: Sub-Word Tokens (Current Method)

Tokens are chunks of text, not characters or full words.

Example:

"playing" → play + ing

"unbelievable" → un + believe + able

Rule of Thumb (English)
Relationship	Value
1 token ≈ 4 characters	
1 token ≈ 0.75 words	
1000 tokens ≈ ~750 words	

So if prompt = 10,000 tokens → ~7,500 words.

🔹 Why Tokens Matter in APIs?

LLM calls are stateless:

The model does not remember previous conversation

We must send full conversation history every time

More tokens = more cost

🔎 Analogy:
Each time you talk to someone with amnesia, you retell the entire story.

What ChatGPT does

It stores past messages and resends them each time behind the scenes—gives illusion of memory.

🔹 Context Window

Context window = max tokens model can see at once.

Example:

GPT-3 → 2K tokens

GPT-4 → 128K tokens

Gemini 2.0 → 1M+ tokens

Claude 3.5 → 200K tokens

Larger context = model remembers more messages + documents.

But:

More tokens = more compute

Slow + expensive

🔹 Cost Structure (How API Pricing Works)

Pricing is based on:

Type	Meaning
Input tokens	What you send to model
Output tokens	What model replies with

Pricing formula:

Total cost = (input_tokens × rate_in) + (output_tokens × rate_out)


Example:
1000 tokens sent + 500 tokens reply
If cost = $1 per million tokens:

1500 tokens = 0.0015M → $0.0015

🔹 Final Summary (For Fast Revision)

LSTM → slow + short memory

Transformers → parallel + self-attention → modern models

Parameters → size of "brain"; larger = smarter & costlier

Tokens = text pieces (1 token ~ 4 chars ~ 0.75 words)

LLM calls are stateless → resend history every time

Context window limits how much model can "see"

API cost = tokens in + tokens out
