# Mermaid Style Guide for Autonomous Agents

## Overview

This style guide provides standards and patterns for creating Mermaid diagrams in the context of autonomous agents and system documentation.

## General Principles

### Color Scheme
```yaml
standard_colors:
  main_node: "#f9f"  # Primary/Root nodes
  sub_node: "#aaf"   # Secondary/Category nodes
  detail_node: "#afa" # Tertiary/Detail nodes
  leaf_node: "#faa"  # Final/Implementation nodes
  
stroke_styles:
  primary: "stroke:#333,stroke-width:4px"
  secondary: "stroke:#333,stroke-width:2px"
  standard: "stroke:#333"
```

### Standard Class Definitions
```mermaid
graph TD
    %% Class Definition Example
    classDef mainNode fill:#f9f,stroke:#333,stroke-width:4px
    classDef subNode fill:#aaf,stroke:#333,stroke-width:2px
    classDef detailNode fill:#afa,stroke:#333
    classDef leafNode fill:#faa,stroke:#333

    %% Example Nodes
    A((Root Node)) --> B[Category Node]
    B --> C[Detail Node]
    C --> D[Leaf Node]

    %% Class Applications
    class A mainNode
    class B subNode
    class C detailNode
    class D leafNode
```

## Diagram Types and Use Cases

### 1. System Architecture (graph TD)
```mermaid
graph TD
    %% Main System Structure
    ROOT((System Core)) --> A[Module A]
    ROOT --> B[Module B]
    ROOT --> C[Module C]

    %% Detailed Implementation
    A --> A1[Component 1]
    A --> A2[Component 2]
    B --> B1[Component 1]
    C --> C1[Component 1]

    %% Relationships
    A1 -.-> B1
    B1 -.-> C1

    %% Styling
    classDef core fill:#f9f,stroke:#333,stroke-width:4px
    classDef module fill:#aaf,stroke:#333
    classDef component fill:#afa,stroke:#333

    class ROOT core
    class A,B,C module
    class A1,A2,B1,C1 component
```

### 2. Process Flows (flowchart)
```mermaid
flowchart TD
    %% Process States
    Start([Start]) --> Init[Initialize Agent]
    Init --> Sense{Sense Environment}
    Sense --> Plan[Plan Action]
    Plan --> Act[Execute Action]
    Act --> Evaluate{Evaluate Result}
    
    %% Decision Flows
    Evaluate -->|Success| Update[Update Knowledge]
    Evaluate -->|Failure| Retry[Retry Action]
    Update --> Sense
    Retry --> Plan

    %% Styling
    classDef start fill:#f9f,stroke:#333
    classDef process fill:#aaf,stroke:#333
    classDef decision fill:#afa,stroke:#333
    
    class Start start
    class Init,Plan,Act,Update,Retry process
    class Sense,Evaluate decision
```

### 3. State Machines (stateDiagram-v2)
```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Processing: receive_task
    Processing --> Executing: plan_ready
    Executing --> Evaluating: action_complete
    Evaluating --> Idle: success
    Evaluating --> Processing: failure
    Executing --> Error: error
    Error --> Idle: reset
    
    note right of Processing
        Agent planning phase
    end note
```

### 4. Sequence Diagrams (for Agent Interactions)
```mermaid
sequenceDiagram
    participant U as User
    participant A as Agent
    participant E as Environment
    participant K as Knowledge Base

    U->>A: Request Action
    activate A
    A->>E: Sense Environment
    E-->>A: Environment State
    A->>K: Query Knowledge
    K-->>A: Relevant Information
    A->>A: Plan Action
    A->>E: Execute Action
    E-->>A: Action Result
    A->>K: Update Knowledge
    A-->>U: Action Complete
    deactivate A
```

### 5. Hierarchical Systems (graph TD with subgraphs)
```mermaid
graph TD
    %% Main System
    subgraph Agent System
        A((Agent Core))
        subgraph Cognitive Module
            C1[Perception]
            C2[Planning]
            C3[Learning]
        end
        subgraph Action Module
            A1[Movement]
            A2[Manipulation]
            A3[Communication]
        end
        subgraph Knowledge Base
            K1[World Model]
            K2[Task Knowledge]
            K3[Experience]
        end
    end

    %% Connections
    A --> C1
    A --> C2
    A --> C3
    C2 --> A1
    C2 --> A2
    C2 --> A3
    C1 --> K1
    C2 --> K2
    C3 --> K3

    %% Styling
    classDef core fill:#f9f,stroke:#333,stroke-width:4px
    classDef module fill:#aaf,stroke:#333
    classDef component fill:#afa,stroke:#333

    class A core
    class C1,C2,C3,A1,A2,A3 module
    class K1,K2,K3 component
```

## Best Practices

### 1. Node Naming Conventions
```yaml
naming_conventions:
  root_nodes: "ALL_CAPS or PascalCase with (( ))"
  category_nodes: "PascalCase with [ ]"
  detail_nodes: "CamelCase with [ ]"
  action_nodes: "verbNoun with ( )"
```

### 2. Relationship Types
```mermaid
graph LR
    A[Node A] --> B[Node B]
    A -.-> C[Node C]
    A ==> D[Node D]
    A --o E[Node E]
    A --x F[Node F]

    %% Legend
    L1[Solid Line] --> L2[Standard Flow]
    L3[Dotted Line] -.-> L4[Optional Flow]
    L5[Double Line] ==> L6[Strong Connection]
    L7[Circle End] --o L8[Aggregation]
    L9[Cross End] --x L10[Termination]
```

### 3. Subgraph Organization
```mermaid
graph TD
    subgraph Main System
        direction TB
        M((Core))
        subgraph Subsystem A
            direction LR
            A1[Component] --> A2[Component]
        end
        subgraph Subsystem B
            direction LR
            B1[Component] --> B2[Component]
        end
    end

    M --> A1
    M --> B1
```

### 4. Documentation Comments
```mermaid
graph TD
    %% System Overview
    %% This section defines the main system structure

    %% Main Components
    ROOT((System)) --> A[Component A]
    
    %% Subsystems
    %% Each subsystem should be documented
    
    %% Relationships and Flows
    %% Define how components interact

    %% Styling and Visual Hierarchy
    classDef main fill:#f9f
```

## Implementation Examples

### 1. Agent Architecture
```mermaid
graph TD
    %% Agent Core Structure
    AGENT((Autonomous Agent)) --> P[Perception]
    AGENT --> C[Cognition]
    AGENT --> A[Action]
    
    %% Perception System
    P --> P1[Sensors]
    P --> P2[Processing]
    P --> P3[Feature Extraction]
    
    %% Cognitive System
    C --> C1[Planning]
    C --> C2[Learning]
    C --> C3[Decision Making]
    
    %% Action System
    A --> A1[Motor Control]
    A --> A2[Task Execution]
    A --> A3[Feedback]

    %% Styling
    classDef core fill:#f9f,stroke:#333,stroke-width:4px
    classDef system fill:#aaf,stroke:#333
    classDef component fill:#afa,stroke:#333

    class AGENT core
    class P,C,A system
    class P1,P2,P3,C1,C2,C3,A1,A2,A3 component
```

### 2. Knowledge Integration
```mermaid
graph TD
    %% Knowledge System
    KB((Knowledge Base)) --> WK[World Knowledge]
    KB --> TK[Task Knowledge]
    KB --> EK[Experiential Knowledge]
    
    %% World Knowledge
    WK --> W1[Environment Model]
    WK --> W2[Object Relations]
    WK --> W3[Physical Laws]
    
    %% Task Knowledge
    TK --> T1[Goals]
    TK --> T2[Procedures]
    TK --> T3[Constraints]
    
    %% Experiential Knowledge
    EK --> E1[Past Actions]
    EK --> E2[Outcomes]
    EK --> E3[Learned Patterns]

    %% Styling
    classDef kb fill:#f9f,stroke:#333,stroke-width:4px
    classDef domain fill:#aaf,stroke:#333
    classDef knowledge fill:#afa,stroke:#333

    class KB kb
    class WK,TK,EK domain
    class W1,W2,W3,T1,T2,T3,E1,E2,E3 knowledge
```

## Maintenance and Updates

### Version Control
- Use clear commit messages for diagram updates
- Document significant changes in diagram structure
- Maintain backward compatibility when possible

### Quality Checks
- Verify all nodes are properly connected
- Ensure consistent styling across diagrams
- Check for proper nesting in subgraphs
- Validate relationship logic

## References

1. [Mermaid JS Documentation](https://mermaid.js.org/)
2. [Graph Theory Fundamentals](https://en.wikipedia.org/wiki/Graph_theory)
3. [System Architecture Patterns](https://en.wikipedia.org/wiki/Architectural_pattern)

## Tags
#documentation #diagrams #system-design #autonomous-agents #visualization 