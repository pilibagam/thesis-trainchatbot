# ÖBB Humor Study – oTree Experiment

This repository contains the oTree experiment used for the Master's thesis:

**"Mitigating Service Failures with Humor: The Impact of Chatbot Responses on Customer Experience in ÖBB"**

The experiment investigates how different chatbot humor styles (affiliative, self-defeating, neutral) influence user reactions to varying levels of service disruption (seat conflict vs. train cancellation).

---

## 🧪 Experiment Structure

The study consists of:

| Phase                  | Description |
|-----------------------|-------------|
| Consent & Introduction | Participant information and setup |
| Scenario Interaction   | Chat interface simulating ÖBB Assist responses |
| Post-Scenario Measures | User perception, behavioral intent, and UX ratings |
| Debriefing             | Explains research purpose |
| Optional Giveaway Page | Users may leave an email for a 50 EUR raffle |

Humor type and scenario severity are **assigned randomly** per participant using oTree randomization.

---

## ⚙️ Technologies

- **oTree** (Python-based behavioral experiment framework)
- **Bootstrap 5** for UI styling
- **JavaScript** for dynamic chat logic
- **Heroku / Cloud deployment** optional

---

## 🚀 Running Locally

```bash
otree devserver
