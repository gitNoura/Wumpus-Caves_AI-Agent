# 🕵️‍♂️ Wumpus World AI Agent  
## 🌟 Overview  
The **Wumpus World** project explores the creation of a logical agent using the **JESS Expert System Shell** to navigate a cave-based environment, identify hazards, and accomplish goals such as collecting gold and eliminating the Wumpus. This project applies **knowledge representation**, **logical inferencing**, and **decision-making** principles to build an intelligent agent capable of tackling the challenges of the Wumpus World.  

---

## 🔍 Introduction  
The **Wumpus World** is a classic AI problem that simulates an agent navigating a partially observable, deterministic, and sequential environment. The agent must:  
1. **Detect hazards** (e.g., pits and the Wumpus).  
2. **Pick up gold** for rewards.  
3. **Eliminate the Wumpus** using arrows.  

Using the **JESS Expert System Shell**, we implemented and enhanced a rule-based agent capable of decision-making and adapting to new information in this environment.  

---

## 🌌 Game Environment  
- **Cave Layout**: The Wumpus World consists of interconnected caves, each representing a discrete room.  
- **Hazards**:  
  - **Wumpus**: A dangerous creature that emits a stench in adjacent caves.  
  - **Pits**: Fatal traps that emit a breeze in adjacent caves.  
- **Sensors**:  
  - **Stench**: Indicates proximity to the Wumpus.  
  - **Breeze**: Indicates proximity to a pit.  
  - **Glitter**: Indicates the presence of gold.  
  - **Bump**: Detects walls.  
  - **Scream**: Heard when the Wumpus is killed.  

### Environment Properties:  
- **Partially Observable**: The agent perceives only adjacent rooms.  
- **Deterministic**: Outcomes of actions are predictable.  
- **Static**: The environment does not change during gameplay.  

---

## 💻 JESS Environment  
JESS (Java Expert System Shell) is a rule-based expert system that provides:  
- **Knowledge Representation**: Facts and rules about the Wumpus World.  
- **Inferencing**: Logical reasoning to update knowledge and make decisions.  
- **Backward Chaining**: Determines facts required to achieve goals.  

---

## 🛠️ Tasks and Implementations  

### Task 1: Improve the Hunter’s Reasoning  
- Enhanced the agent's ability to **deduce exact locations** of hazards using stench and breeze indicators.  
- **Implementation**:  
  - Used JESS queries to evaluate adjacent caves.  
  - Created rules to update knowledge when only one possible hazard location remains.  
  - Ensured the agent distinguishes between "MAYBE" and "TRUE" hazard states.  

---

### Task 2: New Goal – Kill the Wumpus  
- Introduced a **new goal** for the agent: eliminating the Wumpus.  
- **Key Additions**:  
  - Added an `arrows` slot to the agent to track ammunition.  
  - Implemented the `shoot` action, enabling the agent to kill the Wumpus if adjacent.  
  - Adjusted goals to prioritize both collecting gold and killing the Wumpus.  

---

### Task 3: Navigation Enhancements  
- Improved the agent’s ability to navigate to distant caves without getting stuck.  
- **Approach**:  
  - Identified scenarios where the agent failed to proceed.  
  - Updated rules to allow goal-setting and step-by-step navigation toward distant targets.  

---

### Task 4: Prioritize Actions  
- Enabled the agent to **choose the best action** when multiple options are available.  
- **Action Hierarchy**:  
  1. **Shoot Wumpus** (if adjacent).  
  2. **Pick up Gold** (if present).  
  3. **Move to a safer cave**.  

---

### Task 5: Evaluate Agent Performance  
- Evaluated the agent's precision and accuracy across **50 random scenarios**.  
- **Metrics**:  
  - **True Positives (TP)**: Correctly identified and acted on hazards/gold.  
  - **True Negatives (TN)**: Correctly avoided non-existent hazards/gold.  
  - **False Positives (FP)**: Incorrectly acted when no action was needed.  
  - **False Negatives (FN)**: Failed to act when required.  
- **Results**:  
  - **Precision**: 100% (no false positives).  
  - **Accuracy**: 70% (indicating room for improvement in decision-making).  

---

## ⚠️ Challenges and Insights  

### Challenges:  
1. **Learning JESS**: Understanding JESS’s syntax and inferencing mechanisms.  
2. **Complex Rules**: Translating Wumpus World mechanics into accurate rules.  
3. **Testing**: Evaluating agent behavior across varied scenarios required extensive debugging.  

---

