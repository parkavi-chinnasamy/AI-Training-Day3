# Day 3 – Build a ReAct Agent from Scratch

## Overview

Day 3 focuses on building a **ReAct (Reason + Act) agent from scratch using Python**.

The agent can understand a user question, decide which tool is required, execute the tool, observe the result, and continue until it can provide a final answer.

In this task, two tools were implemented:

- Calculator
- Webpage/File Reader

The agent was also intentionally tested with failure cases and then improved using safety guards.

---

## Problem Statement

Build an AI agent that can answer questions requiring information from a webpage or local file and perform calculations using the retrieved information.

For example:

> Read `notice.html` and calculate the total fee for CS101 and AI202 after applying the 10% merit scholarship.

The agent should read the webpage, perform the required calculation, and provide the final answer.

---

## Objectives

- Understand the ReAct agent architecture.
- Build a ReAct loop using plain Python.
- Create and use custom tools.
- Connect the agent to an LLM.
- Handle tool errors safely.
- Test common agent failure modes.
- Add guards to make the agent more reliable.

---

## Tools Implemented

### 1. Calculator

The `calculator()` tool evaluates basic mathematical expressions.

2. Webpage Reader

The read_webpage() tool can read:

Local HTML files
Local text files
HTTP/HTTPS webpages

It extracts readable text and removes HTML tags, scripts, and styles.
