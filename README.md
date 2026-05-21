# BRANDVOICE AI

An AI-powered multi-agent social content generation system that researches live trends, summarizes real-time news, and generates platform-specific social media content in multiple adaptive brand voices.

The project uses:
- Tavily API for live trend and news research
- Gemini API for AI-powered summarization and content generation
- Modular agent architecture for scalable AI workflows

The system is designed to simulate modern AI-powered content automation pipelines used in branding, marketing, and social media systems.

---

# Project Overview

BrandVoice AI is a multi-agent AI system designed to automate social media content generation using live internet research and adaptive brand voice modeling.

The workflow begins with a user-provided topic. The system then:

1. Fetches live news and trending information
2. Summarizes key insights using Gemini
3. Adapts content according to selected brand voice
4. Generates:
   - LinkedIn posts
   - X/Twitter posts
5. Stores generated outputs and logs

The project demonstrates:
- AI agent orchestration
- prompt engineering
- live AI pipelines
- adaptive content generation
- platform-specific AI writing
- modular AI architecture

---

# Features

## Multi-Agent AI Architecture

The project follows a two-agent workflow.

### Research Agent
Responsible for:
- fetching live news
- collecting trends
- summarizing research
- preparing contextual insights

### Copywriter Agent
Responsible for:
- adaptive brand voice generation
- social media content creation
- platform-specific formatting
- engagement-focused writing

This modular separation improves:
- scalability
- maintainability
- workflow clarity
- AI orchestration

---

## Live Trend & News Research

The Research Agent uses Tavily API to fetch:
- live news
- trending topics
- current events
- industry developments

This ensures generated content remains:
- current
- relevant
- context-aware

instead of relying on static prompts.

---

## AI-Powered Summarization

Gemini API is used to:
- summarize live news
- extract important trends
- identify key insights
- prepare contextual information

This structured summarization improves the quality and relevance of generated posts.

---

## Adaptive Brand Voice Generation

The Copywriter Agent dynamically changes writing style based on selected brand voice.

Supported voices include:

- Corporate
- Startup Founder
- Minimalist
- Gen-Z
- Luxury Brand
- Tech Influencer

Each voice modifies:
- vocabulary
- tone
- sentence structure
- pacing
- formatting
- engagement style

---

## Multi-Platform Content Generation

The system generates:

### LinkedIn Content
Optimized for:
- professional engagement
- thought leadership
- structured storytelling
- industry discussions

### X/Twitter Content
Optimized for:
- concise communication
- short-form engagement
- viral-style formatting
- fast readability

---

## Retry Mechanism

The application includes retry handling for temporary failures such as:
- API rate limits
- network interruptions
- incomplete AI responses
- temporary generation failures

This improves system reliability and workflow stability.

---

## Validation & Error Handling

The project includes:
- input validation
- retry logic
- structured exception handling
- graceful failure management

This improves production-level robustness.

---

## Logging System

A dedicated logging module tracks:
- execution flow
- API calls
- retries
- failures
- workflow execution

Logs are stored for monitoring and debugging.

---

## Output Storage

Generated outputs are automatically stored inside the `outputs/` directory.

Stored outputs include:
- LinkedIn posts
- X/Twitter posts
- research summaries
- structured JSON outputs

---

# Tech Stack

## Programming Language
- Python

---

## AI Models & APIs
- Gemini API (gemini-2.5-flash)
- Tavily API

---

## Frameworks & Libraries
- LangChain
- CrewAI
- tavily-python
- rich

---

# Project Architecture

```text
┌─────────────────────────────────────┐
│ User Topic Input                    │
└──────────────────┬──────────────────┘
                   ↓
┌─────────────────────────────────────┐
│ Research Agent                      │
│ Handles live trend research         │
└──────────────────┬──────────────────┘
                   ↓
┌─────────────────────────────────────┐
│ Tavily API                          │
│ Fetches live news & trends          │
└──────────────────┬──────────────────┘
                   ↓
┌─────────────────────────────────────┐
│ Gemini API                          │
│ Summarizes research context         │
└──────────────────┬──────────────────┘
                   ↓
┌─────────────────────────────────────┐
│ Validation Layer                    │
│ Checks summary quality              │
└───────────────┬─────────────────────┘
                │
     ┌──────────┴──────────┐
     │ Validation Success  │
     │                     │
     ↓                     ↓
Continue             Validation Failed
     │                     │
     │               Retry Generation
     │                     │
     └──────────┬──────────┘
                ↓
┌─────────────────────────────────────┐
│ Copywriter Agent                    │
│ Applies selected brand voice        │
└──────────────────┬──────────────────┘
                   ↓
┌─────────────────────────────────────┐
│ Gemini API                          │
│ Generates social media content      │
└──────────────────┬──────────────────┘
                   ↓
┌─────────────────────────────────────┐
│ Platform Formatter                  │
│ Structures LinkedIn & X posts       │
└──────────────────┬──────────────────┘
                   ↓
┌─────────────────────────────────────┐
│ Outputs + Logs                      │
│ Stores generated content & logs     │
└─────────────────────────────────────┘
```

---

# Folder Structure

```text
BrandVoiceAI/
│
├── app/
│   ├── main.py
│   ├── researcher_agent.py
│   ├── copywriter_agent.py
│   ├── voice_profiles.py
│   ├── tools.py
│   ├── config.py
│   ├── utils.py
│   └── logger.py
│
├── outputs/
│   └── Stores generated posts and summaries
│
├── logs/
│   └── Stores execution logs and retry logs
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

# Installation

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

### Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure API Keys

The project stores API keys directly inside:

```text
app/config.py
```

Users need to manually paste their API keys inside this file before running the project.

---

## Step 1 — Create Gemini API Key

1. Open Google AI Studio
2. Sign in with your Google account
3. Click “Get API Key”
4. Create a new API key
5. Copy the generated API key

Official Website:

https://aistudio.google.com/app/apikey

---

## Step 2 — Create Tavily API Key

1. Open Tavily
2. Create account / Sign in
3. Generate API key
4. Copy generated API key

Official Website:

https://www.tavily.com/

---

## Step 3 — Open Configuration File

Open:

```text
app/config.py
```

You will find:

```python
GOOGLE_API_KEY = "YOUR_API_KEY"

TAVILY_API_KEY = "YOUR_API_KEY"
```

---

## Step 4 — Paste Your API Keys

Replace:

```python
"YOUR_API_KEY"
```

with your actual API keys.

Example:

```python
GOOGLE_API_KEY = "AIzaSyXXXXXXXXXXXX"

TAVILY_API_KEY = "tvly-XXXXXXXXXXXXXXXX"
```

---



# Run Project

```bash
python -m app.main
```

---

# Example Workflow

1. User enters topic
2. Research Agent fetches live news
3. Tavily API retrieves trend information
4. Gemini summarizes live context
5. Validation layer checks generated summary
6. Retry mechanism handles temporary failures
7. Copywriter Agent applies selected brand voice
8. Gemini generates:
   - LinkedIn post
   - X/Twitter post
9. Outputs and logs are stored

---

# Example Topics

- Future of AI in business
- AI replacing traditional search engines
- Evolution of cricket
- Luxury fashion industry
- Electric vehicles and Tesla

---

# Example Brand Voices

- Corporate
- Startup Founder
- Minimalist
- Gen-Z
- Luxury Brand
- Tech Influencer

---

# Key Capabilities

- Multi-agent AI workflow
- Adaptive brand voice generation
- Live trend analysis
- AI-powered summarization
- Platform-specific content generation
- Retry handling architecture
- Prompt engineering pipeline
- Structured logging system
- AI workflow orchestration

---

# Future Improvements

- Streamlit dashboard
- Instagram caption generation
- Threads support
- AI image prompt generation
- Content scheduling
- Multi-language support
- Analytics dashboard
- Team collaboration workflow

---

