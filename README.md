# NLP Basics: Preprocessing & Vectorization

## Overview
This notebook walks through a simple NLP pipeline: cleaning raw text and turning it into numbers for machine learning. The focus is on core ideas, not fancy tricks.

---

## Goals
- Why preprocessing matters  
- Basic cleaning steps  
- Converting text into features  

---

## Phase 1: Cleaning Text
Models can’t use raw text, so we tidy it up:

1. **Lowercase** – keep words consistent (`Python` → `python`)  
2. **Remove punctuation** – strip symbols, keep words and spaces  
3. **Tokenize** – split text into words  
4. **Stopwords** – drop common fillers like *the*, *is*, *a*  
5. **Stemming (simple)** – trim endings like `ing` (just a demo)  

---

## Phase 2: Numbers from Text
We turn words into vectors:

- **Bag of Words** – counts word frequency  
- **TF-IDF** – adjusts weights so rare but important words matter more  

