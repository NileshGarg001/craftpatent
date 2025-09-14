# CraftPatent 🚀

Modern patent drafting and quality assessment platform powered by Google ADK (Agent Development Kit). Streamlines patent application creation with intelligent automation and iterative quality improvement.

## Overview

CraftPatent uses an **iterative refinement approach** to automatically draft and improve patent applications. The system takes invention disclosures as input and produces high-quality patent drafts through multiple improvement cycles.

## Architecture

### LoopAgent Workflow
The system uses Google ADK's `LoopAgent` to orchestrate an iterative improvement process:

```
Invention Disclosure → Draft → Rate → Improve → Rate → ... → Final Patent
                      ↑____________________↓
                         (up to 5 iterations)
```

### Core Components

#### 1. Draft Patent Agent (`draft_patent_agent`)
- **Purpose**: Creates and improves patent drafts
- **Input**: Invention disclosure (iteration 1) + previous rating feedback (iterations 2+)
- **Output**: Complete patent draft with all required sections
- **Key Features**:
  - USPTO-compliant formatting
  - Comprehensive claim construction
  - Technical specification generation

#### 2. Rate Patent Agent (`rate_patent_agent`) 
- **Purpose**: Evaluates patent quality across multiple dimensions
- **Input**: Current patent draft
- **Output**: Detailed quality assessment with scores
- **Evaluation Criteria**:
  - Novelty & Inventive Step (1-10)
  - Clarity & Sufficiency of Disclosure (1-10)
  - Claim Construction & Scope (1-10) 
  - Industrial Applicability (1-10)
  - Overall Grantability Score (1-10)

#### 3. Coordinator LoopAgent (`coordinator_agent`)
- **Purpose**: Manages the iterative improvement process
- **Max Iterations**: 5 cycles
- **Session State**: Maintains `current_draft` and `current_rating` between iterations
- **Termination**: Automatically stops after 5 iterations

## File Structure

```
craftpatent/
├── coordinator_agent/           # Multi-agent system
│   ├── __init__.py             # Package initialization
│   ├── agent.py                # Main LoopAgent and sub-agents
│   └── prompts.py              # All agent prompts
├── sample1.txt - sample9.txt   # Test invention disclosures
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Container configuration
├── cloudbuild.yaml            # CI/CD pipeline
└── .dockerignore              # Docker build exclusions
```

## Setup & Installation

1. **Clone and Setup**:
   ```bash
   cd /home/nilesh-garg/projects/agentic/craftpatent
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configure Environment**:
   - Ensure Google ADK credentials are properly configured
   - Set up Gemini API access for the `gemini-2.5-flash` model

3. **Run the System**:
   ```bash
   source venv/bin/activate
   adk web
   ```

## Usage

1. **Start ADK Web Interface**: Run `adk web` in the project directory
2. **Input Invention Disclosure**: Paste your invention description in the chat interface
3. **Iterative Improvement**: The system automatically:
   - Drafts initial patent application
   - Rates the quality (1-10 scale)
   - Improves draft based on feedback
   - Repeats for up to 5 iterations
4. **Final Output**: Receive polished patent draft ready for attorney review

## Test Cases

### High-Quality Inventions (Expected to pass quickly)
- `sample1.txt` - Smart Water Bottle with IoT Integration
- `sample2.txt` - AI-Enhanced Code Review System
- `sample4.txt` - Quantum-Enhanced Solar Cell

### Low-Quality Inventions (Expected to require all 5 iterations)
- `sample8.txt` - Method for Using Email (obvious prior art)
- `sample9.txt` - Water Drinking Reminder (trivial invention)

## Key Features

✅ **Iterative Quality Improvement**: Up to 5 refinement cycles
✅ **Multi-Dimensional Quality Assessment**: Comprehensive scoring system
✅ **USPTO Compliance**: Proper patent formatting and structure
✅ **Session State Management**: Persistent improvement tracking
✅ **Automated Workflow**: No manual intervention required
✅ **Test Coverage**: Multiple sample inventions for validation

## Technology Stack

- **Framework**: Google ADK (Agent Development Kit) v1.14.0
- **LLM**: Gemini 2.5 Flash
- **Architecture**: LoopAgent with sub-agents
- **Language**: Python 3.12+
- **Dependencies**: See `requirements.txt`

## Recent Updates

- **v2.0**: Complete rewrite using LoopAgent architecture
- Simplified from complex multi-agent hierarchy to clean 2-agent workflow
- Fixed iteration failures with proper session state mapping
- Consolidated all prompts into single file
- Removed async complications with custom BaseAgent classes
- Added comprehensive test cases for validation

## Future Enhancements

🔄 **Score-Based Termination**: Stop when quality threshold (7.0+) is reached
📄 **PDF Generation**: Convert final drafts to USPTO-ready PDF format
🔍 **Prior Art Integration**: Automated patent search and conflict detection
📊 **Analytics Dashboard**: Quality improvement tracking and metrics
🤝 **Attorney Integration**: Direct handoff to patent professionals
