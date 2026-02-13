# 📊 Text Sentiment Analyzer

A lightweight command-line Python tool that analyzes text sentiment, identifies top words, and renders an ASCII word cloud—all without external dependencies.

Perfect for rapid prototyping where a production sentiment model will be integrated later.

---

## ✨ Features

- **Rule-based sentiment scoring** using positive and negative word lists
- **Sentiment classification**: `positive` / `neutral` / `negative` with numeric score
- **Word frequency analysis** with automatic stop-word filtering
- **ASCII word cloud** visualization in your terminal
- **Zero dependencies** — runs on Python 3.8+ standard library

---

## 📁 Project Structure

```
sentiment-analyzer/
├── sentiment_analyzer.py    # Main analyzer & CLI
└── README.md                 # Documentation
```

---

## 🎯 Intended Use

This tool is designed as a **prototype/placeholder** for sentiment analysis workflows. Ideal for:

- 🚀 **Rapid prototyping** of UX flows requiring sentiment feedback
- 🧪 **Testing environments** where deterministic, lightweight analysis is needed
- 🎨 **Demo applications** while evaluating ML-based sentiment models
- 🔄 **Easy migration path** to production models (transformers, RNNs, or APIs)

---

## 💻 Requirements

- Python **3.8** or newer
- No external packages required

Uses only standard library modules (`re`, `collections`)

---

## 🚀 Installation & Usage

### Quick Start

1. **Download** the script:
   ```bash
   wget https://your-repo.com/sentiment_analyzer.py
   # or save the file manually
   ```

2. **Run** the analyzer:
   ```bash
   python sentiment_analyzer.py
   ```

### Example Session

```
$ python sentiment_analyzer.py

TEXT SENTIMENT ANALYZER
========================

Enter text (finish with an empty line):
I loved the movie. It was amazing and beautiful,
but the ending was disappointing.

Overall: NEUTRAL  |  Score: 11.11%  |  +:3  -:1

WORD CLOUD
----------
**AMAZING**  **BEAUTIFUL**  loved  movie  ending  disappointing

TOP WORDS
amazing       | █ (1)
beautiful     | █ (1)
loved         | █ (1)
movie         | █ (1)
ending        | █ (1)
disappointing | █ (1)
```

---

## ⚙️ How It Works

The analyzer follows a simple pipeline:

1. **Text Preprocessing**
   - Convert to lowercase
   - Remove punctuation
   - Tokenize into words

2. **Word Filtering**
   - Remove very short tokens (< 2 characters)
   - Filter common stop words

3. **Sentiment Scoring**
   - Compare tokens against positive/negative word sets
   - Calculate: `score = (pos_count - neg_count) / total_words × 100`

4. **Classification Thresholds**
   - Score **> +5%** → `positive`
   - Score **< -5%** → `negative`
   - Otherwise → `neutral`

---

## 🎨 Customization Guide

### Modify Word Lists

Edit the word sets in `SentimentAnalyzer.__init__()`:

```python
self.positive = {"amazing", "beautiful", "excellent", "love", ...}
self.negative = {"terrible", "awful", "hate", "disappointing", ...}
self.stop_words = {"the", "is", "at", "which", ...}
```

### Adjust Sensitivity

Change thresholds in `analyze_sentiment()`:

```python
if score > 5.0:      # Make more/less sensitive
    return "positive", score
elif score < -5.0:
    return "negative", score
```

### ASCII Cloud Styling

Modify `generate_ascii_cloud()` to change highlighting:

```python
# Current: bold uppercase for sentiment words
# Customize: colors, emoji, or size-based formatting
```

---

## 🔄 Migration to ML Models

### Option 1: Drop-in Replacement

Create a new class implementing the same interface:

```python
class MLSentimentAnalyzer:
    def analyze_sentiment(self, text: str) -> tuple:
        # Call your model here
        prediction = model.predict(text)
        return sentiment_label, confidence_score
    
    def get_word_frequency(self, text: str) -> dict:
        # Keep same or adapt
        pass
```

### Option 2: Wrapper Approach

Wrap an API or model inside existing `analyze_sentiment()`:

```python
def analyze_sentiment(self, text):
    # Add ML call here
    api_result = requests.post("https://api.sentiment.com", json={"text": text})
    
    # Keep rule-based as fallback
    if api_result.status_code != 200:
        return self._rule_based_analysis(text)
```

---

## ⚠️ Limitations

| Aspect | Current State | For Production |
|--------|---------------|----------------|
| **Method** | Rule-based word lists | Use trained ML models |
| **Tokenization** | Basic split | Handle contractions, phrases |
| **Language** | English only | Multi-language support |
| **Accuracy** | Prototype-level | Context-aware models |
| **Performance** | Synchronous | Consider async for scale |

> **Note**: This tool is **not intended for production sentiment analysis**. Use transformer models (BERT, RoBERTa) or commercial APIs for accuracy-critical applications.

---

## 🤝 Contributing

Contributions welcome! Focus areas:

- Expanding positive/negative word lists
- Improving word cloud visualization
- Adding command-line arguments
- Documentation improvements

**Process**: Open a PR or edit the file directly for small changes.

---

## 📄 License

**MIT License** — use and modify freely.

```
Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

---

## 🔗 Resources

- [Python `re` module docs](https://docs.python.org/3/library/re.html)
- [NLTK for production NLP](https://www.nltk.org/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)

---

<div align="center">

**Built with ❤️ for rapid prototyping**

⭐ Star this project if you find it useful!

</div>