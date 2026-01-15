# Specify-Flow Reference

This project demonstrates the **Specify-Flow** paradigm for one-shot code generation of visual/interactive demos.

## What is Specify-Flow?

Specify-Flow is the integration between:
- **Spec-Kit**: A framework for Specification-Driven Development (SDD)
- **Claude-Flow**: An AI orchestration platform with swarm intelligence

Together, they enable intelligent code generation where specifications drive implementation through specialized AI agent swarms.

## How This Project Was Built

### 1. Specification Phase

Natural language description of requirements:
```
Create 5 classic LLM coding benchmark demos:
1. Bouncing ball in rotating polyhedron (physics, 3D collision)
2. DVD logo bounce (color change on corner hits)
3. Conway's Game of Life (cellular automaton)
4. 3D rotating cube (perspective projection)
5. Particle system / fireworks (dynamic effects)

Include a GUI launcher application.
```

### 2. Planning Phase

The architect swarm determined:
- All demos as standalone HTML files (self-contained)
- Python + tkinter for cross-platform GUI
- Local HTTP server for demo serving
- No external dependencies

### 3. Implementation Phase

Each demo was generated in parallel by the development swarm:
- One-shot generation (no iterations)
- Complete physics/rendering implementations
- Interactive controls
- Visual polish (gradients, shadows, effects)

## Demo Specifications

### 01-bouncing-polyhedron

**Requirements:**
- 3D icosahedron with perspective projection
- Ball with physics (gravity, bouncing, friction)
- Real-time collision detection with faces
- Color change on collision
- Trail effect
- Rotation controls

**Technical Implementation:**
- 3D rotation matrices
- Face normal calculation for collision
- Painter's algorithm for depth sorting
- Canvas 2D rendering with 3D math

### 02-dvd-logo

**Requirements:**
- Classic DVD logo bouncing
- Color change on wall bounce
- Special celebration on corner hits
- Statistics tracking (bounces, corners, time)
- Trail effect

**Technical Implementation:**
- Simple 2D physics
- Corner detection algorithm
- Text rendering with glow effects

### 03-game-of-life

**Requirements:**
- Conway's rules implementation
- Interactive cell drawing
- Pre-built patterns (glider, pulsar, glider gun)
- Play/pause/step controls
- Statistics (generation, population, births, deaths)
- Speed control

**Technical Implementation:**
- Toroidal grid (wrap-around edges)
- Efficient neighbor counting
- Color based on neighbor count

### 04-rotating-cube

**Requirements:**
- 3D cube with perspective
- Multiple rendering styles
- Mouse drag rotation
- Scroll zoom
- Multiple cubes support

**Technical Implementation:**
- Rotation matrices (X, Y, Z axes)
- Perspective projection
- Back-face culling
- Multiple render modes (neon, wireframe, solid, gradient, rainbow)

### 05-particle-system

**Requirements:**
- Firework rockets with explosion
- Multiple explosion styles
- Click-to-launch interaction
- Auto mode
- Performance stats (particle count, FPS)

**Technical Implementation:**
- Particle class with physics
- Rocket class with trajectory
- Multiple explosion patterns
- Trail rendering
- Object pooling concepts

## Benefits of Specify-Flow

1. **One-shot generation**: Complete working demos without iteration
2. **Consistent quality**: All demos follow similar patterns and polish
3. **Parallel development**: Multiple demos generated simultaneously
4. **Self-contained**: No external dependencies, just HTML/CSS/JS

## Learn More

- [Spec-Kit Repository](https://github.com/github/spec-kit)
- [Claude-Flow Repository](https://github.com/ruvnet/claude-flow)
- [SDD Methodology](https://github.com/github/spec-kit/blob/main/spec-driven.md)
