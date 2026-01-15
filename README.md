# LLM Benchmark Demos

Classic coding challenges used to evaluate LLM code generation capabilities. These demos were generated using the **Specify-Flow** paradigm - a one-shot approach to creating visual/interactive applications.

## Demos Included

| Demo | Description |
|------|-------------|
| **01-bouncing-polyhedron** | Ball bouncing inside a rotating 3D icosahedron with physics simulation |
| **02-dvd-logo** | The classic DVD screensaver - tracks bounces and corner hits |
| **03-game-of-life** | Conway's Game of Life with patterns and interactive drawing |
| **04-rotating-cube** | 3D rotating cube with multiple rendering styles |
| **05-particle-system** | Fireworks and particle effects with multiple modes |

## Quick Start

### Option 1: GUI Launcher (Recommended)

```bash
python launcher.py
```

This opens a GUI application that:
- Starts a local web server
- Provides launch buttons for each demo
- Displays descriptions and tags

### Option 2: Open Directly

Simply open any `index.html` file in your browser:

```bash
# Linux
xdg-open 01-bouncing-polyhedron/index.html

# macOS
open 01-bouncing-polyhedron/index.html

# Windows
start 01-bouncing-polyhedron/index.html
```

### Option 3: Local Server

```bash
# Python 3
python -m http.server 8000

# Then open http://localhost:8000
```

## Screenshots

### Bouncing Ball in Rotating Polyhedron
Real-time 3D collision detection with color changes on impact.

### DVD Logo Bounce
Track bounces and celebrate corner hits!

### Conway's Game of Life
Add patterns like gliders, pulsars, and glider guns.

### 3D Rotating Cube
Multiple styles: neon, wireframe, solid, gradient, rainbow.

### Particle System & Fireworks
Click to launch - multiple effect styles available.

## Technical Details

All demos are built with:
- **Vanilla JavaScript** - no frameworks or libraries
- **HTML5 Canvas** - for rendering
- **CSS3** - for styling and effects

Each demo is self-contained in a single HTML file with embedded CSS and JavaScript.

## Specify-Flow Paradigm

These demos were generated using the Specify-Flow integration between:
- **Spec-Kit**: Specification-Driven Development framework
- **Claude-Flow**: AI orchestration platform with swarm intelligence

The paradigm enables:
1. Clear specification of requirements
2. Intelligent swarm-based code generation
3. One-shot creation of working applications

## License

MIT License - feel free to use, modify, and distribute.

---

*Generated with Specify-Flow - Claude-Flow + Spec-Kit Integration*
